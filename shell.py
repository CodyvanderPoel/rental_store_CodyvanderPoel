from core import *
from disk import *
from time import sleep
from datetime import datetime


def login():
    while True:
        choice = input("[U]ser or [E]mployee or [L]eave:")
        if choice.upper() == 'U':
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


def user_rental(inventory):
    print(
        "These are our current available vehicles:\n1--Sedans\n2--SUVS\n3--Minivans\n4--Vans\n5--Trucks"
    )
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


def user_options(inventory):
    while True:
        choice = input('1--Return\n2--Rental\n3--Leave:')
        if choice == '1':
            pass
            #delivery = user_return(inventory)
            #return delivery
        elif choice == '2':
            vehicle = user_rental(inventory)
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
            receipt = open_file('history.txt')
            print(receipt)
        elif choice == '3':
            print('Have A Good Day!')
            exit()
        else:
            print('That is not an option!')


def main():
    choice = login()
    if choice.upper() == 'U':
        inventory = open_file('inventory.txt')
        vehicle = user_options(inventory)
        fee_1 = deposit_fee(vehicle)
        print(f'The deposit fee is ${fee_1}')
        days = input('How many days would you like to rent the vehicle?')
        fee_2 = total_rental_fee(vehicle, days)
        print(f'The total rental fee is ${fee_2}')
        print('Have A Good Day!')
    else:
        employee_options()


if __name__ == '__main__':
    main()
