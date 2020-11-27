import xmltodict
import xml

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

        ru_analog['right_record'] = "Сведения о праве и правообладателях"

        ru_analog['record_info'] = "Дата государственной регистрации"
        ru_analog['right_data'] = "Общие сведения о правах"
        ru_analog['right_holders'] = "Сведения о правообладателях"

        ru_analog['underlying_documents'] = "Документы-основания"
        ru_analog['third_party_consents'] = "Сведения об осуществлении государственной регистрации сделки, права, ограничения права, совершенных без необходимого в силу закона согласия третьего лица, органа"

        ru_analog['right_type'] = "Вид зарегистрированного вещного права"
        ru_analog['right_number'] = "Номер регистрации вещного права"
        ru_analog['shares'] = "Размер доли в праве"
        ru_analog['share_description'] = "Описание доли текстом"
        ru_analog['reinstatement'] = "Восстановление права на основании судебного акта"

        ru_analog['share'] = "Размер доли в праве"
        ru_analog['share_bal_hectare'] = "Размер доли в праве в баллогектарах"
        ru_analog['share_hectare'] = "Размер доли в праве в гектарах"
        ru_analog['share_unknown'] = "Не указан размер доли в праве общей долевой собственности на общее имущество, в том числе на земельный участок, собственников помещений, машиномест в здании, если объектом недвижимости является помещение, машиноместо в здании"
        ru_analog['room_owners_share'] = "Размер доли в праве общей долевой собственности на общее имущество собственников комнат в жилом помещении"
        ru_analog['builder_share'] = "Доля в праве общей долевой собственности пропорциональна размеру общей площади помещений, машиномест, не переданных участникам долевого строительства"
        ru_analog['builder_share_with_object'] = "Доля в праве общей долевой собственности пропорциональна размеру общей площади помещений, машиномест, не переданных участникам долевого строительства, а также помещений, машиномест"

        ru_analog['numerator'] = "Числитель"
        ru_analog['denominator'] = "Знаменатель"

        ru_analog['bal_hectare'] = "Баллогектары"

        ru_analog['hectare'] = "Гектары"

        ru_analog['share_description'] = "Описание размера доли"
        ru_analog['proportion_cad_number'] = "Кадастровый номер для расчета пропорций"

        ru_analog['room_owners_share_info'] = "Размер доли в праве общей долевой собственности на общее имущество собственников комнат в жилом помещении"

        ru_analog['builder_share_info'] = "Доля в праве общей долевой собственности пропорциональна размеру общей площади помещений, машиномест, не переданных участникам долевого строительства"

        ru_analog['builder_share_with_object_info'] = "Доля в праве общей долевой собственности пропорциональна размеру общей площади помещений, машиномест, не переданных участникам долевого строительства, а также помещений, машиномест"
        ru_analog['info_objects'] = "Сведения о помещениях, машиноместах"

        ru_analog['info_object'] = "Сведения о помещении, машиноместе"

        ru_analog['prev_registration_date'] = "Дата ранее произведенной государственной регистрации права"

        ru_analog['restrict_record'] = "Ограничение права и обременение объекта недвижимости"

        ru_analog['record_info'] = "Дата государственной регистрации"
        ru_analog['restrictions_encumbrances_data'] = "Общие сведения об ограничениях и обременениях"
        ru_analog['restrict_parties'] = " Сведения о лицах, в пользу которых установлены ограничения права и обременения объекта недвижимости"
        ru_analog['underlying_documents'] = "Документы-основания"
        ru_analog['third_party_consents'] = "Сведения об осуществлении государственной регистрации сделки, права, ограничения права, совершенных без необходимого в силу закона согласия третьего лица, органа"
        ru_analog['state_expropriation'] = "Изъятие для государственных или муниципальных нужд"

        ru_analog['restriction_encumbrance_number'] = "Номер регистрации ограничения права или обременения объекта недвижимости"
        ru_analog['restriction_encumbrance_type'] = "Вид зарегистрированного ограничения права или обременения объекта недвижимости"
        ru_analog['period'] = "Срок, на который установлено ограничение прав и обременение объекта недвижимости"
        ru_analog['additional_encumbrance_info'] = "Дополнительная информация в зависимости от вида зарегистрированного ограничения права или обременения объекта недвижимости"
        ru_analog['restricting_rights'] = "Ограничиваемые права"

        ru_analog['period_info'] = "Срок, на который установлено ограничение права и обременение объекта недвижимости"

        ru_analog['start_date'] = "Дата начала действия"
        ru_analog['end_date'] = "Дата прекращения действия"
        ru_analog['deal_validity_time'] = "Срок действия ограничения/обременения (Продолжительность)"

        ru_analog['servitude'] = "Сервитут"

        ru_analog['servitude_kind'] = "Вид сервитута"
        ru_analog['servitude_condition'] = "Условия сервитута"

        ru_analog['restricted_rights_parties'] = "Сведения о лицах, в пользу которых установлены ограничения права и обременения объекта недвижимости"

        ru_analog['restricted_rights_party'] = "Сведения о лице, в пользу которого установлены ограничения права и обременения объекта недвижимости"

        ru_analog['type'] = "Тип лица, в пользу которых установлены ограничения права и обременения объекта недвижимости"
        ru_analog['subject'] = "Лицо, в пользу которого установлены ограничения права и обременения объекта недвижимости"

        ru_analog['public_formation'] = "Публично-правовое образование"
        ru_analog['individual'] = "Физическое лицо"

        ru_analog['legal_entity'] = "Юридическое лицо, орган власти"
        ru_analog['another'] = "Иное лицо, в пользу которого установлены ограничения права и обременения объекта недвижимости"
        ru_analog['public_servitude'] = "Публичный сервитут"
        ru_analog['undefined'] = "Не определено"

        ru_analog['another_type'] = "Тип иного субъекта"

        ru_analog['investment_unit_owner'] = "Владельцы инвестиционных паев"
        ru_analog['certificates_holders'] = "Владельцы ипотечных сертификатов участия"
        ru_analog['bonds_holders'] = "Владельцы облигаций"
        ru_analog['partnership'] = "Инвестиционное товарищество"
        ru_analog['aparthouse_owners'] = "Собственники помещений в многоквартирном доме"
        ru_analog['equity_participants_info'] = "Участники долевого строительства по договорам участия в долевом строительстве"

        ru_analog['not_equity_participants_info'] = "Участники долевого строительства по договорам участия в долевом строительстве, которым не переданы объекты долевого строительства"
        ru_analog['other'] = "Иной субъект"

        ru_analog['equity_participants'] = "Участники долевого строительства"

        ru_analog['not_equity_participants'] = "Участники долевого строительства по договорам участия в долевом строительстве, которым не переданы объекты долевого строительства"

        ru_analog['public'] = "Публичный сервитут"

        ru_analog['undefined'] = "Не определено"

        ru_analog['expropriation_info'] = "Сведения о решении об изъятии земельного участка и (или) расположенного на нем объекта недвижимости для государственных или муниципальных нужд"

        ru_analog['expropriation_info_type'] = "Сведения о решении об изъятии земельного участка и (или) расположенного на нем объекта недвижимости для государственных или муниципальных нужд"
        ru_analog['origin_content'] = "Содержание отметки при возникновении"


        ru_analog['deal_record'] = "Сведения о сделке"


        ru_analog['deal_data'] = "Общие сведения о сделке (вид сделки)"
        ru_analog['third_party_consents'] = "Сведения об осуществлении государственной регистрации сделки, права, ограничения права, совершенных без необходимого в силу закона согласия третьего лица, органа"


        ru_analog['deal_type'] = "Вид сделки"


        ru_analog['record_info'] = "Дата государственной регистрации"
        ru_analog['ownerless_right_data'] = "Общие сведения о правах на бесхозяйное имущество"

        ru_analog['ownerless_right_number'] = "Номер регистрации"
        ru_analog['authority_name'] = "Наименование органа местного самоуправления (органа государственной власти - для городов федерального значения Москвы, Санкт-Петербурга, Севастополя), представившего заявление о постановке на учет данного объекта недвижимости в качестве бесхозяйного"


        ru_analog['third_party_consent'] = "Сведения об осуществлении государственной регистрации сделки, права, ограничения права без необходимого в силу закона согласия третьего лица, органа"

        ru_analog['law'] = "Федеральный закон, которым предусмотрено получение согласия на совершение сделки"
        ru_analog['dissenting_entities'] = "Не представлено согласие на совершение сделки"
        ru_analog['mark_content'] = "Содержание отметки при возникновении / погашении"

        ru_analog['section'] = "Часть"
        ru_analog['paragraph'] = "Пункт"
        ru_analog['article'] = "Статья"
        ru_analog['law_date'] = "Дата"
        ru_analog['number'] = "Номер"
        ru_analog['name'] = "Наименование"


        ru_analog['dissenting_entity'] = "Не представлено согласие лица, органа"

        ru_analog['individual'] = "Физическое лицо"
        ru_analog['legal_entity'] = "Юридическое лицо, орган власти, местного самоуправления"

        ru_analog['name'] = "Наименование"

        ru_analog['registration_date'] = "Дата регистрации"

        ru_analog['restricting_right'] = "Ограничиваемое право"

        ru_analog['number'] = "Номер реестровой записи"
        ru_analog['right_number'] = "Номер регистрации вещного права"


        ru_analog['right_holder'] = "Сведения о правообладателе"

        ru_analog['public_formation'] = "Публично-правовое образование"
        ru_analog['individual'] = "Физическое лицо"
        ru_analog['legal_entity'] = "Юридическое лицо, орган власти"
        ru_analog['another'] = "Иной субъект права"

        ru_analog['public_formation_type'] = "Тип публично-правового образования"


        ru_analog['foreign_public'] = "Иностранное государство"
        ru_analog['union_state'] = "Союзное государство"
        ru_analog['russia'] = "Российская Федерация"
        ru_analog['subject_of_rf'] = "Субъект Российской Федерации"
        ru_analog['municipality'] = "Муниципальное образование"


        ru_analog['name'] = "Полное наименование иностранного государства"
        ru_analog['union_state (Союзное государство)'] = "union_state (Союзное государство)"

        ru_analog['name'] = "Союзное государство"


        ru_analog['name'] = "Российская Федерация"


        ru_analog['name'] = "Наименование субъекта Российской Федерации"


        ru_analog['name'] = "Наименование муниципального образования"


        ru_analog['individual_type'] = "Тип физического лица"
        ru_analog['surname'] = "Фамилия"
        ru_analog['name'] = "Имя"
        ru_analog['patronymic'] = "Отчество"
        ru_analog['birth_date'] = "Дата рождения"
        ru_analog['birth_place'] = "Место рождения"
        ru_analog['citizenship'] = "Гражданство"
        ru_analog['snils'] = "СНИЛС"
        ru_analog['identity_doc'] = "Документ, удостоверяющий личность"
        ru_analog['contacts'] = "Связь с правообладателем"


        ru_analog['person_citizenship_country'] = "Страна гражданства"
        ru_analog['no_citizenship_person'] = "Лицо без гражданства"


        ru_analog['citizenship_country'] = "Страна гражданства"


        ru_analog['no_citizenship'] = "Без гражданства"


        ru_analog['type'] = "Тип юридического лица"
        ru_analog['entity'] = "Юридическое лицо, орган власти"
        ru_analog['contacts'] = "Контактная информация"


        ru_analog['resident'] = "Российское юридическое лицо"
        ru_analog['govement_entity'] = "Орган государственной власти, орган местного самоуправления, иной государственный орган"
        ru_analog['not_resident'] = "Иностранное юридическое лицо"

        ru_analog['full_name'] = "Полное наименование"
        ru_analog['inn'] = "ИНН"
        ru_analog['ogrn'] = "ОГРН"

        ru_analog['another_type'] = "Тип иного субъекта права"

        ru_analog['investment_unit_owner'] = "Владельцы инвестиционных паев"
        ru_analog['certificates_holders'] = "Владельцы ипотечных сертификатов участия"
        ru_analog['bonds_holders'] = "Владельцы облигаций"
        ru_analog['partnership'] = "Инвестиционное товарищество"
        ru_analog['aparthouse_owners'] = "Собственники помещений в многоквартирном доме"
        ru_analog['other'] = "Иной субъект"

        ru_analog['investment_unit_name'] = "Название (индивидуальное обозначение), идентифицирующее паевой инвестиционный фонд"

        ru_analog['certificate_name'] = "Индивидуальное обозначение, идентифицирующее ипотечные сертификаты участия, в интересах владельцев которых осуществляется доверительное управление таким ипотечным покрытием"

        ru_analog['bonds_number'] = "Государственный регистрационный номер выпуска облигаций"
        ru_analog['issue_date'] = "Дата государственной регистрации номера выпуска облигаций"

        ru_analog['partnership_participants'] = "Участники договора инвестиционного товарищества"
        ru_analog['partnership_participants (Участники договора инвестиционного товарищества)'] = "partnership_participants (Участники договора инвестиционного товарищества)"
        ru_analog['partnership_participant'] = "Участник договора инвестиционного товарищества"
        ru_analog['partnership_participant (Участник договора инвестиционного товарищества)'] = "partnership_participant (Участник договора инвестиционного товарищества)"

        ru_analog['legal_entity'] = "Юридическое лицо (российское, иностранное юридическое лицо)"
        ru_analog['contacts'] = "Контактная информация"

        ru_analog['entity'] = "Юридическое лицо (российское, иностранное юридическое лицо)"
        ru_analog['entity (Юридическое лицо (российское, иностранное юридическое лицо))'] = "entity (Юридическое лицо (российское, иностранное юридическое лицо))"

        ru_analog['resident'] = "Российское юридическое лицо"
        ru_analog['not_resident'] = "Иностранное юридическое лицо"

        ru_analog['aparthouse_owners_name'] = "Собственники помещений в многоквартирном доме"

        ru_analog['incorporation_form'] = "Организационно-правовая форма"
        ru_analog['name'] = "Наименование"
        ru_analog['inn'] = "ИНН"
        ru_analog['ogrn'] = "ОГРН"

        ru_analog['incorporation_form'] = "Организационно-правовая форма"
        ru_analog['name'] = "Наименование"
        ru_analog['incorporate_country'] = "Страна регистрации (инкорпорации)"
        ru_analog['registration_number'] = "Регистрационный номер"
        ru_analog['date_state_reg'] = "Дата государственной регистрации"
        ru_analog['registration_organ'] = "Наименование регистрирующего органа"
        ru_analog['reg_address_subject'] = "Адрес (местонахождение) в стране регистрации (инкорпорации)"
        ru_analog['inn'] = "ИНН"

        ru_analog['name'] = "Наименование"
        ru_analog['short_name'] = "Краткое наименование"
        ru_analog['comment'] = "Комментарий"
        ru_analog['print_text'] = "Наименование для печати"
        ru_analog['registration_organ'] = "Регистрирующий орган"
        ru_analog['contacts'] = "Контакты"

        ru_analog['email'] = "Адрес электронной почты"
        ru_analog['mailing_addess'] = "Почтовый адрес"

        ru_analog['origin_mark'] = "Содержание отметки при возникновении"

        ru_analog['origin_content'] = "Содержание"

        ru_analog['surname'] = "Фамилия"
        ru_analog['name'] = "Имя"
        ru_analog['patronymic'] = "Отчество"

        # Документы
        ru_analog['underlying_document'] = "Документ-основание"


        ru_analog['document_code'] = "Код документа"
        ru_analog['document_name'] = "Наименование"
        ru_analog['document_series'] = "Серия документа"
        ru_analog['document_number'] = "Номер документа"
        ru_analog['document_date'] = "Дата документа"
        ru_analog['document_issuer'] = "Орган власти, организация, выдавшие документ"

        ru_analog['document_code'] = "Код документа"
        ru_analog['document_name'] = "Наименование"
        ru_analog['document_series'] = "Серия документа"
        ru_analog['document_number'] = "Номер документа"
        ru_analog['document_date'] = "Дата документа"
        ru_analog['document_issuer'] = "Кем выдан (Организация, выдавшая документ)"
        ru_analog['special_marks'] = "Особые отметки"
        ru_analog['doc_notarized'] = "Нотариальное удостоверение документа"

        ru_analog['underlying_document'] = "Документ-основание"

        ru_analog['document_code'] = "Код документа"
        ru_analog['document_name'] = "Наименование"
        ru_analog['document_series'] = "Серия документа"
        ru_analog['document_number'] = "Номер документа"
        ru_analog['document_date'] = "Дата документа"
        ru_analog['document_issuer'] = "Орган власти, организация, выдавшие документ"
        ru_analog['doc_notarized'] = "Нотариальное удостоверение документа"
        ru_analog['fullname_posts_person'] = "Полное наименование должности должностного лица"

        ru_analog['Тип DocNotarized'] = "Тип DocNotarized"
        ru_analog['notarize_date'] = "Дата нотариального удостоверения"
        ru_analog['notary_name'] = "Фамилия и инициалы нотариуса"
        ru_analog['notary_action_num'] = "Номер в реестре регистрации нотариальных действий"

        # Описание местоположения контура сооружения
        ru_analog['contour'] = "Контур"
        ru_analog['contour (Контур)'] = "contour (Контур)"

        ru_analog['number_pp'] = "Номер контура"
        ru_analog['entity_spatial'] = "Описание элементов контура (характерных точек контура)"
        ru_analog['entity_spatial (Описание элементов контура (характерных точек контура))'] = "entity_spatial (Описание элементов контура (характерных точек контура))"

        ru_analog['sk_id'] = "Система координат"
        ru_analog['spatials_elements'] = "Элементы контура"
        ru_analog['spatials_elements (Элементы контура)'] = "spatials_elements (Элементы контура)"

        ru_analog['spatial_element'] = "Элемент контура"
        ru_analog['spatial_element (Элемент контура)'] = "spatial_element (Элемент контура)"

        ru_analog['level_contour'] = "Тип контура"
        ru_analog['ordinates'] = "Список координат"
        ru_analog['ordinates (Список координат)'] = "ordinates (Список координат)"

        ru_analog['ordinate'] = "Координата"
        ru_analog['ordinate (Координата)'] = "ordinate (Координата)"

        ru_analog['x'] = "Координата X"
        ru_analog['y'] = "Координата Y"
        ru_analog['z'] = "Координата Z"
        ru_analog['ord_nmb'] = "Номер точки (порядок обхода)"
        ru_analog['num_geopoint'] = "Номер точки"
        ru_analog['delta_geopoint'] = "Погрешность"
        ru_analog['r'] = "Радиус"

        # Местоположение помещений, машиномест в объекте недвижимости (план(ы) расположения помещения)
        ru_analog['room_record'] = "Местоположение помещения, расположенного в объекте недвижимости (планы расположения помещения)"


        ru_analog['object'] = "Общие сведения (кадастровый номер помещения)"
        ru_analog['location_in_build'] = "Расположение в пределах объекта недвижимости (планы)"

        ru_analog['level'] = "Расположение в пределах объекта недвижимости (этажа, части этажа, нескольких этажей)"
        ru_analog['car_parking_space_records'] = "car_parking_space_records"

        ru_analog['car_parking_space_record'] = "Местоположение машиноместа, расположенного в объекте недвижимости (планы расположения машиноместа)"
        ru_analog['car_parking_space_record (Местоположение машиноместа, расположенного в объекте недвижимости (планы расположения машиноместа))'] = "car_parking_space_record (Местоположение машиноместа, расположенного в объекте недвижимости (планы расположения машиноместа))"

        ru_analog['object'] = "Общие сведения (кадастровый номер помещения)"
        ru_analog['location_in_build'] = "Расположение в пределах объекта недвижимости (планы)"

        ru_analog['common_data'] = "Общие сведения (кадастровый номер)"

        ru_analog['floor'] = "Номер этажа"
        ru_analog['floor_type'] = "Тип этажа"
        ru_analog['plan_number'] = "Номер на поэтажном плане"
        ru_analog['description'] = "Описание расположения"
        ru_analog['plans'] = "Планы"
        ru_analog['plans (Планы)'] = "plans (Планы)"

        ru_analog['plan'] = "План"
        ru_analog['plan (План)'] = "plan (План)"
        ru_analog['file_link'] = "Ссылка на файл"

        # Таблица 8 # Адрес (местоположение) сооружения
        # ru_analog['address_type'] = "Тип адреса"
        ru_analog['address'] = "Адрес (местоположение)"
        ru_analog['locations'] = "Наименования субъектов Российской Федерации, муниципальных образований, населенных пунктов (при наличии)"
        # ru_analog['Описание элементов и общих типов'] = "Описание элементов и общих типов"
        # ru_analog['Тип AddressMain (Адрес (местоположение))'] = "Тип AddressMain (Адрес (местоположение))"
        ru_analog['address_fias'] = "Адрес (по справочнику ФИАС)"
        ru_analog['note'] = "Неформализованное описание"
        ru_analog['readable_address'] = "Адрес в соответствии с ФИАС (Текст)"
        ru_analog['Тип Address (Адрес (описание местоположения) полный)'] = "Тип Address (Адрес (описание местоположения) полный)"
        ru_analog['level_settlement'] = "Уровень населенного пункта"
        ru_analog['detailed_level'] = "Детализированный уровень"
        # ru_analog['Тип LocationsCity (Наименования субъектов Российской Федерации, муниципальных образований, населенных пунктов (при наличии))'] = "Тип LocationsCity (Наименования субъектов Российской Федерации, муниципальных образований, населенных пунктов (при наличии))"
        ru_analog['location'] = "Наименование субъекта Российской Федерации, муниципального образования, населенного пункта (при наличии)"
        # ru_analog['Тип LocationCity (Местоположение (до уровня населенного пункта))'] = "Тип LocationCity (Местоположение (до уровня населенного пункта))"
        ru_analog['level_settlement'] = "Уровень населенного пункта"
        ru_analog['position_description'] = "Описание местоположения"
        # ru_analog['Тип AddressCity (Адрес (описание местоположения) до уровня населённого пункта)'] = "Тип AddressCity (Адрес (описание местоположения) до уровня населённого пункта)"
        ru_analog['fias'] = "код ФИАС"
        ru_analog['okato'] = "ОКАТО"
        ru_analog['kladr'] = "КЛАДР"
        ru_analog['oktmo'] = "ОКТМО"
        ru_analog['postal_code'] = "Почтовый индекс"
        ru_analog['region'] = "Код региона"
        ru_analog['district'] = "Район "
        ru_analog['city'] = "Муниципальное образование"
        ru_analog['urban_district'] = "Городской район"
        ru_analog['soviet_village'] = "Сельсовет"
        ru_analog['locality'] = "Населённый пункт"
        ru_analog['Тип District (Район)'] = "Тип District (Район)"
        ru_analog['type_district'] = "Тип"
        ru_analog['name_district'] = "Наименование"
        # ru_analog['Тип City (Муниципальное образование)'] = "Тип City (Муниципальное образование)"
        ru_analog['type_city'] = "Тип"
        ru_analog['name_city'] = "Наименование"
        # ru_analog['Тип UrbanDistrict (Городской район)'] = "Тип UrbanDistrict (Городской район)"
        ru_analog['type_urban_district'] = "Тип"
        ru_analog['name_urban_district'] = "Наименование"
        # ru_analog['Тип SovietVillage (Сельсовет)'] = "Тип SovietVillage (Сельсовет)"
        ru_analog['type_soviet_village'] = "Тип"
        ru_analog['name_soviet_village'] = "Наименование"
        # ru_analog['Тип Locality (Населённый пункт)'] = "Тип Locality (Населённый пункт)"
        ru_analog['type_locality'] = "Тип"
        ru_analog['name_locality'] = "Наименование"
        # ru_analog['Тип DetailedLevel (Детализированный уровень)'] = "Тип DetailedLevel (Детализированный уровень)"
        ru_analog['street'] = "Улица"
        ru_analog['level1'] = "Дом"
        ru_analog['Level2'] = "Корпус"
        ru_analog['Level3'] = "Строение"
        ru_analog['apartment'] = "Квартира"
        ru_analog['other'] = "Иное описание местоположения"
        # ru_analog['Тип Street (Улица)'] = "Тип Street (Улица)"
        ru_analog['type_street'] = "Тип"
        ru_analog['name_street'] = "Наименование"
        # ru_analog['Тип Level1 (Дом)'] = "Тип Level1 (Дом)"
        ru_analog['type_level1'] = "Тип"
        ru_analog['name_level1'] = "Значение"
        # ru_analog['Тип Level2'] = "Тип Level2"
        ru_analog['type_level2'] = "Тип"
        ru_analog['name_level2'] = "Значение"
        # ru_analog['Тип Level3'] = "Тип Level3"
        ru_analog['type_level3'] = "Тип"
        ru_analog['name_level3'] = "Значение"
        # ru_analog['Тип Apartment'] = "Тип Apartment"
        ru_analog['type_apartment'] = "Тип"
        ru_analog['name_apartment'] = "Значение"


        ru_analog[''] = ""



