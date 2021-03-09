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
            ['extract_base_params_construction', 'details_statement', 'group_top_requisites', 'registration_number'],
            ['extract_base_params_construction', 'details_statement', 'group_top_requisites', 'date_formation'],
            ['extract_base_params_construction', 'construction_record', 'object', 'common_data', 'cad_number'],
            ['extract_base_params_construction', 'construction_record', 'object', 'common_data', 'quarter_cad_number'],

            ['extract_base_params_construction', 'construction_record', 'address_location', 'address', 'readable_address'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'area'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'built_up_area'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'extension'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'depth'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'occurence_depth'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'volume'],
            ['extract_base_params_construction', 'construction_record', 'params', 'base_parameters', 'base_parameter', 'height'],
            ['extract_base_params_construction', 'construction_record', 'params', 'name'],
            ['extract_base_params_construction', 'construction_record', 'params', 'purpose'],
            ['extract_base_params_construction', 'construction_record', 'params', 'floors'],
            ['extract_base_params_construction', 'construction_record', 'params', 'year_commisioning'],
            ['extract_base_params_construction', 'construction_record', 'params', 'year_built'],
            ['extract_base_params_construction', 'construction_record', 'cost', 'value'],

            ['extract_base_params_construction', 'status'],
            ['extract_base_params_construction', 'construction_record', 'special_notes'],
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
        simple_excel__column_destination = [2, 3, 4, 5,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,  26, 27]
        for i, excel_id in enumerate(simple_excel__column_destination):
            self.excel_table[excel_id] = self.xml_value_table[i + ANCHOR0]

        return self.excel_table

    def __getitem__(self, i):
        return self.excel_table[i]


if __name__ == '__main__':
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\сооружения\\xml_сооружения_29.12.2020",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "Sooruzhenija.xlsx",
        "caps": [
            'Наименование файла', # 1
            'Номер выписки', # 2
            'Дата выписки', # 3
            'Кадастровый номер', # 4
            'Кадастровый квартал', # 5
            'Вид объекта недвижимости', # 6
            'Дата присвоения кадастрового номера', # 7
            'Ранее присвоенный государственный учетный номер', # 8
            'Адрес', # 9
            'Основная характеристика сооружения # Площадь в кв.метрах', # 10
            'Основная характеристика сооружения # Площадь застройки в квадратных метрах с округлением до 0,1 квадратного метра ', # 11
            'Основная характеристика сооружения # Протяженность в метрах с округлением до 1 метра', # 12
            'Основная характеристика сооружения # Глубина в метрах с округлением до 0,1 метра', # 13
            'Основная характеристика сооружения # Глубина залегания в метрах с округлением до 0,1 метра', # 14
            'Основная характеристика сооружения # Объем в кубических метрах с округлением до 1 кубического метра', # 15
            'Основная характеристика сооружения # Высота в метрах с округлением до 0,1 метра', # 16
            'Наименование', # 17
            'Назначение сооружения', # 18
            'Количество этажей, в том числе подземных этажей', # 19
            'Год ввода в эксплуатацию по завершении строительства', # 20
            'Год завершения строительства', # 21
            'Кадастровая стоимость', # 22
            'Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости', # 23
            'Кадастровые номера помещений, машино-мест, расположенных в здании или сооружении', # 24
            'Виды разрешенного использования',# 25
            'Статус записи об объекте недвижимости',# 26
            'Особые отметки', # 27
            'Сведения о праве и правообладателях', # 28
            'Сведения о праве (бесхозяйное имущество)', # 29
        ],
    }
    converter = XmlConverterFabric(config, PomeshhenijaRow)
    converter.run()

