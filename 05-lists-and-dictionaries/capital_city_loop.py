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
            return
        elif response == "exit":
            print("The correct answer is: " + capitals_dict[state])
            print("Goodbye")
            return
        else:
            print("Wrong - try again or type exit to quit")

def check_answer(answer, correct_answer):
    return answer.lower() == correct_answer.lower()

def main():
    state = get_random_state()
    capital_of_state_quiz(state)

if __name__ == "__main__":
    main()
