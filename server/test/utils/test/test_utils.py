import pytest
from test.utils import dict_list_to_tuple_list

def test_dict_list_to_tuple_list():
    dict_list = [
        {"a": 123, "sadfkjh": 34},
        {"aslkdf": 134890, "vbnrejkb": "asdfjkl"},
        {"askhjgjwerh": False}
    ]

    output = dict_list_to_tuple_list(dict_list)
    expected_output = [
        dict([("a", 123), ("sadfkjh", 34)]).items(),
        dict([("aslkdf", 134890), ("vbnrejkb", "asdfjkl")]).items(),
        dict([("askhjgjwerh", False)]).items()
    ]
    
    assert output == expected_output
