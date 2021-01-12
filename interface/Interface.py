import sys
import os
import xml_to_excel
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QPushButton, QFileDialog, QAction)
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from PyQt5.QtGui import QIcon


class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.pre_configuration()
        self.init_ui()
        self.final_configuration()

    def pre_configuration(self):
        self.vbox = QVBoxLayout()

    def button_1(self):
        chooseb = QPushButton("выбрать xml файл")

        chooseb.addAction(QAction(QIcon('open.png'), 'Open', self))
        chooseb.setStatusTip('Выбрать csv файл со списком скриншотов')
        chooseb.clicked.connect(self.choose_xml_file_dialog)

        self.vbox.addWidget(chooseb)

    def button_2(self):
        runb = QPushButton("трансформировать")

        runb.addAction(QAction(QIcon('run.png'), 'Run', self))
        runb.setStatusTip('Запустить программу')
        runb.clicked.connect(self.run_program)

        self.vbox.addWidget(runb)

    def button_3(self):
        savef = QPushButton("выбрать папку сохранения")

        savef.addAction(QAction(QIcon('save_folder.png'), 'save_folder', self))
        savef.setStatusTip('Выберите папку для сохранения')
        savef.clicked.connect(self.save_folder_dialog)

        self.vbox.addWidget(savef)

    def init_ui(self):
        self.button_1()
        self.button_2()
        self.button_3()

    def final_configuration(self):
        self.setLayout(self.vbox)
        self.setFixedSize(280, 180)

        self.setWindowTitle('Добавить надпись')
        self.show()

    def choose_xml_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        print(f"Выбран файл {file_name}")
        self.file_name = file_name

    def save_folder_dialog(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Сохранить в папку', '/home')
        print(f"Выбрана директория {folder_name}")
        self.folder_name = folder_name

    def run_program(self):
        pass
        xml_to_excel.main(self.file_name, self.folder_name)

    def set_up(self):
        self.no_exceptions = True

        def test_excetion_hook(type, value, tback):
            self.no_exceptions = False
            sys.__excepthook__(type, value, tback)

        sys.excepthook = test_excetion_hook

    def tearDown(self):
        assert self.no_exceptions


def main():
    app = QApplication(sys.argv)
    ex = UI()
    ex.set_up()
    ex.tearDown()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
