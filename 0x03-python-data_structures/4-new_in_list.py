#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for num in my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        new_list = list(my_list)
        new_list[idx] = element
        return new_list
