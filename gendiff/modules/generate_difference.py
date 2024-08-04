import pathlib
from gendiff.formaters import select_formater
from gendiff.modules.parser import get_dict
from gendiff.modules.search_difference import search_difference


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = get_dict(get_string(file_path1),
                     pathlib.PurePosixPath(file_path1).suffix)
    dict2 = get_dict(get_string(file_path2),
                     pathlib.PurePosixPath(file_path1).suffix)

    difference = search_difference(dict1, dict2)

    return select_formater(format)(difference)


def get_string(file_path):
    with open(file_path, 'r') as file_object:
        string = file_object.read()
    return string
