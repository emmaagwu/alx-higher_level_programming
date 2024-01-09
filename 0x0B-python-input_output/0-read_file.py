#!/usr/bin/python3
""" Defines a funtion that reads a text """


def read_file(filename=""):
    """ Reads a text file(UTF8) and prints it to stdout

    Argvs:
        filename: this represents file to be opened and read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
