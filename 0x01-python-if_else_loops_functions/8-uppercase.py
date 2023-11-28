#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            str_upper = chr(ord(i) - 32)
            result += str_upper
        else:
            result += i;
    print("{}".format(result))
