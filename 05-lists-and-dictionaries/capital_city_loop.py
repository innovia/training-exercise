# Copyright (c) 2016 Ami . All rights reserved

from capitals import capitals_dict
from random import choice

def get_random_state():
    return choice(list(capitals_dict.keys()))

def capital_of_state_quiz(state):
    while True:
        response = input("What is the capital of " + state + "? ").lower()

        if response == capitals_dict[state].lower():
            print("Correct")
            return True
        elif response == "exit":
            print("Goodbye")
            exit(0)
        else:
            print("Wrong - try again or type exit to quit")
            return capital_of_state_quiz(state)

def main():
    state = get_random_state()
    capital_of_state_quiz(state)

if __name__ == "__main__":
    main()
