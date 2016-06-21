# Copyright (c) 2016 Ami. All rights reserved.

def user_input():
    response = input("Enter some text: ")
    return response

def translate(text):
    new_text = text
    dictionary = {
        "a": "4",
        "b": "8",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }

    for char in dictionary:
        new_text = new_text.replace(char, dictionary[char])

    return new_text

def main():
    response = user_input()
    result = translate(response.lower())
    print(result)

if __name__ == '__main__':
    main()
