from XmlConverterFabric import XmlConverterFabric
import try_modules as tm

import os, sys
import xmltodict
import pandas
import traceback
import datetime


class XmlConverterPomeshhenija(XmlConverterFabric):
    @staticmethod
    def convert(self, dir_path, output_xlsx):
        """
        Converts all xml file files in dir_path directory into one output_xlsx file,
        where 1 row is one xml file
        """
        if os.path.isdir(dir_path):
            self.caps = self.config["caps"]

            # extract number of excel columns from excel caps
            global COL_NUM
            COL_NUM = len(self.caps)

            # data frame will be converted to excel
            df = pandas.DataFrame([[i for i in range(1, COL_NUM + 1)], ],
                                  columns=self.caps)

            # we looking for any xml file in dir to parse
            for file in os.listdir(dir_path):
                if ".xml" == os.path.splitext(file)[-1]:
                    try:
                        print(f"файл № {df.index.max() + 1}")
                        afile = os.path.join(dir_path, file)
                        result = self.parse_one_xml_file(afile)
                        df.loc[df.index.max() + 1] = result
                    except:
                        print(f"Ошибка чтения {file} ")
                        print(f"код {sys.exc_info()[0].__dict__}")
                        traceback.print_exc()

            writer = pandas.ExcelWriter(output_xlsx)
            df.to_excel(writer, index=False)
            writer.save()

            print("Выполнено")

    @staticmethod
    def parse_one_xml_file(filepath):
        print(filepath)
        excel_row_with_numerated_columns = {}.fromkeys([i for i in range(1, COL_NUM + 1)], "")

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

            tm._try_change(excel_row_with_numerated_columns, 4, xml_dict,
                           ['extract_base_params_room', 'room_record', 'object', 'common_data', 'type', 'value'],
                           if_condition=lambda value: value == "room_record",
                           change_value_to="Сооружение",
                           )

            tm._try_date(excel_row_with_numerated_columns, 5, xml_dict,
                         ['extract_base_params_room', 'room_record', 'record_info', 'registration_date'])



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
        ]
    }
    converter.set_config(config)
    converter.run()

