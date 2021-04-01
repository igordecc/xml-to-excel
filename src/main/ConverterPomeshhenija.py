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
            ['extract_base_params_room', 'details_statement', 'group_top_requisites', 'registration_number'],
            ['extract_base_params_room', 'details_statement', 'group_top_requisites', 'date_formation'],

            ['extract_base_params_room', 'room_record', 'record_info', 'registration_date'],
            ['extract_base_params_room', 'room_record', 'object', 'common_data', 'cad_number'],
            ['extract_base_params_room', 'room_record', 'object', 'common_data', 'quarter_cad_number'],

            ['extract_base_params_room', 'room_record', 'address_room', 'address', 'address', 'readable_address'],
            ['extract_base_params_room', 'room_record', 'params', 'area'],
            ['extract_base_params_room', 'room_record', 'params', 'purpose', 'value'],
            ['extract_base_params_room', 'room_record', 'params', 'name'],
            ['extract_base_params_room', 'room_record', 'location_in_build', 'level', 'floor'],
            ['extract_base_params_room', 'room_record', 'params', 'type', 'value'],
            ['extract_base_params_room', 'room_record', 'cost', 'value'],

            ['extract_base_params_room', 'room_record', 'params', 'permitted_uses', 'permitted_use', 'value'],
            ['extract_base_params_room', 'room_record', 'params', 'special_type', 'value'],
            ['extract_base_params_room', 'status'],
            ['extract_base_params_room', 'room_record', 'special_notes'],
        ]

        for value_id, value in enumerate(simple_xml_values):
            self.xml_value_table.append(tm._try_get(self.xml_nested_dict, value))

        # --- 4 == 6
        anchor1 = len(self.xml_value_table)
        self.xml_value_table.append(tm._try_get(self.xml_nested_dict, ['extract_base_params_room', 'room_record',
                                                                       'object', 'common_data', 'type', 'value']))

        # --- 5 == 7
        anchor2 = len(self.xml_value_table)
        dt = tm._try_get(self.xml_nested_dict, ['extract_base_params_room',
                                                'room_record', 'record_info', 'registration_date'])
        if dt:
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z").date()
        self.xml_value_table.append(dt)

        # --- 8 +
        anchor3 = len(self.xml_value_table)
        old_numbers = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                                     root.findall('cad_links/old_numbers')])
        if old_numbers:
            self.xml_value_table.append(old_numbers)
        else:
            self.xml_value_table.append("-")

        # --- 16
        anchor4 = len(self.xml_value_table)
        land_cad_numbers = tm._try_get(self.xml_nested_dict,
                                       ['extract_base_params_room', 'room_record', 'cad_links', 'included_objects',
                                        'included_object']
                                       )
        s12 = lambda s: "".join([str(tm._try_get(s, ["cad_number"])), " ; "])
        self.xml_value_table.append("".join([str(i) for i in tm.iflist(land_cad_numbers, s12)]))

        # --- 21
        anchor5 = len(self.xml_value_table)
        right_holders_name = [[i for i in j.itertext()][0] for j in
                              root.findall('right_records/right_record/right_holders//value')]
        self.xml_value_table.append("; \n".join(right_holders_name))

        # --- 22
        _type = [[i for i in j.itertext()][0] for j in
                 root.findall('right_records/right_record/right_data/right_type/value')]
        right_number = [[i for i in j.itertext()][0] for j in
                        root.findall('right_records/right_record/right_data/right_number')]
        date = [str(datetime.datetime.strptime([i for i in j.itertext()][0], "%Y-%m-%dT%H:%M:%S%z").date()) for j in
                root.findall('right_records/right_record/record_info/registration_date')]
        self.xml_value_table.append("; \n".join([", ".join(el) for i, el in enumerate(zip(_type, right_number, date))]))

        # --- 23
        ud = "; \n".join([", ".join([i for i in j.itertext()]) for j in
                          root.findall('right_records/right_record/underlying_documents/underlying_document')])
        if ud:
            self.xml_value_table.append(ud)
        else:
            self.xml_value_table.append("-")

        # --- 24
        rr = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                            root.findall('restrict_records/restrict_record')])
        # rights = tm._try_get(self.xml_nested_dict, ['extract_base_params_room', 'restrict_records'])
        if rr!="":
            self.xml_value_table.append(rr)
        else:
            self.xml_value_table.append("-")

        # --- 25
        _expropriation_info_type = [[i for i in j.itertext()][0] for j in
                 root.findall('expropriation_info/expropriation_info_type')]
        _origin_content = [[i for i in j.itertext()][0] for j in
                        root.findall('expropriation_info/origin_content')]

        self.xml_value_table.append("; \n".join([", ".join(el) for i, el in enumerate(zip(_expropriation_info_type,
                                                                                          _origin_content))]))

        # --- 26
        rr = "; \n\n".join([", ".join([str(i).strip() for i in j.itertext() if str(i).strip()]) for j in
                            root.findall('extract_base_params_room/deal_records/deal_record')])
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
        simple_excel__column_destination = [2, 3,   5, 6, 7,   9, 10, 11, 12, 13, 14, 15,   17, 18, 19, 20]
        for i, excel_id in enumerate(simple_excel__column_destination):
            self.excel_table[excel_id - 1] = self.xml_value_table[i + ANCHOR0]

        # anchor1 - field #4
        if self.xml_value_table[anchor1] == "room_record":
            self.excel_table[4 - 1] = "Помещение"
        else:
            self.excel_table[4 - 1] = self.xml_value_table[anchor1]

        # anchor2 - field #5
        self.excel_table[5 - 1] = self.xml_value_table[anchor2]

        # anchor3 - field #8
        self.excel_table[8 - 1] = self.xml_value_table[anchor3]

        # anchor4 - field #16
        self.excel_table[16 - 1] = self.xml_value_table[anchor4]

        # anchor5 - field #21
        self.excel_table[21 - 1] = self.xml_value_table[anchor5]

        # anchor5 - field #22
        self.excel_table[22 - 1] = self.xml_value_table[anchor5 + 1]

        # anchor5 - field #23
        self.excel_table[23 - 1] = self.xml_value_table[anchor5 + 2]

        # anchor5 - field #24
        self.excel_table[24 - 1] = self.xml_value_table[anchor5 + 3]

        # anchor5 - field #25
        self.excel_table[25 - 1] = self.xml_value_table[anchor5 + 4]

        # anchor5 - field #25
        self.excel_table[26 - 1] = self.xml_value_table[anchor5 + 5]

        return self.excel_table

    def __getitem__(self, i):
        return self.excel_table[i]


if __name__ == '__main__':
    def excel_format(writer):
        sheet_setting = writer.sheets["Sheet1"]
        wrap_format = writer.book.add_format({'text_wrap': True})
        wid = 20
        sheet_setting.set_column(0, 7, width=wid, cell_format=wrap_format)
        sheet_setting.set_column(8, 8, width=wid * 3, cell_format=wrap_format)
        sheet_setting.set_column(9, 15, width=wid, cell_format=wrap_format)
        sheet_setting.set_column(16, 25, width=wid * 4, cell_format=wrap_format)
        return writer
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\помещения",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "Pomeshhenija.xlsx",
        "excel_format": excel_format,
        "caps": [
            'Наименование файла',  # 1
            'Номер выписки',  # 2
            'Дата выписки',  # 3
            'Вид объекта недвижимости',  # 4
            'Дата присвоения кадастрового номера',  # 5
            'Кадастровый номер',  # 6
            'Кадастровый квартал',  # 7
            'Ранее присвоенный государственный учетный номер',  # 8
            'Адрес',  # 9
            'Площадь',  # 10
            'Назначение',  # 11
            'Наименование',  # 12
            'Номер этажа, в котором расположено помещение, машино - место',  # 13
            'Вид жилого помещения',  # 14
            'Кадастровая стоимость',  # 15
            'Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости',
            # 16
            'Виды разрешенного использования',  # 17
            'Сведения об отнесении жилого помещения к определенному виду жилых помещений специализированного жилищного фонда, к жилым помещениям наемного дома социального использования или наемного дома коммерческого назначения',
            # 18
            'Статус записи об объекте недвижимости',  # 19
            'Особые отметки',  # 20
            'Правообладатель (правообладатели)',  # 21
            'Вид, номер и дата государственной регистрации права',  # 22
            'Документы-основания',  # 23
            'Ограничение прав и обременение объекта недвижимости',  # 24
            'Сведения о наличии решения об изъятии объекта недвижимости для государственных и муниципальных нужд',
            # 25
            'Сведения об осуществлении государственной регистрации прав без необходимого в силу закона согласия третьего лица, органа',
            # 26
        ],
    }
    converter = XmlConverterFabric(config, PomeshhenijaRow)
    converter.run()

