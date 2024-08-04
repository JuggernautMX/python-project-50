from gendiff.formaters.stylish import (
    format_value,
    get_string_from_dictionary
)

nested_object = {'deep': {'id': {'number': 45}}, 'fee': 100500}


def test_format_value():
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'
    assert format_value(
           nested_object) == get_string_from_dictionary(nested_object, 1)


def test_get_string_from_dictionary():
    expectation_nested = """{
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }"""
    assert get_string_from_dictionary(nested_object, 1) == expectation_nested
