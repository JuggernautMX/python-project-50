import json


def format_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"


def format_plain(diff, path=''):
    keys = sorted(diff.keys())
    difference = []
    for key in keys:
        status = diff[key]['type']
        full_path = path
        string = get_formatted_object(key, diff, full_path, status)
        if string:
            difference.append(string)
    return '\n'.join(difference)


def get_formatted_object(key, diff, full_path, type):
    if type == 'not changed':
        string = ''

    elif type == 'nested':
        full_path += (f'{key}.')
        string = format_plain(diff[key]['children'], full_path)

    elif type == 'removed':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' was removed")

    elif type == 'added':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' "
                  f"was added with value: {format_value(diff[key]['value'])}")

    elif type == 'updated':
        full_path += (f'{key}')
        string = (f"Property '{full_path}' was updated. "
                  f"From {format_value(diff[key]['value1'])} "
                  f"to {format_value(diff[key]['value2'])}")
    return string
