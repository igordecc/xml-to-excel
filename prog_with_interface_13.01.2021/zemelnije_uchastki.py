"""
FINISHED
NOT TESTED

contain function to transfer specific info from xml to excel
- for single file - main()
- for directory with files - do_all()
"""

import os, sys
import xmltodict
import pandas
import datetime


def xml_to_excel(dir_path, output_xlsx): ##
    if os.path.isdir(dir_path):
        caps = [
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
                ]

        global COL_NUM
        COL_NUM = len(caps)

        df = pandas.DataFrame([[i for i in range(1, COL_NUM+1)],],
                               columns=caps)
        for file in os.listdir(dir_path):
            if ".xml" == os.path.splitext(file)[-1]:
                try:
                    print(f"файл № {df.index.max() + 1}")
                    afile = os.path.join(dir_path, file)
                    result = main(afile)
                    df.loc[df.index.max() + 1] = result
                except:
                    print(f"Ошибка чтения {file} ")
                    print(f"код {sys.exc_info()[0].__dict__}")
        writer = pandas.ExcelWriter(output_xlsx)
        df.to_excel(writer, index=False)
        writer.save()

        print("Выполнено")


def main(*args, **kwargs):
    file_path = args[0]
    print(file_path)

    xml_rudoc = {}.fromkeys([i for i in range(1, COL_NUM+1)], "")
    print(len(xml_rudoc.keys()))
    xml_rudoc[1] = os.path.split(file_path)[-1]

    with open(file_path, encoding="utf8") as file:
        xml_dict = xmltodict.parse(file.read())
        try:
            xml_rudoc[2] = xml_dict['extract_base_params_land']['details_statement']['group_top_requisites']['registration_number']
        except:
            xml_rudoc[2] = ''
        try:
            xml_rudoc[3] = xml_dict['extract_base_params_land']['details_statement']['group_top_requisites']['date_formation']
        except:
            xml_rudoc[3] = ''
        try:
            value = xml_dict['extract_base_params_land']['land_record']['object']['common_data']['type']['value']
            if value == "land_record":
                xml_rudoc[4] = "Сооружение"
        except:
            xml_rudoc[4] = ''
        try:
            dt = xml_dict['extract_base_params_land']['land_record']['record_info']['registration_date'] # 2012-07-05T00:00:00+04:00
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
            xml_rudoc[5] = str(dt.date())  # Дата присвоения кадастрового номера
            dt = None
        except :
            xml_rudoc[5] = ''
        try:
            xml_rudoc[6] = xml_dict['extract_base_params_land']['land_record']['object']['common_data']['cad_number']
        except:
            xml_rudoc[6] = ''
        try:
            xml_rudoc[7] = xml_dict['extract_base_params_land']['land_record']['object']['common_data']['quarter_cad_number']
        except:
            xml_rudoc[7] = ''
        try:
            old_numbers = xml_dict['extract_base_params_land']['land_record']['cad_links']['old_numbers']["old_number"]
            if isinstance(old_numbers, list):
                xml_rudoc[8] = ''
                for old_number in old_numbers:
                    xml_rudoc[8] += old_number['number_type']['value'] + " " + old_number['number'] +" ; "
            else:
                xml_rudoc[8] = old_numbers['number_type']['value'] + " " + old_numbers['number']  # ранее присвоенный кадастровый номер
        except:
            xml_rudoc[8] = ''
        try:
            xml_rudoc[9] = xml_dict['extract_base_params_land']['land_record']['address_location']['address']['readable_address']
        except:
            xml_rudoc[9] = ''
        try:
            xml_rudoc[10] = xml_dict['extract_base_params_land']['land_record']['params']['area']['value']
        except:
            xml_rudoc[10] = ''
        try:
            xml_rudoc[11] = xml_dict['extract_base_params_land']['land_record']['cost']['value']
        except:
            xml_rudoc[11] = ''
        try:
            land_cad_numbers = xml_dict['extract_base_params_land']['land_record']['cad_links']['included_objects']['included_object']
            xml_rudoc[12] = __read_obj_or_list(land_cad_numbers, ['cad_number',])
        except:
            xml_rudoc[12] = ''
        try:
            xml_rudoc[13] = xml_dict['extract_base_params_land']['land_record']['params']['category']['type']['value']
        except:
            xml_rudoc[13] = ''
        # try:
        #     # print(xml_dict['extract_base_params_land']['land_record']['params']['permitted_uses'])
        #     land_cad_numbers = xml_dict['extract_base_params_land']['land_record']['params']['permitted_uses']
        #     if isinstance(land_cad_numbers, list): # when there are many entries - its a list
        #         xml_rudoc[14] = ''
        #         for land_cad_number in land_cad_numbers:
        #             xml_rudoc[14] += land_cad_number['permitted_use']['name'] +" ; "
        #     else:                                  # when there is one entry - its not
        #         xml_rudoc[14] = land_cad_numbers['permitted_use']['name']
        # except:
        #     xml_rudoc[14] = ''

        # try:
        #     xml_rudoc[14] += xml_dict['extract_base_params_land']['land_record']['params']['permitted_use']['permitted_use_established']['by_document']
        # except:
        #     xml_rudoc[14] = ''
        try:
            xml_rudoc[14] = xml_dict['extract_base_params_land']['land_record']['params']['permitted_use']['permitted_use_established']['land_use']['value']
        except:
            xml_rudoc[14] = ''
        try:
            xml_rudoc[15] = xml_dict['extract_base_params_land']['status']
        except:
            xml_rudoc[15] = ''
        try:
            xml_rudoc[16] = xml_dict['extract_base_params_land']['land_record']['special_notes']
        except:
            xml_rudoc[16] = ''
        try:
            right_records = xml_dict['extract_base_params_land']['right_records']
            # TODO print isinstance
            def do_records(right_record):
                __try_except_set(xml_rudoc, 17, right_record, ['right_record', 'right_holders'])

                # Вид, номер и дата государственной регистрации права
                xml_rudoc[18] = "Вид: "
                __try_except_add(xml_rudoc, 18, right_record, ['right_record', 'right_data', 'right_type', 'value'])  # Вид
                xml_rudoc[18] += " ; Номер: "
                __try_except_add(xml_rudoc, 18, right_record, ['right_record', 'right_data', 'right_number'])  # Номер
                xml_rudoc[18] += " ; Дата регистрации: "
                __try_except_add(xml_rudoc, 18, right_record, ['right_record', 'record_info','registration_date'])  # Дата регистрации

            if isinstance(right_records, list):
                for right_record in right_records:
                    do_records(right_record)
            else:
                do_records(right_records)
        except:
            xml_rudoc[18] = ''

        # try:
        #     right_records = xml_dict['extract_base_params_land']['restrict_records']
        #
        #     # TODO print isinstance
        #     def do_records(right_record):
        #         __try_except_set(xml_rudoc, 17, right_record, ['right_record', 'right_holders'])
        #
        #         # Вид, номер и дата государственной регистрации права
        #         xml_rudoc[19] = "Дата государственной регистрации: "
        #         __try_except_add(xml_rudoc, 18, right_record,
        #                          ['right_record', 'right_data', 'right_type', 'value'])  # Вид
        #         xml_rudoc[18] += " ; Номер: "
        #         __try_except_add(xml_rudoc, 18, right_record,
        #                          ['right_record', 'right_data', 'right_number'])  # Номер
        #         xml_rudoc[18] += " ; Дата регистрации: "
        #         __try_except_add(xml_rudoc, 18, right_record,
        #                          ['right_record', 'record_info', 'registration_date'])  # Дата регистрации
        #
        #     if isinstance(right_records, list):
        #         for right_record in right_records:
        #             do_records(right_record)
        #     else:
        #         do_records(right_records)
        # except:
        #     xml_rudoc[18] = ''


            # xml_rudoc[28] = ''
        try:
            temp_dict = __try_except_set(None, None, xml_dict, ['extract_base_params_land', 'restrict_records', 'restrict_record'])  # Ограничение прав и обременение объекта недвижимости
            desc = [
                'Дата государственной регистрации',
                'Общие сведения об ограничениях и обременениях',
                'Сведения о лицах, в пользу которых установлены ограничения права и обременения объекта недвижимости',
                'Документы-основания',
                'Сведения об осуществлении государственной регистрации сделки, права, ограничения права, совершенных без необходимого в силу закона согласия третьего лица, органа',
            ]
            fields = [
                ['record_info', 'registration_date'],
                ['restrictions_encumbrances_data',],
                ['restrict_parties', 'restricted_rights_parties', 'restricted_rights_party'],
                ['-',],
                ['third_party_consents',],
            ]
            some = __read_obj_or_list_manytimes(temp_dict, desc, fields)
            xml_rudoc[20] = some
            # __try_except_set(xml_rudoc, 20, xml_rudoc[20],
            #                  ['restrict_record'])  # Ограничение прав и обременение объекта недвижимости
        except:
            xml_rudoc[20] = ''
        try:
            restrict_records = xml_dict['extract_base_params_land']['restrict_records']
            def do_restrict_records(restrict_record):
                temp_dict = {}
                __try_except_set(temp_dict, 19, restrict_record,
                                 ['restrict_record', 'underlying_documents'])  # Документы-основания
                desc = [
                    'Код документа',
                    'Наименование',
                    'Серия документа',
                    'Номер документа',
                    'Дата документа',
                    'Орган власти, организация, выдавшие документ',
                ]
                fields = [
                    ['document_code', ],
                    ['document_name', ],
                    ['document_series', ],
                    ['document_number', ],
                    ['document_date', ],
                    ['document_issuer', ],
                ]
                xml_rudoc[19] = __read_obj_or_list_manytimes(temp_dict, desc, fields)
            if isinstance(restrict_records, list):
                for restrict_record in restrict_records:
                    do_restrict_records(restrict_record)
            else:
                do_restrict_records(right_records)
        except:
            xml_rudoc[19] = ''

        # try:
        #     rights = xml_dict['extract_base_params_land']['ownerless_right_records']
        #     xml_rudoc[29] = str(dict(rights))
        # except:
        #     xml_rudoc[29] = ''

    return [xml_rudoc[i] for i in range(1, COL_NUM+1)]


def __try_except_set(set_list, key, dict_value, dict_keys):
    try:
        for dict_key in dict_keys:
            dict_value = dict_value.__getitem__(dict_key)
        if set_list:
            set_list[key] = dict_value
        return dict_value
    except:
        if set_list:
            set_list[key] = ''
        return ''


def __try_except_add(set_list, key, dict_value, dict_keys):
    try:
        for dict_key in dict_keys:
            dict_value = dict_value.__getitem__(dict_key)
        if set_list:
            set_list[key] += dict_value
        return dict_value
    except:
        if set_list:
            set_list[key] += ''
        return ''


def __read_obj_or_list(obj_or_list, fields:list):
    if isinstance(obj_or_list, list):
        _string = ''
        for obj in obj_or_list:
            _string += str(__try_except_set(None, None, obj, fields)) + " ; "
        return
    else:
        return __try_except_set(None, None, obj_or_list, fields)


def __read_obj_or_list_manytimes(obj_or_list, description:list, fields_obj_or_list):
    if isinstance(obj_or_list, list):
        _string = ''
        for i, obj in enumerate(obj_or_list):
            _string += description[i] + ": "
            _string += str(__try_except_set(None, None, obj, fields_obj_or_list[i])) + " ; "
        return _string
    else:
        return __try_except_set(None, None, obj_or_list, fields_obj_or_list)


def run(input_dir, output_dir):
    import os.path
    xml_to_excel(input_dir, os.path.join(output_dir, "Выписки_ЗУ.xlsx"))


if __name__ == '__main__':

    # main(file, "D:\\")
    inputdir = "C:\\Users\\DesyatovIV\\Desktop\\ЗУ"
    outputf = "C:\\Users\\DesyatovIV\\Desktop\\ЗУ"
    run(inputdir, outputf)
