def __try_set(set_list, index, nested_dict, dict_keys=[]):
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
        return str(nested_dict)
    except:
        return ''


def __try_append(set_list, index, nested_dict, dict_keys=[]):
    """
    Appends selected single node from nested dict to the list at the index. Append instead of rewriting as in case of __try_set.

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
        return str(nested_dict)
    except:
        return ''


# ------- advanced

def __try_date(set_list, index, nested_dict, dict_keys=[], try_func=__try_set):
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
        return str(dt.date())  # Дата присвоения кадастрового номера
    except:
        return ''


def __try_change(set_list, index, nested_dict, dict_keys=[], try_func=__try_set, if_condition=lambda value: value == "",
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
def __try_isinstance(set_list, index, nested_dict, dict_keys=[], try_func=__try_set, _class=list, do_func=lambda *args,
                     **kwargs: "", *args, **kwargs):
    # do additional function if instance
    try:
        instance_or_not = try_func(set_list, index, nested_dict, dict_keys)
        if isinstance(instance_or_not, _class):
            set_list[index] = ''
            return do_func(*args, **kwargs)
        else:
            set_list[index] = instance_or_not
            return instance_or_not
    except:
        return ''


