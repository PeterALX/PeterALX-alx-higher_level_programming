#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    print(r1)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    print(r2)
    r2.display()
