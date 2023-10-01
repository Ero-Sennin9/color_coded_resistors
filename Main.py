import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MarkingOfResistors
from Marking import Marking
from Reverse_marking import MarkingRev
from database import DataBase
from transfer import Transfer


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
