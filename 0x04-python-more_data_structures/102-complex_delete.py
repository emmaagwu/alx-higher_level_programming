#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for ke, va in a_dictionary.items():
            if va == value:
                del a_dictionary[ke]
                break

    return (a_dictionary)
