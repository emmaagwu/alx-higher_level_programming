#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup_list = my_list[:]
    for i in range(len(dup_list)):
        if dup_list[i] == search:
            dup_list[i] = replace
    return (dup_list)
