#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, mul, div, sub
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]

    a = int(argv[1])
    b = int(argv[3])

    if op == '+':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, add(a, b)))
    elif op == '-':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, sub(a, b)))
    elif op == '*':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, mul(a, b)))
    elif op == '/':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
