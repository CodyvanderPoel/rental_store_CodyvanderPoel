from core import *

sedan = {'Stock': 10, 'Replacement_fee': 5000, 'Daily_fee': 12}
suv = {'Stock': 10, 'Replacement_fee': 7000, 'Daily_fee': 15}
mini = {'Stock': 10, 'Replacement_fee': 8000, 'Daily_fee': 16}
van = {'Stock': 10, 'Replacement_fee': 10000, 'Daily_fee': 17}
truck = {'Stock': 0, 'Replacement_fee': 12500, 'Daily_fee': 20}

inventory1 = {
    '1': {
        'Name': 'Sedan',
        'Stock': 10,
        'Replacement_fee': 5000,
        'Daily_fee': 12
    },
    '2': {
        'Name': 'SUV',
        'Stock': 10,
        'Replacement_fee': 7000,
        'Daily_fee': 15
    },
    '3': {
        'Name': 'Truck',
        'Stock': 0,
        'Replacement_fee': 12500,
        'Daily_fee': 20
    }
}

inventory2 = {'1': {'Name': 'a'}, '2': {'Name': 'b'}}


def test_deposit_fee_suv():
    assert deposit_fee(suv) == 700


def test_deposit_fee_mini():
    assert deposit_fee(mini) == 800


def test_deposit_fee_van():
    assert deposit_fee(van) == 1000


def test_deposit_fee_truck():
    assert deposit_fee(truck) == 1250


def test_total_rental_fee_sedan():
    days = '7'
    assert total_rental_fee(sedan, days) == 89.88


def test_can_return():
    assert can_return(truck) == True


def test_cannot_return():
    assert can_return(van) == False


def test_is_not_in_stock():
    assert is_in_stock(truck) == False


def test_is_in_stock():
    assert is_in_stock(van) == True


def test_make_inv_options1():
    result = make_inv_options(inventory1)

    assert result == '1--Sedan\n2--SUV\n3--Truck'


def test_make_inv_options2():
    result = make_inv_options(inventory2)

    assert result == '1--a\n2--b'
