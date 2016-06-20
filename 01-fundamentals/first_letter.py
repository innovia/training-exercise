# Copyright (c) 2016 Ami . All rights reserved.

def get_user_password():
    password = input("Tell me your password:")
    return password

def show_first_letter_of(password):
    first_letter = get_first_letter_of(password)
    print("The first letter you entered was: " + first_letter)

def get_first_letter_of(text):
    return text[0].upper()

def main():
    password = get_user_password()
    show_first_letter_of(password)

if __name__ == '__main__':
    main()
