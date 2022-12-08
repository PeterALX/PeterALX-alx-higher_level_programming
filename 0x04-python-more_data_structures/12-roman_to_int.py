#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or isinstance(roman_string, str) == False:
        return 0
    else:
        roman_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(roman_string)):
            if i > 0 and roman_[roman_string[i]] > roman_[roman_string[i - 1]]:
                num += roman_[roman_string[i]] - 2 * roman_[roman_string[i - 1]]
            else:
                num += roman_[roman_string[i]]
        return(num)
