from collections import OrderedDict


def dict_format(dic, change_key_pattern_func, *args):
    orderedDict = OrderedDict(dic)
    format_dict = OrderedDict()
    if isinstance(orderedDict, list) and all(isinstance(item, dict) for item in orderedDict):
        for vIndex, vItem in enumerate(orderedDict):
            orderedDict[vIndex] = dict_format(vItem, change_key_pattern_func, *args)
        format_dict = orderedDict.deepcopy()
    else:
        for k, v in orderedDict.items():
            if isinstance(v, dict):
                new_v = dict_format(v, change_key_pattern_func, *args)
                format_dict[k] = new_v
            elif isinstance(v, list) and all(isinstance(item, dict) for item in v):
                for vIndex, vItem in enumerate(v):
                    v[vIndex] = dict_format(vItem, change_key_pattern_func, *args)
                format_dict = orderedDict
            else:
                new_v = change_key_pattern_func({k: v}, *args)
                format_dict.update(new_v)
    return format_dict


def change_dict_key_pattern(innestDict, value_tuple):
    new_innestDict = {}
    old_dex = value_tuple[0]
    new_dex = value_tuple[1]
    for k, v in innestDict.items():
        v_ = str(v)
        if old_dex in k:
            new_innestDict[k.replace(old_dex, new_dex)] = v_
        else:
            new_innestDict[k] = v_
    return new_innestDict


def exclude_str_root(raw_dict):
    new_dict = {}

    for k, v in raw_dict.items():
        if (k[:4] == "root"):
            new_k = k[4:]
        else:
            new_k = k

        if (isinstance(v, dict)):
            new_v = exclude_str_root(v)
            new_dict[new_k] = new_v
        else:
            new_dict[new_k] = v

    return new_dict
