#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    calcs = [add, sub, mul, div]
    for i, s in enumerate(ops):
        if sys.argv[2] == s:
            print("{} {} {} = {}".format(a, s, b, calcs[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
