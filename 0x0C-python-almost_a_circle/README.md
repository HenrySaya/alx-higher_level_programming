0x0C-python-almost_a_circle
=================================================

#Python - almost a circle

In this particular projectI reviewed everythin about Python.This was a great project that addressed everythin in Python and thus sharpening my skills.In conjuction with previous knowledge of the Python concepts I had a better understandin of Serialization/Deserialization which all coupled up with application of args and kwargs. 
The project required test driven development and implemented unittesting on the various scripts and packages.I had much fun contributing to this project.

##Tasks :
* **1. Base class**
 * [__init__.py]: This is an empty file and with this file the folder becomes a Python package
 * [base.py] : Python program with private class attribute __nb_objects and a class constructor. This class is the base of all other classes in the project.
 * Goal: Manage id attribute in all my future classes and to avoid duplicating the same code  amd by extension some bugs

* **2. First Rectangle
 * [rectangle.py]: This is the class Rectangle that inherits from Base. It contains private instance attributes with its own public getter and setter methods. I used private attributes with getter/setter and not public attributes because I wanted to protect attributes of our class.With a setter I (you too) am able to validate what a user is trying to assigne to a variable.So after, in the class I can 'trust' these attributes
