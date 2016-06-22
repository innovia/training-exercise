# Copyright (c) 2016 Ami . All rights reserved

def invest(initial_amount, interest_rate, duration):
    amount = initial_amount
    print("Principal amount: ", initial_amount)
    print("Annual return rate: ", interest_rate)

    for year in range(1, duration + 1):
        compound_rate = amount * interest_rate
        amount += compound_rate
        print("Year ", year, ":", amount)

    margin = amount - initial_amount
    print("You made in {} years ${}".format(duration, margin))

def main():
    invest(initial_amount=100, interest_rate=.05, duration=8)
    print()
    invest(initial_amount=2000, interest_rate=.025, duration=5)

if __name__ == '__main__':
    main()
