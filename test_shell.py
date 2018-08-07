from shell import *
from unittest.mock import Mock, patch
from bcca.test import with_inputs, should_print

inventory = {
    '1': {
        'Name': 'Sedan',
        'Stock': 9,
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


@with_inputs('c')
@should_print
def test_customer_login(output):
    result = login()

    assert "c" in result


@with_inputs('e')
@should_print
def test_employee_login(output):
    result = login()

    assert "e" in result
