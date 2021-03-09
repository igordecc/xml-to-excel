from XmlConverterFabric import XmlConverterFabric
import try_modules as tm

import os, sys
import xmltodict
import pandas
import traceback
import datetime


class PomeshhenijaRow:
    def __init__(self, name, col_max=26, *args, **kwargs):
        self.filename = name
        self.COL_MAX_NUM = col_max

    def __call__(self):
        try:
            with open(self.filename, encoding="utf8") as opened_file:
                self.xml_nested_dict = xmltodict.parse(opened_file.read())
        except:
            print("Ошибка чтения файла: " + self.filename)
            print(f"код {sys.exc_info()[0].__dict__}")
            traceback.print_exc()
            return lambda x: None

        # PHASE 1 - extract xml Data into xml Table! Keep track of to which excel_column The Data will go ;)

        self.xml_value_table = []

        ANCHOR0 = len(self.xml_value_table)
        # Oh, I'm appending xml table iteratively
        # then I'm appending excel iteratively ( but just for #THIS_CASE)
        # to better find my special place, I will mark this place with ANCHOR!
        simple_xml_values = [
            ['extract_base_params_land', 'details_statement', 'group_top_requisites', 'registration_number'],
            ['extract_base_params_land', 'details_statement', 'group_top_requisites', 'date_formation'],

            ['extract_base_params_land', 'land_record', 'object', 'common_data', 'cad_number'],
            ['extract_base_params_land', 'land_record', 'object', 'common_data', 'quarter_cad_number'],

            ['extract_base_params_land', 'land_record', 'address_location', 'address', 'readable_address'],
            ['extract_base_params_land', 'land_record', 'params', 'area', 'value'],
            ['extract_base_params_land', 'land_record', 'cost', 'value'],

            ['extract_base_params_land', 'land_record', 'params', 'category', 'type', 'value'],
            ['extract_base_params_land', 'land_record', 'params', 'permitted_use', 'permitted_use_established', 'land_use', 'value'],
            ['extract_base_params_land', 'status'],
            ['extract_base_params_land', 'land_record', 'special_notes'],

        ]

        for value_id, value in enumerate(simple_xml_values):
            self.xml_value_table.append(tm._try_get(self.xml_nested_dict, value))

        # PHASE 2 - now, we have all The Data we need! Now it's time to find our data in Xml_table and push it
        # to Excel_table.
        # Simple case:  we pushing one xml_value to one excel_column
        # Complex case: we pushing multiple xml_values to one excel_column.
        # * And some other columns can push the same data too!

        self.excel_table_range = range(1, self.COL_MAX_NUM + 1)
        self.excel_table = [None for i in self.excel_table_range]

        # xml -> excel relations
        # one to one OR one two many
        self.excel_table[0] = os.path.split(self.filename)[-1]

        # simple excel fields
        simple_excel__column_destination = [2, 3,  6, 7,  9, 10, 11,  13, 14, 15, 16]
        for i, excel_id in enumerate(simple_excel__column_destination):
            self.excel_table[excel_id] = self.xml_value_table[i + ANCHOR0]

        return self.excel_table

    def __getitem__(self, i):
        return self.excel_table[i]


if __name__ == '__main__':
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\земельные_участки",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "ZU.xlsx",
        "caps": [
            'Наименование файла',#1
            'Номер выписки',#2
            'Дата выписки',#3
            'Вид объекта недвижимости',#4
            'Дата присвоения кадастрового номера',#5
            'Кадастровый номер',#6
            'Кадастровый квартал',#7
            'Ранее присвоенный государственный учетный номер',#8
            'Адрес',#9
            'Площадь',#10
            'Кадастровая стоимость',#11
            'Кадастровые номера расположенных в пределах земельного участка объектов недвижимости',#12
            'Категория земель',#13
            'Виды разрешенного использования',#14
            'Статус записи об объекте недвижимости',#15
            'Особые отметки',#16
            'Правообладатель (правообладатели)',#17
            'Вид, номер и дата государственной регистрации права',#18
            'Документы-основания',#19
            'Ограничение прав и обременение объекта недвижимости',#20
        ],
    }
    converter = XmlConverterFabric(config, PomeshhenijaRow)
    converter.run()

