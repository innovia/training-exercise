# Copyright (c) 2016 Ami . All rights reserved

def get_a_positive_integer_from_user():
    response = int(input("Enter a positive integer: "))
    if not response:
        return get_a_positive_integer_from_user()

    return response

def print_divisors_of_integer(integer):
    for i in range(1, integer + 1):
        if integer % i == 0:
            print(i, "is a divisor of", integer)

def main():
    num = get_a_positive_integer_from_user()
    print_divisors_of_integer(num)

if __name__ == '__main__':
    main()
