from XmlConverterFabric import XmlConverterFabric
import try_modules as tm

import os, sys
import xmltodict
import pandas
import traceback
import xml.etree.ElementTree as et
import datetime


class ONSRow:
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
            ['extract_base_params_under_construction', 'details_statement', 'group_top_requisites',
                'registration_number'],
            ['extract_base_params_under_construction', 'details_statement', 'group_top_requisites', 'date_formation'],

            ['extract_base_params_under_construction', 'object_under_construction_record', 'object', 'common_data',
                'cad_number'],
            ['extract_base_params_under_construction', 'object_under_construction_record', 'object', 'common_data',
             'quarter_cad_number'],

            ['extract_base_params_under_construction', 'object_under_construction_record', 'address_location',
                'address', 'readable_address'],

            ['extract_base_params_under_construction', 'object_under_construction_record', 'params',
             'degree_readiness'],

            ['extract_base_params_under_construction', 'object_under_construction_record', 'params', 'purpose'],
            ['extract_base_params_under_construction', 'object_under_construction_record', 'cost', 'value'],

            ['extract_base_params_under_construction', 'status'],
            ['extract_base_params_under_construction', 'object_under_construction_record', 'special_notes'],

            # ['extract_base_params_room', 'room_record', 'special_notes'],
        ]

        for value_id, value in enumerate(simple_xml_values):
            self.xml_value_table.append(tm._try_get(self.xml_nested_dict, value))

        # anchor1 - 4
        anchor1 = len(self.xml_value_table)
        _type = [[i for i in j.itertext()][0] for j in
                 root.findall('object_under_construction_record/object/common_data/type/value')][0]
        if _type=="object_under_construction_record":
            self.xml_value_table.append("ОНС")
        elif not _type:
            self.xml_value_table.append("-")
        else:
            self.xml_value_table.append(_type)

        # 5
        cad_num = [[i for i in j.itertext()][0] for j in
                 root.findall('object_under_construction_record/object/common_data/cad_number')][0]
        self.xml_value_table.append(cad_num)

        # 8
        old_numbers = " , ".join([" ".join(([i for i in j.itertext()])) for j in
                   root.findall("cad_links/old_numbers/old_number")])
        if old_numbers != "":
            self.xml_value_table.append(old_numbers)
        else:
            self.xml_value_table.append("-")

        # 10=12
        anchor2 = len(self.xml_value_table)
        base_params = "params/base_parameters/base_parameter/"
        def get_param(param):
            p = [[i for i in j.itertext()][0] for j in root.findall(f"{base_params}{param}")]
            if p:
                return p[0]
            else:
                return ""

        area = "Площадь в кв. метрах " + get_param("area") + " ; \n"
        built_up_area = "Площадь застройки в квадратных метрах с округлением до 0,1 квадратного метра " \
                        + get_param("built_up_area") + " ; \n"
        extension = "Протяженность в метрах с округлением до 1 метра " + get_param("extension") + " ; \n"
        depth = "Глубина в метрах с округлением до 0,1 метра" + get_param("depth") + " ; \n"
        occurence_depth = "Глубина залегания в метрах с округлением до 0,1 метра " + get_param(
            "occurence_depth") + " ; \n"
        volume = "Объем в кубических метрах с округлением до 1 кубического метра " + get_param("volume") + " ; \n"
        height = "Высота в метрах с округлением до 0,1 метра " + get_param("height") + " ; \n"

        _final = "".join([area, built_up_area, extension, depth, occurence_depth, volume, height])
        if _final != "":
            self.xml_value_table.append(_final)
        else:
            self.xml_value_table.append("-")

        # 11
        degree_readiness = [[i for i in j.itertext()][0] for j in root.findall("params/degree_readiness")]
        if degree_readiness:
            degree_readiness = degree_readiness[0]
        self.xml_value_table.append(str(degree_readiness))

        # 15
        anchor3 = len(self.xml_value_table)
        land_cad_numbers = " , ".join([" ".join([i for i in j.itertext()]) for j in
                                       root.findall("cad_links/land_cad_numbers/land_cad_number/cad_number")])
        if land_cad_numbers != "":
            self.xml_value_table.append(land_cad_numbers)
        else:
            self.xml_value_table.append("-")


        # 17
        anchor4 = len(self.xml_value_table)
        base_params = "params/base_parameters/base_parameter/"
        p = [[i for i in j.itertext()][0] for j in root.findall("object_under_construction_record/special_notes")]
        if p:
            p = p[0]
        else:
            p = "-"
        self.xml_value_table.append(p)

        # 18
        right_holders_name = [[i for i in j.itertext()][0] for j in
                              root.findall('right_records/right_record/right_holders//value')]

        def get_right_holder(root: root):
            e = root.findall('right_records/right_record/right_holders/right_holder/*')

            # for ..
            print(e[0].tag)
            if e[0].tag=="public_formation":
                print()
            elif e[0].tag=="individual":
                ...
            elif e[0].tag=="legal_entity":
                ...
            elif e[0].tag=="another":
                ...

        self.xml_value_table.append("; \n".join(right_holders_name))

        # 19
        _type = [[i for i in j.itertext()][0] for j in
                 root.findall('right_records/right_record/right_data/right_type/value')]
        right_number = [[i for i in j.itertext()][0] for j in
                 root.findall('right_records/right_record/right_data/right_number')]
        date = [str(datetime.datetime.strptime([i for i in j.itertext()][0], "%Y-%m-%dT%H:%M:%S%z").date()) for j in
                root.findall('right_records/right_record/record_info/registration_date')]
        self.xml_value_table.append("; \n".join([", ".join(el) for i, el in enumerate(zip(_type, right_number, date))]))

        # --- 20
        ud = "; \n".join([", ".join([i for i in j.itertext()]) for j in
                          root.findall('right_records/right_record/underlying_documents/underlying_document')])
        if ud:
            self.xml_value_table.append(ud)
        else:
            self.xml_value_table.append("-")

        # --- 21
        rr = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                            root.findall('restrict_records/restrict_record')])
        # rights = tm._try_get(self.xml_nested_dict, ['extract_base_params_under_construction', 'restrict_records'])
        self.xml_value_table.append(rr)

        # --- 22
        _expropriation_info_type = [[i for i in j.itertext()][0] for j in
                                    root.findall('expropriation_info/expropriation_info_type')]
        _origin_content = [[i for i in j.itertext()][0] for j in
                           root.findall('expropriation_info/origin_content')]

        self.xml_value_table.append("; \n".join([", ".join(el) for i, el in enumerate(zip(_expropriation_info_type,
                                                                                          _origin_content))]))

        # --- 23
        rr = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                            root.findall('extract_base_params_under_construction/deal_records/deal_record')])
        # rights = tm._try_get(self.xml_nested_dict, ['extract_base_params_room', 'restrict_records'])
        if rr != "":
            self.xml_value_table.append(rr)
        else:
            self.xml_value_table.append("-")

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
        simple_excel__column_destination = [2, 3,  6, 7,  9,  11,  13, 14,  16, 17]
        for i, excel_id in enumerate(simple_excel__column_destination):
            self.excel_table[excel_id - 1] = self.xml_value_table[i + ANCHOR0]

        self.excel_table[4 - 1] = self.xml_value_table[anchor1]
        self.excel_table[5 - 1] = self.xml_value_table[anchor1 + 1]
        self.excel_table[8 - 1] = self.xml_value_table[anchor1 + 2]
        self.excel_table[12 - 1] = self.xml_value_table[anchor2]    # 10=12
        self.excel_table[11 - 1] = self.xml_value_table[anchor2 + 1]
        self.excel_table[15 - 1] = self.xml_value_table[anchor3]
        self.excel_table[17 - 1] = self.xml_value_table[anchor4]
        self.excel_table[18 - 1] = self.xml_value_table[anchor4+1]
        self.excel_table[19 - 1] = self.xml_value_table[anchor4+2]
        self.excel_table[20 - 1] = self.xml_value_table[anchor4 + 3]
        self.excel_table[21 - 1] = self.xml_value_table[anchor4 + 4]
        self.excel_table[22 - 1] = self.xml_value_table[anchor4 + 5]
        self.excel_table[23 - 1] = self.xml_value_table[anchor4 + 6]

        # self.excel_table[4 - 1] = self.xml_value_table[i + anchor1]


        return self.excel_table

    def __getitem__(self, i):
        return self.excel_table[i]


if __name__ == '__main__':
    def excel_format(writer):
        sheet_setting = writer.sheets["Sheet1"]
        wrap_format = writer.book.add_format({'text_wrap': True})
        wid = 20
        sheet_setting.set_column(0, 22, width=wid, cell_format=wrap_format)
        sheet_setting.set_column(8, 8, width=wid*4, cell_format=wrap_format)
        sheet_setting.set_column(16, 22, width=wid*4, cell_format=wrap_format)
        sheet_setting.set_column(9, 9, width=wid * 2, cell_format=wrap_format)
        sheet_setting.set_column(11, 11, width=wid * 2, cell_format=wrap_format)
        return writer
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\ОНС",
        # "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\сооружения\\xml_сооружения_29.12.2020",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "ONS.xlsx",
        "excel_format": excel_format,
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
            'Основная характеристика(для сооружения)',#10
            'Степень готовности объекта незавершенного строительства, %',#11
            'Основная характеристика объекта незавершенного строитлеьства и её проектируемое значение',#12
            'Проектируемое назначение',#13
            'Кадастровая стоимость',#14
            'Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости',#15
            'Статус записи об объекте недвижимости',#16
            'Особые отметки',#17
            'Правообладатель (правообладатели)',#18
            'Вид, номер и дата государственной регистрации права',#19
            'Документы-основания',#20
            'Ограничение прав и обременение объекта недвижимости',#21
            'Сведения о наличии решения об изъятии объекта недвижимости для государственных и муниципальных нужд',#22
            'Сведения об осуществлении государственной регистрации прав без необходимого в силу закона согласия третьего лица, органа',#23
        ]
    }
    converter = XmlConverterFabric(config, ONSRow)
    converter.run()

