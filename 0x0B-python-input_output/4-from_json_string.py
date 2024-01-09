#!/usr/bin/python3
""" defines a function that returns an object from JSON """
import json


def from_json_string(my_str):
    """ Returns an object from a JSON string """
    return json.loads(my_str)
