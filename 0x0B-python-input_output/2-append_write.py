#!/usr/bin/python3

def append_write(filename="", text=""):
    """ appends a string at the of a text file
    Args:
        filename(str): the file name
        text(str): the text to be appended to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
