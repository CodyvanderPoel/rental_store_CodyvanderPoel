from core import *
from disk import *
from time import sleep
from datetime import datetime


def login():
    while True:
        choice = input("[C]ustomer or [E]mployee or [L]eave:")
        if choice.upper() == 'C':
            print("Welcome To Cody's Car Rental!")
            sleep(.5)
            return choice
        elif choice.upper() == 'E':
            print("Welcome to Cody's Car Rental database!")
            sleep(.5)
            return choice
        elif choice.upper() == 'L':
            print("Have A Good Day!")
            exit()
        else:
            print("The option you have chosen is not available!")


def customer_return(inventory):
    while True:
        choice = input(
            "What vehicle are you returning to us today?\n1--Sedan\n2--SUV\n3--Minivan\n4--Van\n5--Truck:"
        )
        if choice == '1':
            choice = inventory['Sedans']
            stock = can_return(choice)
            if stock == True:
                choice['Stock'] += 1
                print('Thank You for returning our vehicle! Have A Good Day!')
                write_to_file_inv(inventory)
                exit()
            else:
                print(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.'
                )
                exit()
        elif choice == '2':
            choice = inventory['SUVS']
            stock = can_return(choice)
            if stock == True:
                choice['Stock'] += 1
                print('Thank You for returning our vehicle! Have A Good Day!')
                write_to_file_inv(inventory)
                exit()
            else:
                print(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.'
                )
                exit()
        elif choice == '3':
            choice = inventory['Minivans']
            stock = can_return(choice)
            if stock == True:
                choice['Stock'] += 1
                print('Thank You for returning our vehicle! Have A Good Day!')
                write_to_file_inv(inventory)
                exit()
            else:
                print(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.'
                )
                exit()
        elif choice == '4':
            choice = inventory['Vans']
            stock = can_return(choice)
            if stock == True:
                choice['Stock'] += 1
                print('Thank You for returning our vehicle! Have A Good Day!')
                exit()
            else:
                print(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.'
                )
                write_to_file_inv(inventory)
                exit()
        elif choice == '5':
            choice = inventory['Trucks']
            stock = can_return(choice)
            if stock == True:
                choice['Stock'] += 1
                print('Thank You for returning our vehicle! Have A Good Day!')
                write_to_file_inv(inventory)
                exit()
            else:
                print(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.'
                )
                exit()
        else:
            print('That is not an option!')


def customer_rental(inventory):
    options = get_inv_options(inventory)
    print('Here are our available options:\n', options)
    vehicle = input("Now what would you like to rent?")
    if vehicle == "1":
        vehicle = inventory['Sedans']
        stock = is_in_stock(vehicle)
        if stock == True:
            vehicle['Stock'] -= 1
            return vehicle
        else:
            print(
                'This vehicle is currently out of stock. Please choose another vehicle!'
            )
    elif vehicle == "2":
        vehicle = inventory['SUVS']
        stock = is_in_stock(vehicle)
        if stock == True:
            vehicle['Stock'] -= 1
            return vehicle
        else:
            print(
                'This vehicle is currently out of stock. Please choose another vehicle!'
            )
    elif vehicle == "3":
        vehicle = inventory['Minivans']
        stock = is_in_stock(vehicle)
        if stock == True:
            vehicle['Stock'] -= 1
            return vehicle
        else:
            print(
                'This vehicle is currently out of stock. Please choose another vehicle!'
            )
    elif vehicle == "4":
        vehicle = inventory['Vans']
        stock = is_in_stock(vehicle)
        if stock == True:
            vehicle['Stock'] -= 1
            return vehicle
        else:
            print(
                'This vehicle is currently out of stock. Please choose another vehicle!'
            )
    elif vehicle == "5":
        vehicle = inventory['Trucks']
        stock = is_in_stock(vehicle)
        if stock == True:
            vehicle['Stock'] -= 1
            return vehicle
        else:
            print(
                'This vehicle is currently out of stock. Please choose another vehicle!'
            )
    else:
        print('That Is Not an Option!')


def customer_options(inventory):
    while True:
        choice = input('1--Return\n2--Rental\n3--Leave:')
        if choice == '1':
            customer_return(inventory)
            exit()
        elif choice == '2':
            vehicle = customer_rental(inventory)
            return vehicle
        elif choice == '3':
            print('Have A Good Day!')
            exit()
        else:
            print('That is not an option!')


def employee_options():
    print(
        'Employee Options:\n1--Check Stock\n2--Review Transactions\n3--Clock Out'
    )
    while True:
        choice = input('What would you like to do?')
        if choice == '1':
            inv = open_file('inventory.txt')
            print(inv)
        elif choice == '2':
            receipt = open_file_history()
            print(receipt)
        elif choice == '3':
            print('Have A Good Day!')
            exit()
        else:
            print('That is not an option!')


def get_days():
    while True:
        days = input('How many days would you like to rent the vehicle?')
        if days.isdigit():
            return days
        else:
            print('I am sorry that is not a number sir')


def main():
    choice = login()
    if choice.upper() == 'C':
        inventory = open_file('inventory.txt')
        vehicle = customer_options(inventory)
        fee_1 = deposit_fee(vehicle)
        print(f'The deposit fee is ${fee_1}')
        days = get_days()
        fee_2 = total_rental_fee(vehicle, days)
        print(f'The total rental fee is ${fee_2}')
        print('Have A Good Day!')
        write_to_file_inv(inventory)
        time = datetime.now()
        history = {
            'name': vehicle,
            'time': time,
            'days_rented': days,
            'deposit': fee_1,
            'profit': fee_2
        }
        write_to_file_history(history)
    else:
        employee_options()


if __name__ == '__main__':
    main()
