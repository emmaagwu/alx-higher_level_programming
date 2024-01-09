#!/usr/bin/python3

def write_file(filename="", text=""):
    """ Writes a strig to a file
    Argv:
        filename: the file to be written
        text: the text to be written on the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        no_of_char_written = f.write(text)
        return no_of_char_written
