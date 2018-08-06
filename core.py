def deposit_fee(vehicle):
    fee = vehicle['Replacement_fee'] / 10
    return fee


def total_rental_fee(vehicle, days):
    days = int(days)
    fee = vehicle['Daily_fee'] * days
    tax = 1.07
    fee *= tax
    return round(fee, 2)


def can_return(vehicle):
    if vehicle['Stock'] < 10:
        return True
    else:
        return False


def is_in_stock(vehicle):
    if vehicle['Stock'] == 0:
        return False
    else:
        return True


def make_inv_options(inventory):
    return '\n'.join([
        '{}--{}'.format(str(i + 1), item['Name'])
        for i, item in enumerate(inventory.values())
    ])


def employee_inv(inv):
    return '\n'.join([
        '{}--{}, Stock: {}, Replacement Fee: {}, Daily Fee: {}'.format(
            str(i + 1), item['Name'], item['Stock'], item['Replacement_fee'],
            item['Daily_fee']) for i, item in enumerate(inv.values())
    ])


def make_history(time, days, fee_1, fee_2):
    history = {
        'time': time,
        'days_rented': days,
        'deposit': fee_1,
        'profit': fee_2
    }
    return history
