# Copyright (c) 2016 Ami . All rights reserved.


def user_input():
    password = input("Tell me your password:")

    print("The first letter you entered was: " + password[0].upper())


def main():
    user_input()


if __name__ == '__main__':
  main()
