from core import *
from disk import *


def login():
    while True:
        choice = input("[U]ser or [E]mployee or [L]eave:")
        if choice.upper() == 'U':
            print("Welcome To Cody's Car Rental!")
            return choice
        elif choice.upper() == 'E':
            print("Welcome to Cody's Car Rental database!")
            return choice
        elif choice.upper() == 'L':
            print("Have A Good Day!")
            exit()
        else:
            print("The option you have chosen is not available!")


def user_options(choice, contents):
    print(
        "These are our current available vehicles:\n1--Sedans\n2--SUVS\n3--Minivans\n4--Vans\n5--Trucks"
    )
    while True:
        vehicle = input("Now what would you like to rent?")
        if vehicle == "1":
            pass
        elif vehicle == "2":
            pass
        elif vehicle == "3":
            pass
        elif vehicle == "4":
            pass
        elif vehicle == "5":
            pass
        else:
            pass


def main():
    choice = login()
    stuff = which_file_to_open(choice)
    print(stuff)


if __name__ == '__main__':
    main()
