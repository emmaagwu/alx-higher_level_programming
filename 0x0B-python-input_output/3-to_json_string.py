#!/usr/bin/python3
""" Defines a function that returns the JSON rep of an object """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object
    Args:
        my_obj: the object to be representated
    """

    return json.dumps(my_obj)
