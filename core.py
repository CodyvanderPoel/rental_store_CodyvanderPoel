def deposit_fee(vehicle):
    fee = vehicle[1] / 10
    return fee


def total_rental_fee(vehicle, days):
    fee = vehicle[2] * days
    return fee
