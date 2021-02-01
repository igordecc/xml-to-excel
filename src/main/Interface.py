"""
13.01.2021
Xml converter program with interface.
"""

import sys
import main_run
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QPushButton, QAction, QComboBox)
from PyQt5 import QtWidgets

from PyQt5.QtGui import QIcon



class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.pre_configuration()
        self.init_ui()
        self.final_configuration()

# --- user interface

    def pre_configuration(self):
        self.vbox = QVBoxLayout()

    def drop_down_menu(self):
        self.dropdown = QComboBox()
        self.dropdown.addItems([
                               "Здания",
                               "ОНС",
                               "Помещения",
                               "Машино-места",
                               "Сооружения",
                               "Земельные участки"
            ])
        self.module_name = self.dropdown.itemText(0)
        self.dropdown.activated.connect(self.selection_changed_dialog)
        self.vbox.addWidget(self.dropdown)


    def button_1(self):
        chooseb = QPushButton("выбрать xml директорию с файлами")
        chooseb.addAction(QAction(QIcon('open.png'), 'Open', self))
        chooseb.setStatusTip('Выбрать директорию с файлами выписок в формате xml ')
        chooseb.clicked.connect(self.choose_xml_file_dialog)
        self.vbox.addWidget(chooseb)


    def button_2(self):
        savef = QPushButton("выбрать папку сохранения")
        savef.addAction(QAction(QIcon('save_folder.png'), 'save_folder', self))
        savef.setStatusTip('Выберите папку для сохранения excel файла')
        savef.clicked.connect(self.save_folder_dialog)
        self.vbox.addWidget(savef)

    def button_3(self):
        runb = QPushButton("Конвертировать")
        runb.addAction(QAction(QIcon('run.png'), 'Run', self))
        runb.setStatusTip('Запустить программу')
        runb.clicked.connect(self.run_program)
        self.vbox.addWidget(runb)

    def init_ui(self):
        self.drop_down_menu()
        self.button_1()
        self.button_2()
        self.button_3()

    def final_configuration(self):
        self.setLayout(self.vbox)
        self.setFixedSize(280, 180)

        self.setWindowTitle('Конвертер выписок')
        self.show()

# --- dialogs
    def selection_changed_dialog(self, i):
        self.module_name = self.dropdown.itemText(i)
        print(self.module_name)

    def choose_xml_file_dialog(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Сохранить в папку', '/home')
        print(f"Выбрана директория ввода {folder_name}")
        self.input_folder = folder_name

    def save_folder_dialog(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, 'Сохранить в папку', '/home')
        print(f"Выбрана директория вывода {folder_name}")
        self.output_folder = folder_name

    def run_program(self):
        print(self.module_name)
        main_run.run(self.module_name, self.input_folder, self.output_folder)

# --- check system exceptions

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
