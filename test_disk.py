from disk import *
from bcca.test import fake_file

inv_string = '1,Jim,5,50,5'
hist_string = '12:00,7,500,173.27'


def test_parse_inventory_item():
    result = parse_inventory_item(inv_string)

    assert result == ['1', 'Jim', 5, 50, 5]


def test_parse_history_item():
    result = parse_history_item(hist_string)

    assert result == ['12:00', '7', '500', '173.27']


@fake_file({
    'inventory.txt':
    'number,name,stock,replacement_fee,daily_fee\n1,Sedans,10,5000,12'
})
def test_open_file():
    result = open_file('inventory.txt')

    assert result == {
        '1': {
            'Name': 'Sedans',
            'Stock': 10,
            'Replacement_fee': 5000,
            'Daily_fee': 12
        }
    }
