#!/usr/bin/python3

"""class student be up in here"""


class Student:
    """the student class be I and I rastafari"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {k: v for (k, v) in self.__dict__ if k in attrs}
