#!/usr/bin/python3

def text_indentation(text):
    """
    handles more than one space atm
    """
    flag = 0
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            flag = 1
        elif flag == 1 and char == " ":
            continue
        else:
            print(char, end="")
            flag = 0
    print()

