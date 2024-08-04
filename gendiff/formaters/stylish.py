import json

prefixes = {
    'removed': '  - ',
    'added': '  + ',
    'not changed': '    ',
    'updated': '    ',
    'nested': '    '
}


def format_value(value, depth=0):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, dict):
        return get_string_from_dictionary(value, depth + 1)
    return str(value)


def format_stylish(diff, depth=0):
    indent = '    ' * depth
    difference = ['{']
    keys = diff.keys()

    for key in keys:
        type = diff[key]['type']
        string = get_formatted_string(indent, type, diff, key, depth)
        difference.append(string)
    difference.append(f'{indent}}}')
    return '\n'.join(difference)


def get_formatted_string(indent, status, diff, key, depth):
    if status == 'added':
        string = (f'{indent}{prefixes["added"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'removed':
        string = (f'{indent}{prefixes["removed"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'not changed':
        string = (f'{indent}{prefixes["not changed"]}{key}: '
                  f'{format_value(diff[key]["value"], depth)}')

    elif status == 'updated':
        string = (f'{indent}{prefixes["removed"]}{key}: '
                  f'{format_value(diff[key]["value1"], depth)}\n'
                  f'{indent}{prefixes["added"]}{key}: '
                  f'{format_value(diff[key]["value2"], depth)}')

    elif status == 'nested':
        string = (f'{indent}{prefixes[status]}{key}: '
                  f'{format_stylish(diff[key]["children"], depth + 1)}')
    return string


def get_string_from_dictionary(diff, depth):
    indent = '    ' * depth
    nested_diff = []
    if isinstance(diff, dict):
        nested_diff.append('{')
        keys = diff.keys()
        for key in keys:
            string = (f'{indent}{prefixes["not changed"]}{key}: '
                      f'{get_string_from_dictionary(diff[key], depth + 1)}')
            nested_diff.append(string)
        nested_diff.append(f'{indent}}}')
    else:
        if isinstance(diff, bool) or diff is None:
            nested_diff.append(json.dumps(diff))
        elif isinstance(diff, dict):
            nested_diff.append(diff, depth + 1)
        nested_diff.append(str(diff))
    return '\n'.join(nested_diff)
