# Copyright (c) 2016 Ami . All rights reserved

def invest(initial_amount, interest_rate, duration):

    print("\nPrincipal amount: ", initial_amount)

    print("Annual return rate: ", interest_rate)

    for year in range(1, duration + 1):
        compound_rate = initial_amount * interest_rate
        initial_amount += compound_rate

        print("Year ", year, ":", amount)

    roi  = amount - initial_amount

    print("You made in {} years ${}".format(duration, roi))

def main():
    invest(initial_amount=100, interest_rate=.05, duration=8)
    invest(initial_amount=2000, interest_rate=.025, duration=5)

if __name__ == '__main__':
    main()
