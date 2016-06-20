# Copyright (c) 2016 Ami . All rights reserved.

def get_user_password():
    password = input("Tell me your password: ")
    if not password:
        get_user_password()
    return password

def show_first_capital_letter(password):
    first_capital_letter = get_first_letter_of(password).upper()
    print("The first (capital) letter you entered was: " + first_capital_letter)

def get_first_letter_of(text):
    return text[0]

def main():
    password = get_user_password()
    show_first_capital_letter(password)

if __name__ == '__main__':
    main()
