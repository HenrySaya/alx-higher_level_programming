#!/usr/bin/python3
"""Defines a file_append function"""


def append_write(filename="", text+=""):
    """ Append a string to the end of text file
        Args:
            filename (string): The name of the text file
            text (string): Text to be appended

        Returns:
            The number of characters added
    """
    with open(filename , 'a', encoding='utf-8') as f:
        return f.write(text)
