from PyQt5.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QMessageBox
from reverse_marking_ui import Ui_UI2
from PyQt5.QtCore import Qt
from streaks import data, data2
import csv
from PIL import Image
from PyQt5.QtGui import QPixmap
import sqlite3


class MarkingRev(QMainWindow, Ui_UI2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Картинка (*.png)')[0]  # выбор картинки
        self.label.setPixmap(QPixmap(self.fname))  # ее отображение на виджете
        self.count = self.selectCount()  # выбор числа полосок
        self.getting_char(self.fname, self.count)  # отображение характеристик
        self.pushButton.clicked.connect(self.add_to_database)  # связывание нажатия кнопки и добавления в бд
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        stores = cur.execute('''SELECT name FROM stores''').fetchall()  # получение всех магазинов из бд
        self.comboBox_5.addItems([elem[0] for elem in stores])  # добавление магазинов в comboBox
        con.close()  # закрытие бд
        self.error = False  # переменная, хранящая информацию о наличии ошибок

    def selectCount(self):  # выбор числа полосок
        count, ok_pressed = QInputDialog.getItem(
            self, "", "Выберите число полосок",
            ("Авто", "3", "4", "5", "6"), 0, False)
        if ok_pressed:
            if count == "Авто":
                count = self.auto_count()
            return count

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # предупреждение о выходе
            valid = QMessageBox.question(
                self, '', "Действительно выйти?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.close()

    def getting_char(self, fname, count):  # отображение характеристик
        try:
            self.picture = Image.open(fname)  # открытие выбранной картинки
            pixels = self.picture.load()  # загрузка ее пикселей
            with open('colors.csv', encoding="utf8") as csvfile:
                reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))  # список с цветами и характеристиками
            res = []  # хранение цветов полоски
            for i in range(len(data[count])):
                x = data[count][i][0][0]  # координаты пикселей по которым определяется цвет полоски
                y = data[count][i][0][1]
                res.append(reader[1].index(', '.join(list(map(str, list(pixels[x, y]))))))  # определение цвета полоски по csv
            for i in range(int(count)):
                res[i] = reader[data2[count][i]][res[i]]  # замена цветов в списке на характеристики
            if count == '3':  # отображение характеристик на виджетах
                self.lineEdit.setText(str(int(res[0] + res[1])) + f' * 10^{res[2]}')
            elif count == '4':
                self.lineEdit.setText(str(int(res[0] + res[1])) + f' * 10^{res[2]}')
                self.lineEdit_2.setText(res[3])
            elif count == '5':
                self.lineEdit.setText(str(int(res[0] + res[1] + res[2])) + f' * 10^{res[4]}')
                self.lineEdit_2.setText(res[3])
            elif count == '6':
                self.lineEdit.setText(str(int(res[0] + res[1] + res[2])) + f' * 10^{res[4]}')
                self.lineEdit_2.setText(res[5])
                self.lineEdit_3.setText(res[3])
        except AttributeError:
            self.error = True
        except ValueError:
            valid = QMessageBox.question(
                self, '', """Ошибка!
Выбрана некоректная картинка или неправильное число полос""",
                QMessageBox.Ok)
            if valid == QMessageBox.Ok:
                self.error = True

    def add_to_database(self):  # добавление резистора в бд
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        store = cur.execute('''SELECT id FROM stores
                            WHERE name == ?''', (self.comboBox_5.currentText(),)).fetchall()[0][0]  # выбранный магазин
        cur.execute("""INSERT INTO resistors(resistance, degree, inaccuracy, tkr, power, count, storeId, streaks)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                    (self.lineEdit.text()[:self.lineEdit.text().find('*') - 1],
                     self.lineEdit.text()[self.lineEdit.text().find('^') + 1:],
                     self.lineEdit_2.text(), self.lineEdit_3.text(), self.spinBox_3.text(), self.spinBox_2.text(),
                     store, self.count))  # добавление резистора в бд
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд

    def auto_count(self):  # автоматическое определение числа полос
        streaks = sorted(list(data.values()), key=lambda s: len(s), reverse=True)  # список с координатами полос
        im = Image.open(self.fname)  # открытие выбранной картинки
        pixels = im.load()  # ее пиксели
        for elem in streaks:
            self.Err = False  # переменная, хранящая информацию об ошибке
            try:
                with open('colors.csv', encoding="utf8") as csvfile:
                    reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))  # список с цветами и характеристиками
                for i in range(len(elem)):
                    x = elem[i][0][0]  # координаты пикселей по которым определяется цвет полоски
                    y = elem[i][0][1]
                    reader[1].index(', '.join(list(map(str, list(pixels[x, y])))))  # определение цвета полоски
            except ValueError:  # если такого цвета нет в csv файле, то это ошибка и такое кол-во полос не подходит
                self.Err = True
            if not self.Err:  # если ошибки не произошло, возвращаем нужное число полос
                return str(streaks[-1::-1].index(elem) + 3)


