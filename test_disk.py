from disk import *
from bcca.test import fake_file

inv_string = '1,Jim,5,50,5'


def test_parse_inventory_item():
    result = parse_inventory_item(inv_string)

    assert result == ['1', 'Jim', 5, 50, 5]
