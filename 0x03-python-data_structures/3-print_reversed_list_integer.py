#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    [print("{:d}".format(num)) for num in my_list[::-1]]
