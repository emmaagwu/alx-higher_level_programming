#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key = list(a_dictionary.keys())[0]
    high = a_dictionary[key]
    for i, j in a_dictionary.items():
        if j > high:
            high = j
            key = i
    return (key)
