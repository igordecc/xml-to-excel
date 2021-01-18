"""
coppied from zdanija
READY FOR TESTS
TODO ask difference between 10 and 12

contain function to transfer specific info from xml to excel
- for single file - main()
- for directory with files - xml_to_excel()
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

        global COL_NUM
        COL_NUM = len(caps)

        df = pandas.DataFrame([[i for i in range(1, COL_NUM+1)],],
                               columns=caps)
        rcount = 1
        for file in os.listdir(dir_path):
            if ".xml" == os.path.splitext(file)[-1]:
                try:
                    print(f"файл № {rcount}")
                    afile = os.path.join(dir_path, file)
                    df.loc[rcount] = main(afile)
                    rcount += 1
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

    xml_rudoc = {}.fromkeys([i for i in range(1, 27+1)], "")
    xml_rudoc[1] = os.path.split(file_path)[-1]

    with open(file_path, encoding="utf8") as file:
        xml_dict = xmltodict.parse(file.read())
        try:
            xml_rudoc[2] = xml_dict['extract_base_params_under_construction']['details_statement']['group_top_requisites']['registration_number']
        except:
            xml_rudoc[2] = ''
        try:
            xml_rudoc[3] = xml_dict['extract_base_params_under_construction']['details_statement']['group_top_requisites']['date_formation']
        except:
            xml_rudoc[3] = ''
        try:
            value = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['object']['common_data']['type']['value']
            if value == "object_under_construction_record":
                xml_rudoc[4] = "Сооружение"
        except:
            xml_rudoc[4] = ''
        try:
            dt = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['record_info']['registration_date'] # 2012-07-05T00:00:00+04:00
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
            xml_rudoc[5] = str(dt.date())  # Дата присвоения кадастрового номера
            dt = None
        except :
            xml_rudoc[5] = ''
        try:
            xml_rudoc[6] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['object']['common_data']['cad_number']
        except:
            xml_rudoc[6] = ''
        try:
            xml_rudoc[7] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['object']['common_data']['quarter_cad_number']
        except:
            xml_rudoc[7] = ''


        try:
            old_numbers = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['cad_links']['old_numbers']["old_number"]
            if isinstance(old_numbers, list):
                xml_rudoc[8] = ''
                for old_number in old_numbers:
                    xml_rudoc[8] += old_number['number_type']['value'] + " " + old_number['number'] +" ; "
            else:
                xml_rudoc[8] = old_numbers['number_type']['value'] + " " + old_numbers['number']  # ранее присвоенный кадастровый номер
        except:
            xml_rudoc[8] = ''
        try:
            xml_rudoc[9] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['address_location']['address']['readable_address']
        except:
            xml_rudoc[9] = ''


        try:
            xml_rudoc[10] = "площадь " + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['area']
        except:
            xml_rudoc[10] = ''
        try:
            xml_rudoc[10] += " ; площадь застройки " + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['built_up_area']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[10] += " ; протяженность " + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['extension']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[10] += " ; глубина " + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['depth']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[10] += " ; глубина залегания" + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['occurence_depth']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[10] += " ; объем" + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['volume']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[10] += " ; высота " + xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['base_parameters']['base_parameter']['height']
        except:
            xml_rudoc[10] += ''
        try:
            xml_rudoc[11] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['degree_readiness']
        except:
            xml_rudoc[11] = ''
        try:
            xml_rudoc[12] = xml_rudoc[10] # TODO ask difference
        except:
            xml_rudoc[12] = ''
        try:
            xml_rudoc[13] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['params']['purpose']
        except:
            xml_rudoc[13] = ''
        try:
            xml_rudoc[14] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['cost']['value']
        except:
            xml_rudoc[14] = ''
        try:
            land_cad_numbers = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['cad_links']['land_cad_numbers']['land_cad_number']
            if isinstance(land_cad_numbers, list):
                xml_rudoc[15] = ''
                for land_cad_number in land_cad_numbers:
                    xml_rudoc[15] += land_cad_number['cad_number'] +" ; "
            else:
                xml_rudoc[15] = land_cad_numbers['cad_number']
        except:
            xml_rudoc[15] = ''
        try:
            xml_rudoc[16] = xml_dict['extract_base_params_under_construction']['status']
        except:
            xml_rudoc[16] = ''
        try:
            xml_rudoc[17] = xml_dict['extract_base_params_under_construction']['object_under_construction_record']['special_notes']
        except:
            xml_rudoc[17] = ''
        try:
            right_records = xml_dict['extract_base_params_under_construction']['right_records']
            if isinstance(right_records, list):
                for right_record in right_records:
                    __try_except_set(xml_rudoc, 18, right_record, ['right_record','right_holders'])

                    # Вид, номер и дата государственной регистрации права
                    __try_except_set(xml_rudoc, 19, right_record, ['right_record','right_data','right_type'])  #Вид
                    __try_except_add(xml_rudoc, 19, right_record, ['right_record','right_data','right_number'])  #Номер
                    __try_except_add(xml_rudoc, 19, right_record, ['right_record','record_info'])  #Дата регистрации

                    __try_except_set(xml_rudoc, 20, right_record, ['right_record','underlying_documents'])  #Документы-основания
                    __try_except_set(xml_rudoc, 21, right_record, ['right_record','restrict_records'])  #Ограничение прав и обременение объекта недвижимости
                    __try_except_set(xml_rudoc, 21, xml_rudoc[21], ['restrict_record'])  #Ограничение прав и обременение объекта недвижимости

                    __try_except_set(xml_rudoc, 22, right_record, ['right_record','underlying_documents'])  #Сведения о наличии решения об изъятии объекта недвижимости для государственных и муниципальных нужд
                    __try_except_set(xml_rudoc, 23, right_record, ['right_record','third_party_consents'])  #Сведения об осуществлении государственной регистрации прав без необходимого в силу закона согласия третьего лица, органа


            # xml_rudoc[28] = str(dict(right_records))   # to not read many other fields - pass them, as they are in xml
        except:
            # xml_rudoc[28] = ''
            pass

        # try:
        #     rights = xml_dict['extract_base_params_under_construction']['ownerless_right_records']
        #     xml_rudoc[29] = str(dict(rights))
        # except:
        #     xml_rudoc[29] = ''

    return [xml_rudoc[i] for i in range(1, COL_NUM)]


def __try_except_set(set_list, key, dict_value, dict_keys):
    try:
        for dict_key in dict_keys:
            dict_value = dict_value.__getitem__(dict_key)
        set_list[key] = dict_value
    except:
        set_list[key] = ''


def __try_except_add(set_list, key, dict_value, dict_keys):
    try:
        for dict_key in dict_keys:
            dict_value = dict_value.__getitem__(dict_key)
        set_list[key] += dict_value
    except:
        set_list[key] += ''


def run(input_dir, output_dir):
    import os.path
    xml_to_excel(input_dir, os.path.join(output_dir, "Выписки_Здания.xlsx"))


if __name__ == '__main__':

    # main(file, "D:\\")
    inputdir = "D:\\PYTHON\\xml-to-excel\\xml"
    outputf = "D:\\PYTHON\\xml-to-excel\\Вывод.xlsx"
    xml_to_excel(inputdir, outputf)
