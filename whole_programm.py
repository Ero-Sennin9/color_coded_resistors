import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QFileDialog, QInputDialog, QMessageBox

from PIL import ImageDraw, Image
import os
from PyQt5.QtCore import Qt
import csv
from PyQt5.QtGui import QPixmap
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI4(object):
    def setupUi(self, UI4):
        UI4.setObjectName("UI4")
        UI4.resize(575, 600)
        self.centralwidget = QtWidgets.QWidget(UI4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        UI4.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI4)
        self.statusbar.setObjectName("statusbar")
        UI4.setStatusBar(self.statusbar)

        self.retranslateUi(UI4)
        QtCore.QMetaObject.connectSlotsByName(UI4)

    def retranslateUi(self, UI4):
        _translate = QtCore.QCoreApplication.translate
        UI4.setWindowTitle(_translate("UI4", "MainWindow"))
        self.pushButton.setText(_translate("UI4", "Перевод"))
        self.label_3.setText(_translate("UI4", "из"))
        self.label_4.setText(_translate("UI4", "в"))
        self.label_2.setText(_translate("UI4", "Выберите резисторы для перевода"))
        self.label.setText(_translate("UI4", "Для выхода нажмите esc"))


class Ui_UI3(object):
    def setupUi(self, UI3):
        UI3.setObjectName("UI3")
        UI3.resize(993, 355)
        self.centralwidget = QtWidgets.QWidget(UI3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 6, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 5, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_7)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 6, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 5, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 2, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        UI3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI3)
        self.statusbar.setObjectName("statusbar")
        UI3.setStatusBar(self.statusbar)

        self.retranslateUi(UI3)
        self.comboBox_7.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(UI3)

    def retranslateUi(self, UI3):
        _translate = QtCore.QCoreApplication.translate
        UI3.setWindowTitle(_translate("UI3", "MainWindow"))
        self.pushButton_3.setText(_translate("UI3", "Удалить склад"))
        self.pushButton_4.setText(_translate("UI3", "Добавить склад"))
        self.pushButton_2.setText(_translate("UI3", "Очистить склад"))
        self.label.setText(_translate("UI3", "Склад"))
        self.comboBox_5.setItemText(1, _translate("UI3", "10"))
        self.comboBox_5.setItemText(2, _translate("UI3", "5"))
        self.comboBox_5.setItemText(3, _translate("UI3", "2"))
        self.comboBox_5.setItemText(4, _translate("UI3", "1"))
        self.comboBox_5.setItemText(5, _translate("UI3", "0.5"))
        self.comboBox_5.setItemText(6, _translate("UI3", "0.25"))
        self.comboBox_5.setItemText(7, _translate("UI3", "0.1"))
        self.comboBox_5.setItemText(8, _translate("UI3", "0.05"))
        self.comboBox_4.setItemText(1, _translate("UI3", "3"))
        self.comboBox_4.setItemText(2, _translate("UI3", "4"))
        self.comboBox_4.setItemText(3, _translate("UI3", "5"))
        self.comboBox_4.setItemText(4, _translate("UI3", "6"))
        self.label_6.setText(_translate("UI3", "Сопротивление(Ом)"))
        self.label_7.setText(_translate("UI3", "Допуск(%)"))
        self.label_8.setText(_translate("UI3", "ТКС(ppm/OC)"))
        self.label_3.setText(_translate("UI3", "Мощность"))
        self.comboBox_2.setItemText(1, _translate("UI3", "100"))
        self.comboBox_2.setItemText(2, _translate("UI3", "50"))
        self.comboBox_2.setItemText(3, _translate("UI3", "25"))
        self.comboBox_2.setItemText(4, _translate("UI3", "15"))
        self.comboBox_2.setItemText(5, _translate("UI3", "10"))
        self.comboBox_2.setItemText(6, _translate("UI3", "5"))
        self.comboBox_2.setItemText(7, _translate("UI3", "1"))
        self.label_2.setText(_translate("UI3", "Кол-во полос"))
        self.comboBox_7.setCurrentText(_translate("UI3", "* 10^0"))
        self.comboBox_7.setItemText(0, _translate("UI3", "* 10^-2"))
        self.comboBox_7.setItemText(1, _translate("UI3", "* 10^-1"))
        self.comboBox_7.setItemText(2, _translate("UI3", "* 10^0"))
        self.comboBox_7.setItemText(3, _translate("UI3", "* 10^1"))
        self.comboBox_7.setItemText(4, _translate("UI3", "* 10^2"))
        self.comboBox_7.setItemText(5, _translate("UI3", "* 10^3"))
        self.comboBox_7.setItemText(6, _translate("UI3", "* 10^4"))
        self.comboBox_7.setItemText(7, _translate("UI3", "* 10^5"))
        self.comboBox_7.setItemText(8, _translate("UI3", "* 10^6"))
        self.comboBox_7.setItemText(9, _translate("UI3", "* 10^7"))
        self.comboBox_7.setItemText(10, _translate("UI3", "* 10^8"))
        self.comboBox_7.setItemText(11, _translate("UI3", "* 10^9"))
        self.label_9.setText(_translate("UI3", "Для выхода нажмите Esc"))
        self.label_4.setText(_translate("UI3", "Для удаления резистора кликните по нему два раза"))
        self.pushButton.setText(_translate("UI3", "Поиск"))
        self.pushButton_5.setText(_translate("UI3", "Очистить фильтр"))


class Ui_UI2(object):
    def setupUi(self, UI2):
        UI2.setObjectName("UI2")
        UI2.resize(740, 376)
        self.centralwidget = QtWidgets.QWidget(UI2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setBaseSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 2, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setMaximum(1000000000)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_2.addWidget(self.spinBox_3, 1, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 2, 1, 1)
        UI2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI2)
        self.statusbar.setObjectName("statusbar")
        UI2.setStatusBar(self.statusbar)

        self.retranslateUi(UI2)
        QtCore.QMetaObject.connectSlotsByName(UI2)

    def retranslateUi(self, UI2):
        _translate = QtCore.QCoreApplication.translate
        UI2.setWindowTitle(_translate("UI2", "MainWindow"))
        self.label_3.setText(_translate("UI2", "Сопротивление(Ом)"))
        self.label_4.setText(_translate("UI2", "Допуск(%)"))
        self.label_5.setText(_translate("UI2", "ТКС(ppm/OC)"))
        self.label_2.setText(_translate("UI2", "Для выхода нажмите Esc"))
        self.label_7.setText(_translate("UI2", "Мощность(Вт)"))
        self.label_8.setText(_translate("UI2", "Количество"))
        self.label_9.setText(_translate("UI2", "Магазин"))
        self.pushButton.setText(_translate("UI2", "Добавить на склад"))


class Ui_UI1(object):
    def setupUi(self, UI1):
        UI1.setObjectName("UI1")
        UI1.resize(770, 502)
        font = QtGui.QFont()
        font.setPointSize(10)
        UI1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(UI1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setProperty("value", 11)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setMaximum(1000000000)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout.addWidget(self.spinBox_3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setProperty("value", 1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout.addWidget(self.spinBox_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.gridLayout_2.addLayout(self.verticalLayout, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 2, 2)
        UI1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UI1)
        self.statusbar.setObjectName("statusbar")
        UI1.setStatusBar(self.statusbar)

        self.retranslateUi(UI1)
        self.comboBox_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UI1)

    def retranslateUi(self, UI1):
        _translate = QtCore.QCoreApplication.translate
        UI1.setWindowTitle(_translate("UI1", "MainWindow"))
        self.label_5.setText(_translate("UI1", "ТКС(ppm/OC)"))
        self.comboBox.setItemText(0, _translate("UI1", "3"))
        self.comboBox.setItemText(1, _translate("UI1", "4"))
        self.comboBox.setItemText(2, _translate("UI1", "5"))
        self.comboBox.setItemText(3, _translate("UI1", "6"))
        self.label_3.setText(_translate("UI1", "Сопротивление(Ом)"))
        self.label_4.setText(_translate("UI1", "Допуск(%)"))
        self.label.setText(_translate("UI1", "Кол-во полос"))
        self.comboBox_2.setItemText(0, _translate("UI1", "100"))
        self.comboBox_2.setItemText(1, _translate("UI1", "50"))
        self.comboBox_2.setItemText(2, _translate("UI1", "25"))
        self.comboBox_2.setItemText(3, _translate("UI1", "15"))
        self.comboBox_2.setItemText(4, _translate("UI1", "10"))
        self.comboBox_2.setItemText(5, _translate("UI1", "5"))
        self.comboBox_2.setItemText(6, _translate("UI1", "1"))
        self.comboBox_3.setItemText(0, _translate("UI1", "10"))
        self.comboBox_3.setItemText(1, _translate("UI1", "5"))
        self.comboBox_3.setItemText(2, _translate("UI1", "2"))
        self.comboBox_3.setItemText(3, _translate("UI1", "1"))
        self.comboBox_3.setItemText(4, _translate("UI1", "0.5"))
        self.comboBox_3.setItemText(5, _translate("UI1", "0.25"))
        self.comboBox_3.setItemText(6, _translate("UI1", "0.1"))
        self.comboBox_3.setItemText(7, _translate("UI1", "0.05"))
        self.comboBox_4.setCurrentText(_translate("UI1", "* 10^-2"))
        self.comboBox_4.setItemText(0, _translate("UI1", "* 10^-2"))
        self.comboBox_4.setItemText(1, _translate("UI1", "* 10^-1"))
        self.comboBox_4.setItemText(2, _translate("UI1", "* 10^0"))
        self.comboBox_4.setItemText(3, _translate("UI1", "* 10^1"))
        self.comboBox_4.setItemText(4, _translate("UI1", "* 10^2"))
        self.comboBox_4.setItemText(5, _translate("UI1", "* 10^3"))
        self.comboBox_4.setItemText(6, _translate("UI1", "* 10^4"))
        self.comboBox_4.setItemText(7, _translate("UI1", "* 10^5"))
        self.comboBox_4.setItemText(8, _translate("UI1", "* 10^6"))
        self.comboBox_4.setItemText(9, _translate("UI1", "* 10^7"))
        self.comboBox_4.setItemText(10, _translate("UI1", "* 10^8"))
        self.comboBox_4.setItemText(11, _translate("UI1", "* 10^9"))
        self.label_7.setText(_translate("UI1", "Мощность(Вт)"))
        self.label_8.setText(_translate("UI1", "Количество"))
        self.label_9.setText(_translate("UI1", "Магазин"))
        self.pushButton.setText(_translate("UI1", "Добавить на склад"))
        self.pushButton_2.setText(_translate("UI1", "Сохранить"))
        self.label_2.setText(_translate("UI1", "Для выхода нажмите Esc"))


class Ui_MarkingOfResistors(object):
    def setupUi(self, MarkingOfResistors):
        MarkingOfResistors.setObjectName("MarkingOfResistors")
        MarkingOfResistors.resize(497, 279)
        self.centralwidget = QtWidgets.QWidget(MarkingOfResistors)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        MarkingOfResistors.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MarkingOfResistors)
        self.statusbar.setObjectName("statusbar")
        MarkingOfResistors.setStatusBar(self.statusbar)

        self.retranslateUi(MarkingOfResistors)
        QtCore.QMetaObject.connectSlotsByName(MarkingOfResistors)

    def retranslateUi(self, MarkingOfResistors):
        _translate = QtCore.QCoreApplication.translate
        MarkingOfResistors.setWindowTitle(_translate("MarkingOfResistors", "MainWindow"))
        self.pushButton_4.setText(_translate("MarkingOfResistors", "Перевод с одного склада на другой"))
        self.pushButton.setText(_translate("MarkingOfResistors", "Найти резистор на складе"))
        self.pushButton_3.setText(_translate("MarkingOfResistors", "Определить хар-ки резистора"))
        self.pushButton_2.setText(_translate("MarkingOfResistors", "Маркировка резистора"))


data = {'3': [((209, 43), (229, 215)), ((272, 86), (292, 172)), ((332, 86), (352, 172))],
        '4': [((209, 43), (229, 215)), ((272, 86), (292, 172)),  # координаты полосок
              ((332, 86), (352, 172)), ((521, 43), (541, 215))],
        '5': [((209, 43), (229, 215)), ((272, 86), (292, 172)),
              ((332, 86), (352, 172)), ((521, 43), (541, 215)),
              ((392, 86), (412, 172))],
        '6': [((209, 43), (229, 215)), ((272, 86), (292, 172)),
              ((332, 86), (352, 172)), ((521, 43), (541, 215)),
              ((392, 86), (412, 172)), ((458, 86), (478, 172))]}

data2 = {'3': [2, 2, 3],  # соответсвие координат полосок и номеров строк в csv-файле, т.е. характеристик
         '4': [2, 2, 3, 4],
         '5': [2, 2, 2, 4, 3],
         '6': [2, 2, 2, 5, 3, 4]}


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
        self.pushButton_5.clicked.connect(self.clear_filters)

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


class MainWindow(QMainWindow, Ui_MarkingOfResistors):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Resistors')
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.marking)
        self.pushButton_3.clicked.connect(self.reverse_marking)
        self.pushButton.clicked.connect(self.database)
        self.pushButton_4.clicked.connect(self.transfer)

    def marking(self):
        self.window_1 = Marking()
        self.window_1.show()

    def reverse_marking(self):
        self.window_2 = MarkingRev()
        self.window_2.show()

    def database(self):
        self.window_3 = DataBase()
        self.window_3.show()

    def transfer(self):
        self.window_4 = Transfer()
        self.window_4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())