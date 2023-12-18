#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list.
    """
    i = 0
    if x == 0:
        return (0)
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return (i)
