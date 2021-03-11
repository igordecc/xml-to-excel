from XmlConverterFabric import XmlConverterFabric
import try_modules as tm

import os, sys
import xmltodict
import pandas
import traceback
import datetime
import xml.etree.ElementTree as et


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

        # PHASE 0 - parse etree. enjoy XPath!

        tree = et.parse(self.filename)
        root = tree.getroot()
        root.findall("")

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

        # --- 4 == 6 soor
        anchor1 = len(self.xml_value_table)
        self.xml_value_table.append(tm._try_get(self.xml_nested_dict, ['extract_base_params_land',
                                                                       'land_record', 'object', 'common_data',
                                                                       'type', 'value']))

        # --- 5 == 7 soor
        anchor2 = len(self.xml_value_table)
        dt = tm._try_get(self.xml_nested_dict, ['extract_base_params_land',
                                                'land_record', 'record_info', 'registration_date'])
        if dt:
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z").date()
        self.xml_value_table.append(dt)

        # --- 8
        anchor3 = len(self.xml_value_table)
        old_numbers = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                            root.findall('cad_links/old_numbers')])
        if old_numbers:
            self.xml_value_table.append(old_numbers)
        else:
            self.xml_value_table.append("-")

        # --- 12 == 23 soor
        anchor4 = len(self.xml_value_table)
        land_cad_numbers = tm._try_get(self.xml_nested_dict,
                                       ['extract_base_params_land', 'land_record', 'cad_links', 'included_objects',
                                           'included_object']
                                       )
        s12 = lambda s: "".join([str(tm._try_get(s, ["cad_number"])), " ; "])
        self.xml_value_table.append("".join([str(i) for i in tm.iflist(land_cad_numbers, s12)]))

        # TODO remake into more objects
        # --- 17 == 28 soor
        anchor5 = len(self.xml_value_table)
        right_holders_name = [[i for i in j.itertext()][0] for j in root.findall('right_records/right_record/right_holders//value')]
        self.xml_value_table.append("; \n".join(right_holders_name))

        # --- 18
        _type = [[i for i in j.itertext()][0] for j in
                 root.findall('right_records/right_record/right_data/right_type/value')]
        right_number = [[i for i in j.itertext()][0] for j in
                 root.findall('right_records/right_record/right_data/right_number')]
        date = [str(datetime.datetime.strptime([i for i in j.itertext()][0], "%Y-%m-%dT%H:%M:%S%z").date()) for j in
                root.findall('right_records/right_record/record_info/registration_date')]
        self.xml_value_table.append("; \n".join([", ".join(el) for i, el in enumerate(zip(_type, right_number, date))]))

        # --- 19
        ud = "; \n".join([", ".join([i for i in j.itertext()]) for j in
                 root.findall('right_records/right_record/underlying_documents/underlying_document')])
        if ud:
            self.xml_value_table.append(ud)
        else:
            self.xml_value_table.append("-")

        # --- 20
        rr = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                        root.findall('restrict_records/restrict_record')])
        # rights = tm._try_get(self.xml_nested_dict, ['extract_base_params_land', 'restrict_records'])
        self.xml_value_table.append(rr)
        #

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
            self.excel_table[excel_id - 1] = self.xml_value_table[i + ANCHOR0]

        # anchor1 - field #4
        if self.xml_value_table[anchor1] == "land_record":
            self.excel_table[4 - 1] = "Земельный участок"
        else:
            self.excel_table[4 - 1] = self.xml_value_table[anchor1]

        # anchor2 - field #5
        self.excel_table[5 - 1] = self.xml_value_table[anchor2]

        # anchor3 - field #8
        self.excel_table[8 - 1] = self.xml_value_table[anchor3]

        # anchor4 - field #12
        self.excel_table[12 - 1] = self.xml_value_table[anchor4]

        # anchor5 - field #17
        self.excel_table[17 - 1] = self.xml_value_table[anchor5]

        # ancho6 - field 18
        self.excel_table[18 - 1] = self.xml_value_table[anchor5+1]

        # anchor9 - field #19
        self.excel_table[19 - 1] = self.xml_value_table[anchor5+2]

        # anchor9 - field #20
        self.excel_table[20 - 1] = self.xml_value_table[anchor5+3]

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

