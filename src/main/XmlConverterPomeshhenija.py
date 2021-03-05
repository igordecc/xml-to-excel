from XmlConverterFabric import XmlConverterFabric
import try_modules as tm

import os, sys
import xmltodict
import pandas
import traceback
import datetime


class Row:
    def __init__(self, name, _len):
        self.filename = name
        self.row = ["" for i in _len] ##??? delete this
        self.script_list = [] ###??? delete this
        try:
            with open(self.filename, encoding="utf8") as opened_file:
                self.xml_nested_dict = xmltodict.parse(opened_file.read())

        except:
            print("Xml file read error: ")
            print(sys.exc_info())

        # PHASE 1 - extract xml Data into xml Table! Keep track of to which excel_column The Data will go ;)

        self.xml_value_table = []


#    def fill_xml__value_table(self):
        simple_excel_column_destination = [2, 3,   5, 6, 7,   9, 10, 11, 12, 13, 14, 15,   18, 19, 20]
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

            ['extract_base_params_room', 'room_record', 'params', 'special_type', 'value'],
            ['extract_base_params_room', 'status'],
            ['extract_base_params_room', 'room_record', 'special_notes'],
        ]

        for value_id in simple_xml_values:
            self.xml_value_table[value_id] = [ simple_excel_column_destination,
                                               tm._try_get(self.xml_nested_dict, simple_xml_values[value_id])
                                               ]


        # PHASE 2 - now, we have all The Data we need! Now it's time to find our data in Xml_table and push it
        # to Excel_table.
        # Simple case:  we pushing one xml_value to one excel_column
        # Complex case: we pushing multiple xml_values to one excel_column.
        # * And some other columns can push the same data too!




        self.xml_value_table.append()



    # there will be TWO type of scripts - xml_values and excel_column scripts!
    # def set_script(self, script_list):
    #     self.script_list.append(*script_list)

    def __call__(self, index, *args, **kwargs):
        return self.script_list[index](*args, **kwargs)

    def __getitem__(self, item):
        return self.row[item]

    def get_row(self):
        return self.row


class Xml_values:
    def __init__(self, query_list: list):
        self.query_list = query_list

    def query_xml_value(self, query):
        pass

class Excel_fields:
    def __init__(self, COL_MAX_NUM):
        self.COL_MAX_NUM = COL_MAX_NUM
        self.field_ids = range(1, self.COL_MAX_NUM + 1)
        self.fields = [[i for i in self.field_ids], ]

    def __add__(self, other):
        self.fields.append(other)

    def query_excel_field(self, query):
        # xml_value_id
        # pass to excel_field_id
        pass






class XmlConverterPomeshhenija(XmlConverterFabric):

    def __init__(self, config: dict, *args, **kwargs):
        super().__init__(self, config, *args, **kwargs)
        # self.config = config

    def main(self):
        
        self.excel_fields = Excel_fields(self.COL_MAX_NUM)
        self.
        
        row1 = Row(self.config["caps"][1], self.COL_MAX_NUM, [tm._try_set()])
        
        with open(filepath, encoding="utf8") as opened_file:
            xml_dict = xmltodict.parse(opened_file.read())
        row1(0, excel_row_with_numerated_columns, column, xml_dict,
                            dict_keys=field_sequence
                            )
        self.excel_fields + row1.get_row() 


    def fill_excel_columns(self):
        """
        Converts all xml file files in self.confg["xml"] directory into one self.confg["excel"] file,
        where 1 row is one xml file
        """
        
        # extract number of excel columns from excel caps
        # df = pandas.DataFrame([[i for i in range(1, COL_NUM + 1)], ],
        #                       columns=self.caps)

        # list will be converted to data frame
        # data frame will be converted to excel
        


        # extracting any xml file in dir to parse
        file_list = [file for file in os.listdir(self.config["xml"]) if ".xml" == os.path.splitext(file)[-1]]

        # creating list of Excel_row objects
        list_of_rows = [Row(file, self.COL_MAX_NUM) for row_i, file in file_list]

        excel_fields = [[i for i in self.ex_range], ]

                excel_fields.append(["" for i in self.ex_range])
                for field_i, field in enumerate(excel_fields):
                    excel_fields[field_i]

                try:
                    print(f"файл № {df.index.max() + 1}")
                    afile = os.path.join(self.config["xml"], file)
                    result = self.get_xml_values(afile)

                    # !!! here execute xml_values to excel_fields script
                    df.loc[df.index.max() + 1] = result
                except:
                    print(f"Ошибка чтения {file} ")
                    print(f"код {sys.exc_info()[0].__dict__}")
                    traceback.print_exc()


        writer = pandas.ExcelWriter(self.confg["excel"])
        df.to_excel(writer, index=False)
        writer.save()

        print("Выполнено")

    @staticmethod
    def get_xml_values(filepath):
        print(filepath)
        excel_row_with_numerated_columns = {}.fromkeys([i for i in range(1, COL_NUM + 1)], "")
        config["excel_fields"] = excel_row_with_numerated_columns
        xml_values = {}
        config["xml_values"] = xml_values


        filename = os.path.split(filepath)[-1]
        excel_row_with_numerated_columns[1] = filename

        with open(filepath, encoding="utf8") as opened_file:
            xml_dict = xmltodict.parse(opened_file.read())

            try_set__columns = [2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20]

            for column in try_set__columns:
                field_sequence = config["fields"][column]
                tm._try_set(excel_row_with_numerated_columns, column, xml_dict,
                            dict_keys=field_sequence
                            )


            # tm._try_change_value_if(excel_row_with_numerated_columns, 4, xml_dict,
            #                         ['extract_base_params_room', 'room_record', 'object', 'common_data', 'type', 'value'],
            #                         if_condition=lambda value: value == "room_record",
            #                         change_value_to="Сооружение",
            #                         )
            #
            # tm._try_date(excel_row_with_numerated_columns, 5, xml_dict,
            #              ['extract_base_params_room', 'room_record', 'record_info', 'registration_date'])
            #
            # # custom queries that may be refactored
            #
            # tm._try_isinstance_of_list(excel_row_with_numerated_columns,
            #                    8,
            #                    xml_dict,
            #                    ['extract_base_params_room', 'room_record', 'cad_links', 'old_numbers', "old_number"],
            #                    tm._try_set,
            #                    do_func=lambda old_number: str(old_number['number_type']['value']) + " " + \
            #                     str(old_number['number']) + " ; ",
            #                    do_func_is_not=lambda old_number: str(old_number['number_type']['value']) + " " + \
            #                     str(old_number['number']) + " ; ",
            #                    )
            #
            #
            # tm._try_isinstance_of_list(excel_row_with_numerated_columns,
            #                    16,
            #                    xml_dict,
            #                    ['extract_base_params_room', 'room_record', 'cad_links', 'land_cad_numbers',
            #                        'land_cad_number'],
            #                    tm._try_set,
            #                    do_func=lambda land_cad_number: land_cad_number['cad_number'] + " ; ",
            #                    do_func_is_not=lambda land_cad_number: land_cad_number['cad_number'] + " ; ",
            #                    )
            #
            # level_16 = tm._try(xml_dict, ['extract_base_params_room', 'room_record', 'cad_links', 'land_cad_numbers',
            #                    'land_cad_number'])
            # if level_16:
            #     excel_row_with_numerated_columns[16] = level_16
            # else:
            #     excel_row_with_numerated_columns[16] = ''
            #
            #
            # try:
            #     land_cad_numbers = xml_dict['extract_base_params_room']['room_record']['cad_links']['land_cad_numbers'][
            #         'land_cad_number']
            #     if isinstance(land_cad_numbers, list):
            #         excel_row_with_numerated_columns[16] = ''
            #         for land_cad_number in land_cad_numbers:
            #             excel_row_with_numerated_columns[16] += land_cad_number['cad_number'] + " ; "
            #     else:
            #         excel_row_with_numerated_columns[16] = land_cad_numbers['cad_number']
            # except:
            #     excel_row_with_numerated_columns[16] = ''
            #
            # try:
            #     print(xml_dict['extract_base_params_room']['room_record']['params']['permitted_uses'])
            #     land_cad_numbers = xml_dict['extract_base_params_room']['room_record']['params']['permitted_uses']
            #     if isinstance(land_cad_numbers, list):  # when there are many entries - its a list
            #         excel_row_with_numerated_columns[17] = ''
            #         for land_cad_number in land_cad_numbers:
            #             excel_row_with_numerated_columns[17] += land_cad_number['permitted_use']['name'] + " ; "
            #     else:  # when there is one entry - its not
            #         excel_row_with_numerated_columns[17] = land_cad_numbers['permitted_use']['name']
            # except:
            #     excel_row_with_numerated_columns[17] = ''
            #
            #
            #
            #
            # # huge queries
            #
            # try:
            #     right_records = xml_dict['extract_base_params_room']['right_records']
            #
            #     def do_records(right_record):
            #
            #         def _prepair_try(_try_set, *args):
            #             def h(fields):
            #                 return _try_set(*args, fields)
            #             return h
            #
            #         _prepair_try(tm._try_set, excel_row_with_numerated_columns, 21, right_record)(['right_record', 'right_holders'])
            #
            #         tm.execute_for_one_or_many(tm._try_set(excel_row_with_numerated_columns, 21, right_record, ['right_record', 'right_holders']))
            #
            #         column_21_nested_dict = tm._try(excel_row_with_numerated_columns,
            #                 right_record,
            #                 ['right_record', 'right_holders']
            #                 )
            #         function_for_excuting_one_or_many = _prepair_try(tm._try_set,
            #                                                 excel_row_with_numerated_columns,
            #                                                 21,
            #                                                 right_record)
            #
            #         tm.execute_for_one_or_many(column_21_nested_dict,
            #                                    )
            #
            #         tm._try_set(excel_row_with_numerated_columns, 21, right_record, ['right_record', 'right_holders'])
            #
            #         # Вид, номер и дата государственной регистрации права
            #         excel_row_with_numerated_columns[22] = "Вид: "
            #         tm._try_append(excel_row_with_numerated_columns, 22, right_record,
            #                        ['right_record', 'right_data', 'right_type', 'value'])  # Вид
            #         excel_row_with_numerated_columns[22] += " ; Номер: "
            #         tm._try_append(excel_row_with_numerated_columns, 22, right_record, ['right_record', 'right_data', 'right_number'])  # Номер
            #         excel_row_with_numerated_columns[22] += " ; Дата регистрации: "
            #         tm._try_date(excel_row_with_numerated_columns, 22, right_record,
            #                      ['right_record', 'record_info', 'registration_date'],
            #                      try_func=tm._try_append)  # Дата регистрации
            #
            #         tm._try_set(excel_row_with_numerated_columns, 23, right_record,
            #                     ['right_record', 'underlying_documents'])  # Документы-основания
            #         tm._try_set(excel_row_with_numerated_columns, 24, xml_dict,
            #                     ['extract_base_params_room', 'right_records', 'right_record',
            #                      'restrict_record'])  # Ограничение прав и обременение объекта недвижимости
            #         tm._try_set(excel_row_with_numerated_columns, 24, xml_dict,
            #                     ['extract_base_params_room', 'right_records', 'right_record', 'restrict_records',
            #                      'restrict_record'])  # Ограничение прав и обременение объекта недвижимости
            #
            #         tm._try_set(excel_row_with_numerated_columns, 25, right_record, ['right_record',
            #                                                   'underlying_documents'])  # Сведения о наличии решения об изъятии объекта недвижимости для государственных и муниципальных нужд
            #         tm._try_set(excel_row_with_numerated_columns, 26, right_record, ['right_record',
            #                                                   'third_party_consents'])  # Сведения об осуществлении государственной регистрации прав без необходимого в силу закона согласия третьего лица, органа
            #
            #     # really common situation of choosing from two
            #     #   one value - xml converts to one item (which is not the element of a list!)
            #     #   two or more - xml converts to the list of multiple records
            #     tm.execute_for_one_or_many(right_records, do_records)
            # except:
            #     pass



        return [excel_row_with_numerated_columns[i] for i in range(1, COL_NUM + 1)]


if __name__ == '__main__':
    converter = XmlConverterPomeshhenija()
    config = {
        "xml": "D:\\PYTHON\\xml-to-excel\\src\\main\\resources\\помещения",
        "excel": "D:\\PYTHON\\xml-to-excel\\",
        "excel_filename": "Pomeshhenija.xlsx",
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
        "fields": [
            [],
            [],
            ['extract_base_params_room', 'details_statement', 'group_top_requisites', 'registration_number'],
            ['extract_base_params_room', 'details_statement', 'group_top_requisites', 'date_formation'],
            [],
            ['extract_base_params_room', 'room_record', 'record_info', 'registration_date'],
            ['extract_base_params_room', 'room_record', 'object', 'common_data', 'cad_number'],
            ['extract_base_params_room', 'room_record', 'object', 'common_data', 'quarter_cad_number'],
            [],
            ['extract_base_params_room', 'room_record', 'address_room', 'address', 'address', 'readable_address'],
            ['extract_base_params_room', 'room_record', 'params', 'area'],
            ['extract_base_params_room', 'room_record', 'params', 'purpose', 'value'],
            ['extract_base_params_room', 'room_record', 'params', 'name'],
            ['extract_base_params_room', 'room_record', 'location_in_build', 'level', 'floor'],
            ['extract_base_params_room', 'room_record', 'params', 'type', 'value'],
            ['extract_base_params_room', 'room_record', 'cost', 'value'],
            [],
            [],
            ['extract_base_params_room', 'room_record', 'params', 'special_type', 'value'],
            ['extract_base_params_room', 'status'],
            ['extract_base_params_room', 'room_record', 'special_notes'],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
    }
    converter.set_config(config)
    converter.run()

