# Copyright (c) 2016 Ami . All rights reserved

def invest(amount, rate, num_of_years):
    initial_amount = amount

    print("\nPrincipal amount: ", amount)

    print("Annual return rate: ", rate)

    for year in range(1, num_of_years + 1):
        compound_rate = amount * rate
        amount = amount + compound_rate
        print("Year ", num_of_years, ":", amount)

    roi  = amount - initial_amount
    print("You made in {} years ${}".format(num_of_years, roi))

def main():
    invest(100, .05, 8)
    invest(2000, .025, 5)

if __name__ == '__main__':
    main()
