from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from Marking_ui import Ui_UI1
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap
import os
import csv
from streaks import data
import sqlite3


class Marking(QMainWindow, Ui_UI1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentTextChanged.connect(self.current_char)  # при изменении кол-ва полосок выставляются ограничения на ввод
        self.spinBox.valueChanged.connect(self.picture)  # при изменении параметров отрисовывается резистор
        self.comboBox.currentTextChanged.connect(self.picture)
        self.comboBox_2.currentTextChanged.connect(self.picture)
        self.comboBox_3.currentTextChanged.connect(self.picture)
        self.comboBox_4.currentTextChanged.connect(self.picture)
        self.pushButton_2.clicked.connect(self.save_picture)  # сохранение картинки
        self.pushButton.clicked.connect(self.add_to_database)  # добавление в бд
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        stores = cur.execute('''SELECT name FROM stores''').fetchall()  # получение магазинов
        self.comboBox_5.addItems([elem[0] for elem in stores])  # отображение их на виджете
        con.close()
        self.picture()  # рисование резистора

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # предупреждение о выходе
            valid = QMessageBox.question(
                self, '', "Действительно выйти?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.close()

    def current_char(self):  # отображение корректных значений
        def char(max, enable_1, enable_2):
            self.spinBox.setMaximum(max)
            self.comboBox_3.setEnabled(enable_1)
            self.comboBox_2.setEnabled(enable_2)
        if self.comboBox.currentText() == '3':
            char(99, False, False)
        elif self.comboBox.currentText() == '4':
            char(99, True, False)
        elif self.comboBox.currentText() == '5':
            char(999, True, False)
        elif self.comboBox.currentText() == '6':
            char(999, True, True)

    def picture(self):
        self.resistor = Image.new("RGB", (750, 260), (240, 240, 240))  # создание изображения, на котором будет рисоваться резистор
        draw = ImageDraw.Draw(self.resistor)
        draw.line((0, 125, 100, 125), fill='#D3D3D3', width=6)  # рисунок резистора без полос
        draw.line((650, 125, 750, 125), fill='#D3D3D3', width=6)
        draw.polygon(((100, 86), (100, 172), (143, 215), (229, 215), (272, 172), (478, 172), (521, 215),
                      (607, 215), (650, 172), (650, 86), (607, 43), (521, 43), (478, 86), (272, 86),
                      (229, 43), (143, 43)), '#cd7f32')
        with open('colors.csv', encoding="utf8") as csvfile:  # файл с цветами и характеристиками
            reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
            if self.comboBox.currentText() == '3':  # находим нужные цвета в файле
                colors = [reader[1][reader[2].index(str(int(self.spinBox.text()) // 10))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 10))],
                          reader[1][reader[3].index(self.comboBox_4.currentText()[5:])]]
            elif self.comboBox.currentText() == '4':
                colors = [reader[1][reader[2].index(str(int(self.spinBox.text()) // 10))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 10))],
                          reader[1][reader[3].index(str(self.comboBox_4.currentText()[5:]))],
                          reader[1][reader[4].index(self.comboBox_3.currentText())]]
            elif self.comboBox.currentText() == '5':
                colors = [reader[1][reader[2].index(str(int(self.spinBox.text()) // 100))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 100 // 10))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 10))],
                          reader[1][reader[4].index(self.comboBox_3.currentText())],
                          reader[1][reader[3].index(str(self.comboBox_4.currentText()[5:]))]]
            elif self.comboBox.currentText() == '6':
                colors = [reader[1][reader[2].index(str(int(self.spinBox.text()) // 100))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 100 // 10))],
                          reader[1][reader[2].index(str(int(self.spinBox.text()) % 10))],
                          reader[1][reader[5].index(self.comboBox_2.currentText())],
                          reader[1][reader[3].index(str(self.comboBox_4.currentText()[5:]))],
                          reader[1][reader[4].index(self.comboBox_3.currentText())]]
        for i in range(len(data[self.comboBox.currentText()])):  # рисование самих полосок
            color = tuple(map(int, colors[i].split(', ')))
            coord = data[self.comboBox.currentText()][i]
            draw.rectangle(coord, color)
        self.resistor.save('image.png')  # сохранение резистора
        self.label_6.setPixmap(QPixmap('image.png'))  # его отображение на виджете
        os.remove('image.png')  # удаление резистора

    def save_picture(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", "", 'Картинка (*.png)')[0]  # сохранение резистора
        if filename != '':  # если файл выбран, то сохраняем
            self.resistor.save(filename)

    def add_to_database(self):  # добавление резистора в бд
        con = sqlite3.connect('resistors.db')  # открытие бд
        cur = con.cursor()  # создание курсора
        count = self.comboBox.currentText()  # число полос
        store = cur.execute('''SELECT id FROM stores WHERE name == ?''',
                            (self.comboBox_5.currentText(),)).fetchall()[0][0]  # получение магазина
        if count == '3':  # подбор данных для сохранения исходя из кол-ва полос
            a, b = None, None
        elif count in '45':
            a, b = self.comboBox_3.currentText(), None
        else:
            a, b = self.comboBox_3.currentText(), self.comboBox_2.currentText()
        cur.execute("""INSERT INTO resistors(resistance, degree, inaccuracy, tkr, power, count, storeId, streaks)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                    (int(self.spinBox.text()), int(self.comboBox_4.currentText()[5:]),
                     a, b, int(self.spinBox_3.text()), int(self.spinBox_2.text()), store,
                     int(self.comboBox.currentText())))  # добавление резистора в бд
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд
