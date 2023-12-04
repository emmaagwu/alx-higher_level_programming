#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    duplicate_list = my_list.copy()
    list_length = len(my_list)
    if idx < 0 or idx > list_length:
        return duplicate_list
    else:
        duplicate_list[idx] = element
        return duplicate_list
