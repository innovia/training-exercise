# Copyright (c) 2015 Ami. All rights reserved.

def user_input():
    response = input("Enter some text: ")
    translate(response.lower())

def translate(text):
    result = text.replace("a", "4").replace("b", "8").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5").replace("t", "7")

    print(result)

def main():
    user_input()

if __name__ == '__main__':
    main()
