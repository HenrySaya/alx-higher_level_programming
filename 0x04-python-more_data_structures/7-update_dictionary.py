#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    a_dictionary[key] = value

    for k, v in a_dictionary.items():
        a_dictionary[key] = value
        if k == key:
            a_dictionary[key] = value

    return a_dictionary
