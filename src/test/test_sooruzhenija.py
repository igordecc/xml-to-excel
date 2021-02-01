from sooruzhenija import xml_to_excel, run
import os
import pytest
import _pytest

# py -3 -m pytest sooruzhenija.py

def test_run():
    inputdir = "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\сооружения\\xml_сооружения_29.12.2020"
    outputdir = "D:\\"

    got_items = run(inputdir, outputdir)
    gave_items = len(os.listdir(inputdir))

    assert got_items == gave_items


def test_xml_to_excel():
    inputdir = "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\сооружения\\xml_сооружения_29.12.2020"
    outputf = "D:\\Выписки_Сооружения.xlsx"

    got_items = xml_to_excel(inputdir, outputf)
    gave_items = len(os.listdir(inputdir))

    assert got_items == gave_items

