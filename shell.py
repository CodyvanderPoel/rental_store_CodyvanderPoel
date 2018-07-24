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


def user_options(inventory):
    print(
        "These are our current available vehicles:\n1--Sedans\n2--SUVS\n3--Minivans\n4--Vans\n5--Trucks"
    )
    while True:
        vehicle = input("Now what would you like to rent?")
        if vehicle == "1":
            vehicle = stuff['Sedans']
            return vehicle
        elif vehicle == "2":
            vehicle = stuff['SUVS']
            return vehicle
        elif vehicle == "3":
            vehicle = stuff['Minivans']
            return vehicle
        elif vehicle == "4":
            vehicle = stuff['Vans']
            return vehicle
        elif vehicle == "5":
            vehicle = stuff['Trucks']
            return vehicle
        else:
            print('That Is Not an Option!')


def employee_options():
    pass


def main():
    choice = login()
    inventory = which_file_to_open(choice)
    if choice.upper() == 'U':
        vehicle = user_options(inventory)
        fee_1 = deposit_fee(vehicle)
        print(f'The deposit fee is ${fee_1}')
        days = input('How many days would you like to rent the vehicle?')
        days = int(days)
        fee_2 = total_rental_fee(vehicle, days)
        print(f'The total rental fee is ${fee_2}')
    else:
        employee_options()
    print('Have A Good Day!')


if __name__ == '__main__':
    main()
