from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from transfer_ui import Ui_UI4
from PyQt5.QtCore import Qt
import sqlite3


class Transfer(QMainWindow, Ui_UI4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.transfer)  # перевод резисторов
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        stores = [elem[0] for elem in cur.execute('''SELECT name FROM stores''').fetchall()]  # получение всех магазинов
        self.comboBox.addItems(stores)  # отображение их на виджете
        con.close()  # закрытие бд
        self.comboBox.currentTextChanged.connect(self.show_res)  # отображение резисторов в данном магазине
        self.current_value()  # в comboBox_2 не должно быть выбранного магазина из comboBox
        self.show_res()  # отображение результатов

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # предупреждение о выходе
            valid = QMessageBox.question(
                self, '', "Действительно выйти?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.close()

    def show_res(self):
        self.current_value()  # в comboBox_2 не должно быть выбранного магазина из comboBox
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        store = cur.execute('''SELECT id FROM stores WHERE name == ?''',
                            (self.comboBox.currentText(),)).fetchall()[0][0]  # id выбранного магазина
        results = cur.execute('''SELECT * FROM resistors WHERE storeId == ?''',
                              (store,)).fetchall()  # результаты с данным id
        con.close()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(len(results))
        self.tableWidget.setHorizontalHeaderLabels(['Id', 'Streaks', 'Resistance', 'Degree', 'Inaccuracy',
                                                    'Tkr', 'Power', 'Count'])
        for i, row in enumerate(results):  # отображение результатов на виджете
            for j, elem in enumerate(row):
                if elem == None:
                    elem = '-'
                if j != 8:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def current_value(self):
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        stores = [elem[0] for elem in cur.execute('''SELECT name FROM stores''').fetchall()]  # получение всех магазинов
        del stores[stores.index(self.comboBox.currentText())]  # удаление выбранного магазина в comboBox
        self.comboBox_2.clear()  # очистка виджета
        self.comboBox_2.addItems(stores)  # добавление в него магазинов без выбранного в comboBox
        con.close()  # закрытие бд

    def transfer(self):
        data = []  # список для хранения фильтров резисторов для перевода с одного склада на другой
        for elem in self.tableWidget.selectedItems():
            id = self.tableWidget.item(elem.row(), 0)  # id выбранных резисторов
            data.append('id = ' + id.text())  # добавление фильтра
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        store = cur.execute('''SELECT id FROM stores WHERE name = ?''',
                            (self.comboBox_2.currentText(),)).fetchall()[0][0]  # id магазина в который будет осущ. перевод
        cur.execute("""UPDATE resistors
                       SET storeId = ?
                       WHERE ?""", (store, ' AND '.join(list(set(data)))))  # изменение id магазина вследствие перевода(не работает)
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд
        self.show_res()  # отображение результатов
