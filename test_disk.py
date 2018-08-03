from disk import *
from bcca.test import fake_file

inv_string = '1,Jim,5,50,5'
hist_string = '12:00,7,500,173.27'
inventory = {
    '1': {
        'Name': 'Sedans',
        'Stock': 10,
        'Replacement_fee': 5000,
        'Daily_fee': 12
    }
}
history = {
    '2018-07-30 10:57:38.919233': {
        'days_rented': '7',
        'deposit': '1000.0',
        'profit': '127.33'
    }
}


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


@fake_file({
    'history.txt':
    'time,days_rented,deposit,profit\n2018-07-30 10:57:38.919233,7,1000.0,127.33'
})
def test_open_file_history():
    result = open_file_history()

    assert result == '2018-07-30 10:57:38.919233, 7,1000.0, 127.33'


def test_inventory_to_string():
    result = inventory_to_string(inventory)

    assert result == '\n1,Sedans,10,5000,12'


def test_history_to_string():
    result = history_to_string(history)

    assert result == '\n2018-07-30 10:57:38.919233,7,1000.0,127.33'


@fake_file({
    'inventory.txt':
    'number,name,stock,replacement_fee,daily_fee1,Sedans,10,5000,12'
})
def test_write_to_file_inv():
    write_to_file_inv(inventory)

    assert open('inventory.txt').read(
    ) == 'number,name,stock,replacement_fee,daily_fee\n1,Sedans,10,5000,12'


@fake_file({'history.txt': 'time,days_rented,deposit,profit'})
def test_write_to_file_history():
    write_to_file_history(history)

    assert open('history.txt').read(
    ) == 'time,days_rented,deposit,profit\n2018-07-30 10:57:38.919233,7,1000.0,127.33'
