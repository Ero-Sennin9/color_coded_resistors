from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox
from database_ui import Ui_UI3
from PyQt5.QtCore import Qt
import sqlite3


class DataBase(QMainWindow, Ui_UI3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_4.currentTextChanged.connect(self.current_char)  # подбор корректных значений для ввода
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        stores = cur.execute('''SELECT name FROM stores''').fetchall()  # получение всех магазинов
        self.comboBox.addItems([''] + [elem[0] for elem in stores])  # отображение магазинов на виджете
        con.close()  # закрытие бд
        self.pushButton.clicked.connect(self.show_results)  # отображение результатов
        self.tableWidget.doubleClicked.connect(self.delete_item)  # удаление резистора двойным нажатием на него
        self.pushButton_2.clicked.connect(self.clear_store)  # очистка магазина
        self.pushButton_3.clicked.connect(self.delete_store)  # удаление магазина
        self.pushButton_4.clicked.connect(self.add_store)  # добавление магазина
        self.pushButton_5.clicked.connect(self.clear_filters)  # очистка фильтров

    def show_results(self):  # отображение результатов
        request = []  # хранение фильтров
        degree = self.comboBox_7.currentText()[self.comboBox_7.currentText().index('^') + 1:]  # степень сопротивления
        data = {'streaks': self.comboBox_4.currentText(),  # характеристики резистора
                'resistance': [self.spinBox_2.text(), degree],
                'inaccuracy': self.comboBox_5.currentText(),
                'tkr': self.comboBox_2.currentText(),
                'power': self.spinBox.text(),
                'store': self.comboBox.currentText()}
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        for elem in data.keys():  # добавление в список выбранных фильтров
            if data[elem] not in ['', '0']:
                if elem == 'store':
                    store = cur.execute('''SELECT id FROM stores
                                                WHERE name == ?''', (data[elem],)).fetchall()[0][0]
                    request.append(f'storeId == {store}')
                elif elem == 'resistance':
                    if data[elem][0] != '0':
                        request.append(f'resistance == {data[elem][0]} AND degree == {data[elem][1]}')
                else:
                    request.append(f'{elem} == {data[elem]}')
        if request:
            results = cur.execute("""SELECT * FROM resistors
                                     WHERE """ + ' AND '.join(request)).fetchall()  # результаты
        else:
            results = cur.execute("""SELECT * FROM resistors""").fetchall()  # все резисторы из бд, если фильтры отсутствуют
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(len(results))
        self.tableWidget.setHorizontalHeaderLabels(['Id', 'Streaks', 'Resistance', 'Degree', 'Inaccuracy',
                                                    'Tkr', 'Power', 'Count', 'Store'])
        for i, row in enumerate(results):  # отображение результатов
            for j, elem in enumerate(row):
                if elem == None:
                    elem = '-'
                if j == 8:
                    elem = cur.execute("""SELECT name FROM stores WHERE id == ?""", (elem,)).fetchall()[0][0]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        con.close()  # закрытие бд

    def current_char(self):  # ограничения на ввод
        def char(max, enable_1, enable_2):
            self.spinBox_2.setMaximum(max)
            if not enable_1:
                self.comboBox_5.setCurrentText('')
            if not enable_2:
                self.comboBox_2.setCurrentText('')
            self.comboBox_2.setEnabled(enable_2)
            self.comboBox_5.setEnabled(enable_1)
        if self.comboBox_4.currentText() == '3':
            char(99, False, False)
        elif self.comboBox_4.currentText() == '4':
            char(99, True, False)
        elif self.comboBox_4.currentText() == '5':
            char(999, True, False)
        elif self.comboBox_4.currentText() in ['6', '']:
            char(999, True, True)

    def keyPressEvent(self, event):  # предупреждение о выходе
        if event.key() == Qt.Key_Escape:
            valid = QMessageBox.question(
                self, '', "Действительно выйти?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.close()

    def delete_item(self):  # удаление резистора из дб
        elem = self.tableWidget.selectedItems()[0]  # выбранный резистор
        id = self.tableWidget.item(elem.row(), 0).text()  # его id
        con = sqlite3.connect('resistors.db')  # подключение бд
        cur = con.cursor()  # создание курсора
        cur.execute("""DELETE FROM resistors
                       WHERE id == ?""", (id,))  # удаление резистора из дб
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд
        self.show_results()  # отображение результата без удаленного резистора

    def delete_or_clear(self, button=1):  # удаление/очистка магазинов
        con = sqlite3.connect('resistors.db')  # открытие бд
        cur = con.cursor()  # создание курсора
        stores = [el[0] for el in cur.execute("""SELECT name FROM stores""")]  # получение всех магазинов
        store = self.selectStore(list(stores))  # выбор магазина для удаления/очистки
        if store != None:
            id = cur.execute("""SELECT id FROM stores
                                                WHERE name == ?""", (store,)).fetchall()[0][0]  # id магазина
            cur.execute("""DELETE FROM resistors
                                           WHERE storeId == ?""", (id,))  # удаление резисторов с нужным id магазина
            if button == 1:  # если происходит удаление магазина
                cur.execute("""DELETE FROM stores
                                       WHERE id == ?""", (id,))  # удаление магазина
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд
        self.show_results()  # отображение результатов с учетом удаления или очистки магазинов

    def delete_store(self):  # удалить склад
        self.delete_or_clear()

    def clear_store(self):  # очистить склад
        self.delete_or_clear(button=2)

    def selectStore(self, stores):  # выбор склада для удаления/очистки
        count, ok_pressed = QInputDialog.getItem(
            self, "", "Выберите магазин",
            tuple(stores), 0, False)
        if ok_pressed:
            return count

    def get_Store(self):  # ввод склада для добавления
        count, ok_pressed = QInputDialog.getText(
            self, "", "Введите название магазина")
        if ok_pressed:
            return count

    def add_store(self):  # добавление склада
        con = sqlite3.connect('resistors.db')  # открытие бд
        cur = con.cursor()  # создание курсора
        store = self.get_Store()  # склад для добавления
        if store != None:
            cur.execute("""INSERT INTO stores(name) VALUES(?)""", (store,))  # добавление склада
        con.commit()  # синхронизация с бд
        con.close()  # закрытие бд

    def clear_filters(self):
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(2)
        self.spinBox_2.setValue(0)
        self.spinBox.setValue(0)

