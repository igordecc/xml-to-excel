import xmltodict
import os

def main(*args):
    file_path = args[0]
    folder_path = args[1]
    # print(folder_path)
    with open(file_path, encoding="utf8") as file:
        xml_dict = xmltodict.parse(file.read())
        xml_rudoc = {}
        xml_rudoc[1] = os.path.split(file_path)[-1] # имя файла
        gtr = xml_dict['extract_base_params_construction']['details_statement']['group_top_requisites']
        xml_rudoc[2] = gtr['registration_number'] # Регистрационный номер
        xml_rudoc[3] = gtr['date_formation'] # Дата формирования выписки
        xml_rudoc[4] = xml_dict['cad_number']  # Кадастровый номер
        xml_rudoc[5] = xml_dict['quarter_cad_number']  # Кадастровый квартал
        xml_rudoc[6] = xml_dict['type']  # Вид объекта недвижимости ### TODO get parent
        xml_rudoc[7] = xml_dict['assignment_date']  # Дата присвоения кадастрового номера
        xml_rudoc[8] = xml_dict['old_number']  # Ранее присвоенный государственный учетный номер
        xml_rudoc[9] = xml_dict['readable_address']  # Адрес
        # base_parameter много значений, пример area-70-кв. метры
        # xml_rudoc[10] = xml_dict[''] # Основная характеристика сооружения # Тип
        # xml_rudoc[11] = xml_dict[''] # Основная характеристика сооружения # Значение
        # xml_rudoc[12] = xml_dict[''] # Основная характеристика сооружения # Единица измерения
        xml_rudoc[13] = xml_dict['name']  # Наименование ### TODO get parent
        xml_rudoc[14] = xml_dict['purpose']  # назначение сооружения?
        xml_rudoc[15] = xml_dict['year_built']  # Год ввода в эксплуатацию по завершении строительства
        xml_rudoc[16] = xml_dict['year_commisioning']  # Год ввода в эксплуатацию по завершении строительства
        xml_rudoc[17] = xml_dict['year_built']  # Год завершения строительства
        xml_rudoc[18] = xml_dict['value']  # Кадастровая стоимость ### TODO get parent
        xml_rudoc[19] = xml_dict[
            'land_cad_numbers']  # Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости
        xml_rudoc[20] = str(
            xml_dict['room_cad_numbers'])  # Кадастровые номера машино-мест расположенных в здании или сооружении
        xml_rudoc[20] += " " + str(xml_dict[
                                       'car_parking_space_cad_numbers'])  # Кадастровые номера помещений расположенных в здании или сооружении
        xml_rudoc[21] = xml_dict['permitted_use']  # Вид разрешённого использования
        xml_rudoc[22] = xml_dict['status']  # Статус записи об объекте недвижимости
        xml_rudoc[23] = xml_dict['special_notes']  # "особые отметки" - особые отметки

    print(xml_dict)



if __name__ == '__main__':
    file = "D:\\PYTHON\\xml-to-excel\\report3.xml"
    main(file, "D:\\")