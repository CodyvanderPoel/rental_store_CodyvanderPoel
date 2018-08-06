from shell import *
from bcca.test import with_inputs, should_print


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
