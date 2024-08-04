def get_keys(dict1, dict2):
    return set(list(dict1.keys()) + list(dict2.keys()))


def get_value(dict1, dict2, key):
    if key in dict1 and key not in dict2:
        value = {
            'type': 'removed',
            'value': dict1.get(key)}
    elif key in dict2 and key not in dict1:
        value = {
            'type': 'added',
            'value': dict2.get(key)}
    elif dict1[key] == dict2[key]:
        value = {
            'type': 'not changed',
            'value': dict1.get(key)}
    elif not isinstance(dict1[key], dict) or not isinstance(dict2[key], dict):
        value = {
            'type': 'updated',
            'value1': dict1.get(key),
            'value2': dict2.get(key)}
    elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
        value = {
            'type': 'nested',
            'children': search_difference(dict1[key], dict2[key])}
    return value


def search_difference(dict1, dict2):
    keys = sorted(get_keys(dict1, dict2))
    difference = {}
    for key in keys:
        difference[key] = get_value(dict1, dict2, key)
    return difference
