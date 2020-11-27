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

        ru_analog[''] = ""


