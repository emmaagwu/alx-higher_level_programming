#!/usr/bin/python3
""" Defines a function that adds all arguments to a Python List """
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file
    items = load_from_json_file("add_item.json")
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
