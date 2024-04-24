#!/usr/bin/python3
"""Defines a base superclass"""

class Base:
    """Represent the base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base class

        Args:
            id (iint): id of the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
