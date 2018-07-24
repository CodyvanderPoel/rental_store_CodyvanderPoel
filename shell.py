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


def main():
    choice = login()


if __name__ == '__main__':
    main()
