def deposit_fee(vehicle):
    fee = vehicle['Replacement_fee'] / 10
    return fee


def total_rental_fee(vehicle, days):
    days = int(days)
    fee = vehicle['Rental_fee'] * days
    tax = 0.07
    fee += fee * tax
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
