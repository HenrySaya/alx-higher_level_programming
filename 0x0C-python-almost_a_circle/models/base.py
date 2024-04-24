#!/usr/bin/python3
"""Defines a base superclass"""


class Base:
    """Represent the base class."""

    __nb_objects = 0  # Private class variable

    def __init__(self, id=None):
        """ Initialize the base class

        Args:
            id (iint): id of the base class
        """

        if id is not None:
            self.id = id  # Assign id if provided
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # __nb_objects value as id
