from sooruzhenija import xml_to_excel, run
import os
import pandas
import io
import pytest
import _pytest

# TO boot the pytest
# or customise pycharm
# py -3 -m pytest sooruzhenija.py


def test_run():
    inputdir = "D:\\PYTHON\\xml-to-excel\\src\\test\\resources\\сооружения\\test"
    outputdir = "D:\\"

    got_items = run(inputdir, outputdir)
    some = os.listdir(inputdir)
    gave_items = len(os.listdir(inputdir))
    # TODO GOT ITEMS not returning
    assert got_items == gave_items


def test_xml_to_excel():
    inputdir = "D:\\PYTHON\\xml-to-excel\\src\\test\\resources\\сооружения\\test"
    outputf = "D:\\Выписки_Сооружения.xlsx"

    got_items = xml_to_excel(inputdir, outputf)
    gave_items = len(os.listdir(inputdir))

    assert got_items == gave_items


def test_is_excel_the_same():
    pass


def read_excel(file_path):
    if os.path.isfile(file_path):
        df = pandas.read_excel(open(file_path, 'rb'))
        print(df)
        pass


def test_read_excel():
    read_excel("D:\\Выписки_Сооружения.xlsx")
# def test_field(field_number):
#
#     def test_field(*args, **kwargs):
#         return field_number
#
#     return test_field

