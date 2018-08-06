from core import *
from disk import *
import sys
from termcolor import colored, cprint
from time import sleep
from datetime import datetime


def login():
    while True:
        choice = input("[C]ustomer or [E]mployee or [L]eave:")
        if choice.upper() == 'C':
            cprint("Welcome To Cody's Car Rental!", 'cyan')
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
            cprint(
                'THAT IS NOT AN OPTION!\nLOGIN ERROR 5345',
                'red',
                attrs=['blink'])


def customer_return(inventory):
    while True:
        options = make_inv_options(inventory)
        choice = input(f'What are you returning today?\n{options}\n???')
        if choice in options:
            vehicle = inventory[choice]
            if can_return(vehicle) == True:
                vehicle['Stock'] += 1
                fee = deposit_fee(vehicle)
                print(
                    f'Thank You for returning our vehicle! Here is your deposit of ${fee}. Have A Good Day!'
                )
                write_to_file_inv(inventory)
            else:
                cprint(
                    'I am sorry to say this, but this vehicle is not ours. Please leave the premises.',
                    'red')
            exit()
        else:
            cprint('That is not an option!', 'red')


def customer_rental(inventory):
    options = make_inv_options(inventory)
    print('Here are our available options:\n', options)
    while True:
        choice = input("Now what would you like to rent?")
        if choice in options:
            vehicle = inventory[choice]
            if is_in_stock(vehicle) == True:
                vehicle['Stock'] -= 1
                return vehicle
        else:
            cprint('That is not an option!', 'red')


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
            cprint('That is not an option!', 'red')


def employee_options():
    print(
        'Employee Options:\n1--Check Stock\n2--Review Transactions\n3--Clock Out'
    )
    while True:
        choice = input('What would you like to do?')
        if choice == '1':
            inv = open_file('inventory.txt')
            inv = show_employee_inv(inv)
            print(inv)
        elif choice == '2':
            receipt = open_file_history()
            print(receipt)
        elif choice == '3':
            print('Have A Good Day!')
            exit()
        else:
            cprint('That is not an option!', 'red')


def get_days():
    while True:
        days = input('How many days would you like to rent the vehicle?')
        if days.isdigit():
            return days
        else:
            cprint('I am sorry that is not a number sir', 'red')


def main():
    store = True
    while store != False:
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
            history = make_history(time, days, fee_1, fee_2)
            write_to_file_history(history)
            store = False
        elif choice.upper() == 'E':
            employee_options()


if __name__ == '__main__':
    main()
