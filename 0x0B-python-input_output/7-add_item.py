#!/usr/bin/python3
"""A script that adds all arguments to a
Python list, and then save them to a file"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    py_list = []

for elm in argv[1:]:
    py_list.append(elm)
save_to_json_file(py_list, filename)
