from core import *

sedan = {'Stock': 10, 'Replacement_fee': 5000, 'Rental_fee': 12}
suv = {'Stock': 10, 'Replacement_fee': 7000, 'Rental_fee': 15}
mini = {'Stock': 10, 'Replacement_fee': 8000, 'Rental_fee': 16}
van = {'Stock': 10, 'Replacement_fee': 10000, 'Rental_fee': 17}
truck = {'Stock': 0, 'Replacement_fee': 12500, 'Rental_fee': 20}


def test_deposit_fee_sedan():
    assert deposit_fee(sedan) == 500


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
    assert total_rental_fee(sedan, days) == 84


def test_can_return():
    assert can_return(truck) == True


def test_cannot_return():
    assert can_return(van) == False


def test_is_not_in_stock():
    assert is_in_stock(truck) == False


def test_is_in_stock():
    assert is_in_stock(van) == True
