"""
contain function to transfer specific info from xml to excel
- for single file - main()
- for directory with files - do_all()
"""

import os, sys
import pandas
import xml.etree.ElementTree as ET
import xmltodict
import pandas
import datetime
from collections.abc import Iterable
from collections import OrderedDict
import os.path

def xml_to_excel(dir_path, output_xlsx):
    if os.path.isdir(dir_path):
        caps = ['Наименование файла',
                'Номер выписки',
                'Дата выписки',
                'Кадастровый номер',
                'Кадастровый квартал',
                'Вид объекта недвижимости',
                'Дата присвоения кадастрового номера',
                'Ранее присвоенный государственный учетный номер',
                'Адрес',
                'Основная характеристика сооружения # Площадь в кв.метрах',
                'Основная характеристика сооружения # Площадь застройки в квадратных метрах с округлением до 0,1 квадратного метра ',
                'Основная характеристика сооружения # Протяженность в метрах с округлением до 1 метра',
                'Основная характеристика сооружения # Глубина в метрах с округлением до 0,1 метра',
                'Основная характеристика сооружения # Глубина залегания в метрах с округлением до 0,1 метра',
                'Основная характеристика сооружения # Объем в кубических метрах с округлением до 1 кубического метра',
                'Основная характеристика сооружения # Высота в метрах с округлением до 0,1 метра',
                'Наименование',
                'Назначение сооружения',
                'Количество этажей, в том числе подземных этажей',
                'Год ввода в эксплуатацию по завершении строительства',
                'Год завершения строительства',
                'Кадастровая стоимость',
                'Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости',
                'Кадастровые номера помещений, машино-мест, расположенных в здании или сооружении',
                'Виды разрешенного использования',
                'Статус записи об объекте недвижимости',
                'Особые отметки',
                'Сведения о праве и правообладателях',
                'Сведения о праве (бесхозяйное имущество)']

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
    """
    # xml_rudoc[2] = xml_dict['registration_number'] # Регистрационный номер
    # xml_rudoc[3] = xml_dict['date_formation'] # Дата формирования выписки
    # xml_rudoc[4] = xml_dict['cad_number'] # Кадастровый номер
    # xml_rudoc[5] = xml_dict['quarter_cad_number'] # Кадастровый квартал
    # xml_rudoc[6] = xml_dict['type'] # Вид объекта недвижимости ### TODO get parent
    # xml_rudoc[7] = xml_dict['assignment_date'] # Дата присвоения кадастрового номера ### TODO get parent
    # xml_rudoc[8] = xml_dict['old_number'] # Ранее присвоенный государственный учетный номер ### TODO get parent
    # xml_rudoc[9] = xml_dict['readable_address'] # Адрес
    # base_parameter много значений, пример area-70-кв. метры
    # xml_rudoc[10] = xml_dict['area'] # Основная характеристика сооружения # Площадь в кв. метрах
    # xml_rudoc[11] = xml_dict['built_up_area'] # Основная характеристика сооружения # Площадь застройки в квадратных метрах с округлением до 0,1 квадратного метра
    # xml_rudoc[12] = xml_dict['extension'] # Основная характеристика сооружения # Протяженность в метрах с округлением до 1 метра
    # xml_rudoc[13] = xml_dict['depth'] # Основная характеристика сооружения # Глубина в метрах с округлением до 0,1 метра
    # xml_rudoc[14] = xml_dict['occurence_depth'] # Основная характеристика сооружения # Глубина залегания в метрах с округлением до 0,1 метра
    # xml_rudoc[15] = xml_dict['volume'] # Основная характеристика сооружения # Объем в кубических метрах с округлением до 1 кубического метра
    # xml_rudoc[16] = xml_dict['height'] # Основная характеристика сооружения # Высота в метрах с округлением до 0,1 метра
    # xml_rudoc[17] = xml_dict['name'] # Наименование (сооружения?)
    # xml_rudoc[18] = xml_dict['purpose'] # назначение сооружения?
    # xml_rudoc[19] = xml_dict['floors']  # Количество этажей, в том числе подземных этажей
    # xml_rudoc[20] = xml_dict['year_commisioning'] # Год ввода в эксплуатацию по завершении строительства
    # xml_rudoc[21] = xml_dict['year_built'] # Год завершения строительства
    # xml_rudoc[22]= xml_dict['value'] # Кадастровая стоимость ### TODO get parent
    # xml_rudoc[23] = xml_dict['land_cad_numbers'] # Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости
    # xml_rudoc[24] = str(xml_dict['room_cad_numbers']) # Кадастровые номера машино-мест расположенных в здании или сооружении
    # xml_rudoc[24] += " " + str(xml_dict['car_parking_space_cad_numbers']) # Кадастровые номера помещений расположенных в здании или сооружении
    # xml_rudoc[25] = xml_dict['permitted_uses'] # Вид разрешённого использования
    # xml_rudoc[26] = xml_dict['status'] # Статус записи об объекте недвижимости
    # xml_rudoc[27] = xml_dict['special_notes'] # "особые отметки" - особые отметки
    # xml_rudoc[28] = '' #xml_dict['right_record'] # сведенья о правах
    # xml_rudoc[29] = '' #xml_dict['ownerless_right_records'] # Сведения о праве (бесхозяйное имущество)
    # xml_rudoc[28] = xml_dict['record_info'] # "Дата гос регистрации
    # xml_rudoc[29] = xml_dict['right_data'] # "Обшие свеленья о правах
    # xml_rudoc[30] = xml_dict['holders'] # "Сведенья о правообладателях
    # xml_rudoc[31] = xml_dict['underlying_documents'] # "Документы-основания
    # xml_rudoc[32] = xml_dict['third_party_consents'] # "Сведения об осуществлении государственной регистрации сделки, права, ограничения права, совершенных без необходимого в силу закона согласия третьего лица, органа

    :param args:
    :param kwargs:
    :return:
    """
    file_path = args[0]
    print(file_path)

    xml_rudoc = {}.fromkeys([i for i in range(1, 32+1)], "")
    xml_rudoc[1] = os.path.split(file_path)[-1]


    with open(file_path, encoding="utf8") as file:
        xml_dict = xmltodict.parse(file.read())
        try:
            xml_rudoc[2] = xml_dict['extract_base_params_construction']['details_statement']['group_top_requisites']['registration_number']
        except:
            xml_rudoc[2] = ''
        try:
            xml_rudoc[3] = xml_dict['extract_base_params_construction']['details_statement']['group_top_requisites']['date_formation']
        except:
            xml_rudoc[3] = ''
        try:
            xml_rudoc[4] = xml_dict['extract_base_params_construction']['construction_record']['object']['common_data']['cad_number']
        except:
            xml_rudoc[4] = ''
        try:
            xml_rudoc[5] = xml_dict['extract_base_params_construction']['construction_record']['object']['common_data']['quarter_cad_number']
        except:
            xml_rudoc[5] = ''
        try:
            value = xml_dict['extract_base_params_construction']['construction_record']['object']['common_data']['type']['value']
            if value == "construction_record":
                xml_rudoc[6] = "Сооружение"
        except:
            xml_rudoc[6] = ''
        try:
            dt = xml_dict['extract_base_params_construction']['construction_record']['record_info']['registration_date'] # 2012-07-05T00:00:00+04:00
            dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
            xml_rudoc[7] = str(dt.date())  # Дата присвоения кадастрового номера
            dt = None
        except :
            xml_rudoc[7] = ''
        try:
            old_numbers = xml_dict['extract_base_params_construction']['construction_record']['cad_links']['old_numbers']["old_number"]
            if isinstance(old_numbers, list):
                xml_rudoc[8] = ''
                for old_number in old_numbers:
                    xml_rudoc[8] += old_number['number_type']['value'] + " " + old_number['number'] +" ; "
            else:
                xml_rudoc[8] = old_numbers['number_type']['value'] + " " + old_numbers['number']  # ранее присвоенный кадастровый номер
        except:
            xml_rudoc[8] = ''
        try:
            xml_rudoc[9] = xml_dict['extract_base_params_construction']['construction_record']['address_location']['address']['readable_address']
        except:
            xml_rudoc[9] = ''
        try:
            xml_rudoc[10] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['area']
        except:
            xml_rudoc[10] = ''
        try:
            xml_rudoc[11] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['built_up_area']
        except:
            xml_rudoc[11] = ''
        try:
            xml_rudoc[12] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['extension']
        except:
            xml_rudoc[12] = ''
        try:
            xml_rudoc[13] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['depth']
        except:
            xml_rudoc[13] = ''
        try:
            xml_rudoc[14] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['occurence_depth']
        except:
            xml_rudoc[14] = ''
        try:
            xml_rudoc[15] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['volume']
        except:
            xml_rudoc[15] = ''
        try:
            xml_rudoc[16] = xml_dict['extract_base_params_construction']['construction_record']['params']['base_parameters']['base_parameter']['height']
        except:
            xml_rudoc[16] = ''
        try:
            xml_rudoc[17] = xml_dict['extract_base_params_construction']['construction_record']['params']['name']
        except:
            xml_rudoc[17] = ''
        try:
            xml_rudoc[18] = xml_dict['extract_base_params_construction']['construction_record']['params']['purpose']
        except:
            xml_rudoc[18] = ''
        try:
            xml_rudoc[19] = xml_dict['extract_base_params_construction']['construction_record']['params']['floors']
        except:
            xml_rudoc[19] = ''
        try:
            xml_rudoc[20] = xml_dict['extract_base_params_construction']['construction_record']['params']['year_commisioning']
        except:
            xml_rudoc[20] = ''
        try:
            xml_rudoc[21] = xml_dict['extract_base_params_construction']['construction_record']['params']['year_built']
        except:
            xml_rudoc[21] = ''
        try:
            xml_rudoc[22] = xml_dict['extract_base_params_construction']['construction_record']['cost']['value']
        except:
            xml_rudoc[22] = ''
        try:
            land_cad_numbers = xml_dict['extract_base_params_construction']['construction_record']['cad_links']['land_cad_numbers']['land_cad_number']
            if isinstance(land_cad_numbers, list):
                xml_rudoc[23] = ''
                for land_cad_number in land_cad_numbers:
                    xml_rudoc[23] += land_cad_number['cad_number'] +" ; "
            else:
                xml_rudoc[23] = land_cad_numbers['cad_number']
        except:
            xml_rudoc[23] = ''
        try:
            print(xml_dict['extract_base_params_construction']['construction_record']['cad_links']['room_cad_numbers'])
            land_cad_numbers = xml_dict['extract_base_params_construction']['construction_record']['cad_links']['room_cad_numbers']['room_cad_number']
            if isinstance(land_cad_numbers, list):
                xml_rudoc[24] = ''
                for land_cad_number in land_cad_numbers:
                    xml_rudoc[24] += land_cad_number['cad_number'] +" ; "
            else:
                xml_rudoc[24] = land_cad_numbers['cad_number']
        except:
            xml_rudoc[24] = ''
        try:
            land_cad_numbers = xml_dict['extract_base_params_construction']['construction_record']['cad_links']['car_parking_space_cad_numbers']['car_parking_space_cad_number']
            if isinstance(land_cad_numbers, list):
                for land_cad_number in land_cad_numbers:
                    xml_rudoc[24] += land_cad_number['cad_number'] +" ; "
            else:
                xml_rudoc[24] = land_cad_numbers['cad_number']
        except:
            ...     # cause - append this column to the previous

        try:
            print(xml_dict['extract_base_params_construction']['construction_record']['params']['permitted_uses'])
            land_cad_numbers = xml_dict['extract_base_params_construction']['construction_record']['params']['permitted_uses']
            if isinstance(land_cad_numbers, list): # when there are many entries - its a list
                xml_rudoc[25] = ''
                for land_cad_number in land_cad_numbers:
                    xml_rudoc[25] += land_cad_number['permitted_use']['name'] +" ; "
            else:                                  # when there is one entry - its not
                xml_rudoc[25] = land_cad_numbers['permitted_use']['name']
        except:
            xml_rudoc[25] = ''


        try:
            xml_rudoc[26] = xml_dict['extract_base_params_construction']['status']
        except:
            xml_rudoc[26] = ''
        try:
            xml_rudoc[27] = xml_dict['extract_base_params_construction']['construction_record']['special_notes']
        except:
            xml_rudoc[27] = ''
        try:
            rights = xml_dict['extract_base_params_construction']['right_records']
            xml_rudoc[28] = str(dict(rights))   # to not read many other fields - pass them, as they are in xml
        except:
            xml_rudoc[28] = ''

        try:
            rights = xml_dict['extract_base_params_construction']['ownerless_right_records']
            xml_rudoc[29] = str(dict(rights))
        except:
            xml_rudoc[29] = ''

    return [xml_rudoc[i] for i in range(1, COL_NUM+1)]


def run(input_dir, output_dir):
    xml_to_excel(input_dir, os.path.join(output_dir, "Выписки_Сооружения.xlsx"))
    print(os.path.join(output_dir, "Выписки_Сооружения.xlsx"))


if __name__ == '__main__':

    # main(file, "D:\\")
    inputdir = "D:\\PYTHON\\xml-to-excel\\xml_сооружения_29.12.2020"
    outputf = "D:\\PYTHON\\xml-to-excel\\Выписки_Сооружения.xlsx"
    xml_to_excel(inputdir, outputf)
