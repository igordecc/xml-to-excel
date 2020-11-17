import sys
import os
import xml_to_excel
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QFileDialog, QAction)


from PyQt5.QtGui import QIcon

class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        chooseb = QPushButton("выбрать csv")
        runb = QPushButton("добавить надпись")

        chooseb.addAction(QAction(QIcon('open.png'), 'Open', self))
        chooseb.setStatusTip('Выбрать csv файл со списком скриншотов')
        chooseb.clicked.connect(self.showDialog)

        runb.addAction(QAction(QIcon('run.png'), 'Run', self))
        runb.setStatusTip('Запустить программу')
        runb.clicked.connect(self.runProgram)

        vbox = QVBoxLayout()
        vbox.addWidget(chooseb)
        vbox.addWidget(runb)


        self.setLayout(vbox)
        self.setFixedSize(280, 180)

        self.setWindowTitle('Добавить надпись')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print("Выбрано")
        self.fname = fname


    def runProgram(self):
        xml_to_excel.main(file=self.fname)

    def setUp(self):
        self.no_exceptions = True

        def testExcetionHook(type, value, tback):
            self.no_exceptions = False
            sys.__excepthook__(type, value, tback)

        sys.excepthook = testExcetionHook

    def tearDown(self):
        assert self.no_exceptions


def main():
    app = QApplication(sys.argv)
    ex = UI()
    ex.setUp()
    ex.tearDown()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()