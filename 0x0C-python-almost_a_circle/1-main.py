#!/usr/bin/python3
"""1-main"""
from models.base import Base

if __name__ == "__main__":
    b1 = Base()  # OUTPUTS
    print(b1.id) #  1 

    b2 = Base()
    print(b2.id)  # 2

    b3 = Base()
    print(b3.id)  # 3

    b4 = Base(110)
    print(b4.id)  # 110

    b5 = Base()
    print(b5.id)  # 4
