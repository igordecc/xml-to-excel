import os, sys
import pandas
import xml.etree.ElementTree as ET
import xmltodict
import pandas


def iter_docs(author):
    author_attr = author.attrib
    for doc in author.iter('document'):
        doc_dict = author_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict


def do_all(dir_path, output_xlsx):
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
                'Особые отметки']

        df = pandas.DataFrame([[i for i in range(1, 28)],],
                               columns=caps)
        rcount = 1
        for file in os.listdir(dir_path):
            afile = os.path.join(dir_path, file)
            df.loc[rcount] = main(afile)
            rcount += 1
        writer = pandas.ExcelWriter(output_xlsx)
        df.to_excel(writer, index=False)
        writer.save()


def main(*args, **kwargs):
    file_path = args[0]
    print(file_path)
    # print(folder_path)
    etree = ET.parse(file_path)
    root = etree.getroot()

    # todo выбрать файлы (много)
    xml_dict = {}

    xml_tags = ['registration_number'  # Регистрационный номер
    ,'date_formation'  # Дата формирования выписки
    ,'cad_number'  # Кадастровый номер
    ,'quarter_cad_number'  # Кадастровый квартал
    ,'type'  # Вид объекта недвижимости
    ,'assignment_date'  # Дата присвоения кадастрового номера
    ,'old_number'  # Ранее присвоенный государственный учетный номер
    ,'readable_address'  # Адрес
    # Основная характеристика сооружения # Тип # Значение # Единица измерения
    , 'area'
    , 'built_up_area'
    , 'extension'
    , 'depth'
    , 'occurence_depth'
    , 'volume'
    , 'height'
    # -----
    ,'name'  # Наименование
    ,'purpose'  # назначение сооружения?
    ,'floors'  #  Количество этажей, в том числе подземных этажей
    ,'year_commisioning'  # Год ввода в эксплуатацию по завершении строительства
    ,'year_built'  # Год завершения строительства
    ,'value'  # Кадастровая стоимость
    ,'land_cad_numbers'  # Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости
    ,'room_cad_numbers'  # Кадастровые номера машино-мест расположенных в здании или сооружении
    ,'car_parking_space_cad_numbers'  # Кадастровые номера помещений расположенных в здании или сооружении
    ,'permitted_use'  # Вид разрешённого использования
    ,'status'  # Статус записи об объекте недвижимости
    ,'special_notes']  # "особые отметки" - особые отметки

    xml_dict.update(zip(xml_tags, ['' for i in xml_tags]))
    for i in root.iter():
        xml_dict[i.tag] = i.text.strip() #

    xml_rudoc = {}
    xml_rudoc[1] = os.path.split(file_path)[-1]
    xml_rudoc[2] = xml_dict['registration_number'] # Регистрационный номер
    xml_rudoc[3] = xml_dict['date_formation'] # Дата формирования выписки
    xml_rudoc[4] = xml_dict['cad_number'] # Кадастровый номер
    xml_rudoc[5] = xml_dict['quarter_cad_number'] # Кадастровый квартал
    # xml_rudoc[6] = xml_dict['type'] # Вид объекта недвижимости ### TODO get parent
    xml_rudoc[7] = xml_dict['assignment_date'] # Дата присвоения кадастрового номера
    xml_rudoc[8] = xml_dict['old_number'] # Ранее присвоенный государственный учетный номер
    xml_rudoc[9] = xml_dict['readable_address'] # Адрес
    # base_parameter много значений, пример area-70-кв. метры
    xml_rudoc[10] = xml_dict['area'] # Основная характеристика сооружения # Площадь в кв. метрах
    xml_rudoc[11] = xml_dict['built_up_area'] # Основная характеристика сооружения # Площадь застройки в квадратных метрах с округлением до 0,1 квадратного метра
    xml_rudoc[12] = xml_dict['extension'] # Основная характеристика сооружения # Протяженность в метрах с округлением до 1 метра
    xml_rudoc[13] = xml_dict['depth'] # Основная характеристика сооружения # Глубина в метрах с округлением до 0,1 метра
    xml_rudoc[14] = xml_dict['occurence_depth'] # Основная характеристика сооружения # Глубина залегания в метрах с округлением до 0,1 метра
    xml_rudoc[15] = xml_dict['volume'] # Основная характеристика сооружения # Объем в кубических метрах с округлением до 1 кубического метра
    xml_rudoc[16] = xml_dict['height'] # Основная характеристика сооружения # Высота в метрах с округлением до 0,1 метра
    # xml_rudoc[17] = xml_dict['name'] # Наименование (сооружения?) ### TODO get parent
    xml_rudoc[18] = xml_dict['purpose'] # назначение сооружения?
    xml_rudoc[19] = xml_dict['floors']  # Количество этажей, в том числе подземных этажей
    xml_rudoc[20] = xml_dict['year_commisioning'] # Год ввода в эксплуатацию по завершении строительства
    xml_rudoc[21] = xml_dict['year_built'] # Год завершения строительства
    # xml_rudoc[22]= xml_dict['value'] # Кадастровая стоимость ### TODO get parent
    xml_rudoc[23] = xml_dict['land_cad_numbers'] # Кадастровые номера иных объектов недвижимости, в пределах которых расположен объект недвижимости
    xml_rudoc[24] = str(xml_dict['room_cad_numbers']) # Кадастровые номера машино-мест расположенных в здании или сооружении
    xml_rudoc[24] += " " + str(xml_dict['car_parking_space_cad_numbers']) # Кадастровые номера помещений расположенных в здании или сооружении
    xml_rudoc[25] = xml_dict['permitted_use'] # Вид разрешённого использования
    xml_rudoc[26] = xml_dict['status'] # Статус записи об объекте недвижимости
    xml_rudoc[27] = xml_dict['special_notes'] # "особые отметки" - особые отметки

    with open(file_path, encoding="utf8") as file:
        xml_dict = xmltodict.parse(file.read())
        try:
            xml_rudoc[6] = xml_dict['extract_base_params_construction']['construction_record']['object']['common_data']['type']['value']
        except:
            xml_rudoc[6] = ''
        try:
            xml_rudoc[17] = xml_dict['extract_base_params_construction']['construction_record']['params']['name']
        except:
            xml_rudoc[17] = ''
        try:
            xml_rudoc[22] = xml_dict['extract_base_params_construction']['construction_record']['cost']['value']
        except:
            xml_rudoc[22] = ''

    return [xml_rudoc[i] for i in range(1, 28)]



    # import xlsxwriter
    # workbook = xlsxwriter.Workbook("output.xlsx")
    # sheets = workbook.worksheets()
    # print(sheets)
    # worksheet = workbook.get_worksheet_by_name("Лист 1")
    #
    # merge_format = workbook.add_format({
    #     'bold': 1,
    #     'border': 1,
    #     'align': 'center',
    #     'valign': 'vcenter',
    #     'fg_color': 'yellow'})
    # worksheet.merge_range('A1:A2', 'Merged Cells', merge_format)


if __name__ == '__main__':

    # main(file, "D:\\")
    inputf = "D:\\PYTHON\\xml-to-excel\\xmls"
    outputf = "D:\\PYTHON\\xml-to-excel\\output.xlsx"
    do_all(inputf, outputf)