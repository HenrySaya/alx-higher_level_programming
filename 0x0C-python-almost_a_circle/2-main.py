#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id) # 1

    r1 = Rectangle(10, 92)
    print(r1.id) # 2

    r1 = Rectangle(10, 2, 0, 0 , 110)
    print(r1.id) # 110
