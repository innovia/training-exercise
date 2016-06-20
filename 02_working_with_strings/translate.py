# Copyright (c) 2015 Ami. All rights reserved.

def user_input():
    response = input("Enter some text: ")
    return response

def translate(text):
    result = text.replace("a", "4").replace("b", "8").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5").replace("t", "7")

    print(result)

def main():
    response = user_input()
    translate(response.lower())

if __name__ == '__main__':
    main()
