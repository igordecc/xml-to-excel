import xmltodict

ru_analog = {}

def main(file_path):
    with open(file_path, encoding='utf-8') as file:
        xml_dict = xmltodict.parse(file.read())

        ru_analog['extract_base_params_construction'] = "Выписка об основных характеристиках и зарегистрированных правах на объект недвижимости (сооружение). "

        ru_analog['details_statement'] = "Реквизиты выписки"
        ru_analog['details_request'] = "Реквизиты поступившего запроса"
        ru_analog['construction_record'] = "Сведения об объекте недвижимости - сооружении"
        ru_analog['room_records'] = "Местоположение помещений в объекте недвижимости (план(ы) расположения помещения)"
        ru_analog['car_parking_space_records'] = "Местоположение машиномест в объекте недвижимости (план(ы) расположения машиноместа)"
        ru_analog['right_records'] = "Сведения о правах и правообладателях"
        ru_analog['restrict_records'] = "Ограничение прав и обременение объекта недвижимости"
        ru_analog['ownerless_right_record'] = "Сведения о праве (бесхозяйное имущество)"
        ru_analog['deal_records'] = "Сведения о сделках, совершенных без необходимого в силу закона согласия третьего лица, органа"
        ru_analog['recipient_statement'] = "Получатель выписки"
        ru_analog['status'] = "Статус записи об объекте недвижимости"
        ru_analog['guid'] = "Глобальный уникальный идентификатор документа"

        ru_analog['group_top_requisites'] = "Группа верхних реквизитов"
        ru_analog['group_lower_requisites'] = "Группа нижних реквизитов"

        ru_analog['organ_registr_rights'] = "Полное наименование органа регистрации прав"
        ru_analog['date_formation'] = "Дата формирования выписки"
        ru_analog['registration_number'] = "Регистрационный номер"

        ru_analog['full_name_position'] = "Полное наименование должности"
        ru_analog['initials_surname'] = "Инициалы, фамилия"

        ru_analog['date_received_request'] = "Дата поступившего запроса"
        ru_analog['date_receipt_request_reg_authority_rights'] = "Дата получения запроса органом регистрации прав"

        ru_analog['record_info'] = "Даты государственной регистрации"
        ru_analog['object'] = "Общие сведения об объекте недвижимости"
        ru_analog['cad_links'] = "Сведения об объектах (связь с кадастровыми номерами)"
        ru_analog['params'] = "Характеристики сооружения"
        ru_analog['address_location'] = "Адрес (местоположение)"
        ru_analog['cost'] = "Кадастровая стоимость"
        ru_analog['object_parts'] = "Сведения о частях сооружения"
        ru_analog['contours'] = "Описание местоположения контура сооружения"
        ru_analog['special_notes'] = "Особые отметки"

        ru_analog['registration_date'] = "Дата постановки на учет/ регистрации"
        ru_analog['cancel_date'] = "Дата снятия с учета/регистрации"

        ru_analog['common_data'] = "Общие сведения"

        ru_analog['land_cad_numbers'] = "Кадастровые номера иных объектов недвижимости (земельных участков), в пределах которых расположен объект недвижимости"
        ru_analog['room_cad_numbers'] = "Кадастровые номера помещений, расположенных в объекте недвижимости"
        ru_analog['car_parking_space_cad_numbers'] = "Кадастровые номера машиномест, расположенных в объекте недвижимости"
        ru_analog['old_numbers'] = "Ранее присвоенные номера"

        ru_analog['land_cad_number'] = "Кадастровый номер объекта недвижимости (земельного участка), в пределах которого расположен объект недвижимости"

        ru_analog['room_cad_number'] = "Кадастровый номер помещения, расположенного в объекте недвижимости"

        ru_analog['car_parking_place_cad_number'] = "Кадастровый номер машиноместа, расположенного в объекте недвижимости"

        ru_analog['base_parameters'] = "Основные характеристики"
        ru_analog['floors'] = "Количество этажей (в том числе подземных)"
        ru_analog['underground_floors'] = "Количество подземных этажей"
        ru_analog['purpose'] = "Назначение сооружения"
        ru_analog['name'] = "Наименование сооружения"
        ru_analog['year_built'] = "Год завершения строительства"
        ru_analog['year_commisioning'] = "Год ввода в эксплуатацию по завершении строительства"
        ru_analog['permitted_uses'] = "Вид(ы) разрешенного использования"

        ru_analog['base_parameter'] = "Основная характеристика"

        ru_analog['area'] = "Площадь в кв. метрах"
        ru_analog['built_up_area'] = "Площадь застройки в квадратных метрах с округлением"
        ru_analog['extension'] = "до 0,1 квадратного метра"
        ru_analog['depth'] = "Протяженность в метрах с округлением до 1 метра"
        ru_analog['occurence_depth'] = "Глубина в метрах с округлением до 0,1 метра"
        ru_analog['volume'] = "Глубина залегания в метрах с округлением до 0,1 метра"
        ru_analog['height'] = "Объем в кубических метрах с округлением до 1 кубического метра"

        ru_analog['value'] = "Стоимость (руб.)"

        ru_analog['object_part'] = "Сведения о части объекта недвижимости"

        ru_analog['part_number'] = "Порядковый номер части"
        ru_analog['content_restrictions'] = "Содержание ограничений"

        ru_analog['data_registration'] = "Сведения о регистрации"
        ru_analog['reg_numb_border'] = "Реестровый номер границы"

        ru_analog['reg_number'] = "Номер"

        ru_analog['cad_number'] = "Кадастровый номер"
        ru_analog['quarter_cad_number'] = "Номер кадастрового квартала"
        ru_analog['type'] = "Вид объекта недвижимости"

        ru_analog['number'] = "Кадастровый номер"

        ru_analog['old_number'] = "Ранее присвоенный номер"
        ru_analog['number_type'] = "Вид номера"
        ru_analog['number'] = "Номер"
        ru_analog['assignment_date'] = "Дата присвоения"
        ru_analog['assigner'] = "Организация, присвоившая номер"

        ru_analog['permitted_use'] = "Вид разрешенного использования"

        ru_analog['name'] = "Наименование вида использования"
        ru_analog['code'] = "Код справочника НСИ"
        ru_analog['value'] = "Текстовое значение, соответствующее коду справочника НСИ"

        ru_analog['restriction_encumbrance_number'] = "Номер регистрации/реестровой записи"
        ru_analog['registration_date'] = "Дата регистрации"

        ru_analog['number'] = "Номер реестровой записи"
        ru_analog['right_number'] = "Номер регистрации ограничения права или обременения ОН"

        ru_analog[''] = ""
        ru_analog[''] = ""


