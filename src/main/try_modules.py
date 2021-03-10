def iflist(mblist, lmbd) -> list:
    if isinstance(mblist, list):
        return [lmbd(i) for i in mblist]
    else:
        return [lmbd(mblist)]


def _try_get(nested_dict, dict_keys):
    """
    Tries to select single node from nested dict and write it to the list at the index.

    :param set_list: will convert to excel
    :param index: column's index
    :param nested_dict: was parsed from xml (tree structure)
    :param dict_keys: key list to navigate the dict tree
    :return: same value being writen to set_list
    """
    try:
        for dict_key in dict_keys:
            nested_dict = nested_dict.__getitem__(dict_key)
        return nested_dict
    except:
        return ''


def _try(_dict, _fields):
    try:
        return _dict[_fields]
    except:
        return None



# -----------------
def _try_set(set_list, index, nested_dict, dict_keys=[]):
    """
    Tries to select single node from nested dict and write it to the list at the index.

    :param set_list: will convert to excel
    :param index: column's index
    :param nested_dict: was parsed from xml (tree structure)
    :param dict_keys: key list to navigate the dict tree
    :return: same value being writen to set_list
    """
    try:
        for dict_key in dict_keys:
            nested_dict = nested_dict.__getitem__(dict_key)
        set_list[index] = str(nested_dict)
        return nested_dict
    except:
        return ''


def _try_append(set_list, index, nested_dict, dict_keys=[]):
    """
    Appends selected single node from nested dict to the list at the index.
    Append instead of rewriting as in case of __try_set.

    :param set_list: will convert to excel
    :param index: column's index
    :param nested_dict: was parsed from xml (tree structure)
    :param dict_keys: key list to navigate the dict tree
    :return: same value being writen to set_list
    """
    try:
        for dict_key in dict_keys:
            nested_dict = nested_dict.__getitem__(dict_key)
        if set_list:
            set_list[index] += str(nested_dict)
        return nested_dict
    except:
        return ''


# ------- advanced

def _try_date(set_list, index, nested_dict, dict_keys=[], try_func=_try_set):
    """
    Use try_func and converts its string result to date string.

    :param set_list: will convert to excel
    :param index: column's index
    :param nested_dict: was parsed from xml (tree structure)
    :param dict_keys: key list to navigate the dict tree
    :param try_func: try func to be used
    :return: same value being writen to set_list
    """
    import datetime
    try:
        dt = try_func(None, None, nested_dict, dict_keys) # 2012-07-05T00:00:00+04:00
        dt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S%z")
        try_func(set_list, index, str(dt.date()))
        print(str(dt.date())+" sdfsdfsdf")
        return dt.date()  # Дата присвоения кадастрового номера
    except:
        return ''


def _try_change_value_if(set_list, index, nested_dict, dict_keys=[], try_func=_try_set, if_condition=lambda value: value == "",
                         change_value_to=""):
    """
    Use @try_func, then @change_value_to given according to @if_condition function return true.

    :param set_list: will convert to excel
    :param index: column's index
    :param nested_dict: was parsed from xml (tree structure)
    :param dict_keys: key list to navigate the dict tree
    :param try_func: try func to be used
    :param if_condition:
    :param change_value_to:
    :return: same value being writen to set_list
    """
    try:
        value = try_func(set_list, index, nested_dict, dict_keys)
        if if_condition(value):
            set_list[index] = change_value_to
            return change_value_to
    except:
        return ''


#TODO remake this into simpler for function
def _try_isinstance_of_list(set_list,
                    index,
                    nested_dict,
                    dict_keys=[],
                    try_func=_try_set,
                    do_func=lambda *args, **kwargs: "",
                    do_func_is_not=lambda *args, **kwargs: "",
                    *args,
                    **kwargs
                    ):
    # do additional function if instance
    try:
        instance_or_not = try_func(set_list, index, nested_dict, dict_keys)
        if isinstance(instance_or_not, list):
            for element in instance_or_not:
                return do_func(element, *args, **kwargs)
        else:
            return do_func_is_not(instance_or_not, *args, **kwargs)
    except:
        return ''




def execute_for_one_or_many(parsed_xml_element, method):
    if isinstance(parsed_xml_element, list):
        for right_record in parsed_xml_element:
            method(right_record)
    else:
        method(parsed_xml_element)



