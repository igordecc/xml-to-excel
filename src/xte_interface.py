import sys
import os
import xml_to_excel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QFileDialog, QAction)
import traceback

from PyQt5.QtGui import QIcon


class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        choose_in_b = QPushButton("выбрать директорию xml")
        choose_out_b = QPushButton("выбрать директорию вывода")
        runb = QPushButton("добавить надпись")

        choose_in_b.addAction(QAction(QIcon('open.png'), 'Open', self))
        choose_in_b.setStatusTip('Выберите директорию с xml файлами')
        choose_in_b.clicked.connect(self.chooseInDialog)

        choose_out_b.addAction(QAction(QIcon('open.png'), 'Open', self))
        choose_out_b.setStatusTip('Выберите директорию с для сохранение excel файла с выгрузкой данных')
        choose_out_b.clicked.connect(self.chooseOutDialog)

        runb.addAction(QAction(QIcon('run.png'), 'Run', self))
        runb.setStatusTip('Запустить программу')
        runb.clicked.connect(self.runProgram)

        vbox = QVBoxLayout()
        vbox.addWidget(choose_in_b)
        vbox.addWidget(choose_out_b)
        vbox.addWidget(runb)

        self.setLayout(vbox)
        self.setFixedSize(280, 180)

        self.setWindowTitle('Добавить надпись')
        self.show()

    def chooseInDialog(self):
        self.dirin = QFileDialog.getExistingDirectory(None, "Выберете папку")
        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print(f"Выбраны xml {self.dirin}")

    def chooseOutDialog(self):
        self.dirout = QFileDialog.getExistingDirectory(None, "Выберете папку")
        self.fileout =os.path.join(self.dirout, "Вывод.xlsx")
        print(f"Выбран вывод excel {self.dirout}")

    def runProgram(self):
        if not hasattr(self, "dirin"):
            print("Выберите xml")
        elif not hasattr(self, "dirout"):
            print("Выберите excel")
        else:
            print("Выполняется...")
            xml_to_excel.do_all(self.dirin, self.fileout)

    def setUp(self):
        self.no_exceptions = True

        def testExcetionHook(type, value, tback):
            self.no_exceptions = False
            sys.__excepthook__(type, value, tback)

        sys.excepthook = testExcetionHook

    def tearDown(self):
        assert self.no_exceptions


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.setUp()
    ex.tearDown()
    sys.exit(app.exec_())