from gendiff.formaters.plain import format_value


def test_decoding_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value({'a': 'b'}) == '[complex value]'
    assert format_value(300) == 300
