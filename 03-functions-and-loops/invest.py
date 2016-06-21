# Copyright (c) 2016 Ami . All rights reserved

def invest(amount, interest_rate, duration):
    initial_amount = amount

    print("\nPrincipal amount: ", amount)

    print("Annual return rate: ", interest_rate)

    for year in range(1, duration + 1):
        compound_rate = amount * interest_rate
        amount = amount + compound_rate
        print("Year ", duration, ":", amount)

    roi  = amount - initial_amount
    print("You made in {} years ${}".format(duration, roi))

def main():
    invest(100, .05, 8)
    invest(2000, .025, 5)

if __name__ == '__main__':
    main()
