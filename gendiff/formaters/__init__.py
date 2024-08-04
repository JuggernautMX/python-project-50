from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish

formaters = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json, }


def select_formater(format):
    if format not in formaters:
        raise TypeError('Wrong format!')

    return formaters[format]
