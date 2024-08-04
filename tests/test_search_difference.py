from gendiff.modules.search_difference import (
    get_keys,
    get_value,
    search_difference
)


def test_get_keys():
    dict1 = {"a": "aa", "b": "bb"}
    dict2 = {"b": "bb", "c": "cc"}
    assert get_keys(dict1, dict2) == {"a", "b", "c"}


def test_search_difference():
    dict1 = {"a": "aa", "b": "bb", "d": {"dd": "ddd"}}
    dict2 = {"b": "bbb", "c": "cc", "d": {"dd": "dddd"}}
    expectation = (
    {'a': {'type': 'removed', 'value': 'aa'},  # noqa
     'b': {'type': 'updated', 'value1': 'bb',
           'value2': 'bbb'},
     'c': {'type': 'added', 'value': 'cc'},
     'd': {'type': 'nested', 'children':
           {'dd': {'type': 'updated',
                   'value1': 'ddd', 'value2': 'dddd'}}}
     })
    assert search_difference(dict1, dict2) == expectation


def test_get_value():
    dict1 = {"a": "aa", "b": "bb"}
    dict2 = {"b": "bb", "c": "cc"}
    assert get_value(dict1, dict2, 'a') == {
        'type': 'removed',
        'value': 'aa'}
    assert get_value(dict1, dict2, 'b') == {
        'type': 'not changed',
        'value': 'bb'}
    assert get_value(dict1, dict2, 'c') == {
        'type': 'added',
        'value': 'cc'}
