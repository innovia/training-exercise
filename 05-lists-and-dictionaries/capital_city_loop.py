# Copyright (c) 2016 Ami . All rights reserved

from capitals import capitals_dict
from random import choice

def get_random_state():
    return choice(list(capitals_dict.keys()))

def capital_of_state_quiz(state):
    while True:
        response = input("What is the capital of " + state + "? ").lower()

        if check_answer(response, capitals_dict[state]):
            print("Correct")
            return True
        elif response == "exit":
            print("Goodbye")
            return True
        else:
            print("Wrong - try again or type exit to quit")
            return capital_of_state_quiz(state)

def check_answer(answer, correct_answer):
    if answer.lower() == correct_answer.lower():
        return True

def main():
    state = get_random_state()
    capital_of_state_quiz(state)

if __name__ == "__main__":
    main()
