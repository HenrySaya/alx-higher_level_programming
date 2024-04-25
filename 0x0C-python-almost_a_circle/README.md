0x0C-python-almost_a_circle
=================================================

# Python - almost a circle

In this particular projectI reviewed everythin about Python.This was a great project that addressed everythin in Python and thus sharpening my skills.In conjuction with previous knowledge of the Python concepts I had a better understandin of Serialization/Deserialization which all coupled up with application of args and kwargs. 
The project required test driven development and implemented unittesting on the various scripts and packages.I had much fun contributing to this project.

## Tests :heavy_check_mark:
* [tests]: Folder of test files. Includes unittests.

## Tasks :page_with_curl:
* **1. Base class**
  * [__init__.py](./models/__init__.py): This is an empty file and with this file the folder becomes a Python package
  * [base.py](./models/base.py) : Python program with private class attribute __nb_objects and a class constructor. This class is the base of all other classes in the project.
  * [1-main.py](./1-main.py): This is a sample of tests to run our scripts
  * Goal: Manage id attribute in all my future classes and to avoid duplicating the same code  amd by extension some bugs

* **2. First Rectangle**
  * [rectangle.py](./models/rectangle.py): Python class that defines a rectangle.The class `class Rectangle(Base):` Inherits  from [base.py](./models/base.py) with:
	* Private instance attribute `width`
	* Property getter `def width(self):` to get `width`
	* Property setter `def width(self, value):` to set `width`
        * Private instance attribute `height`
        * Property getter `def height(self):` to get `height`
        * Property setter `def height(self, value):` to set `height`
        * Private instance attribute `x`
        * Property getter `def x(self):` to get `x`
        * Property setter `def x(self, value):` to set `x`
        * Private instance attribute `y`
        * Property getter `def y(self):` to get `y`
        * Property setter `def y(self, value):` to set `y`
	* Instantiation with optional `x`, `y`, and `id`: `def __init__(self, width, height, x=0, y=0, id=None):`
	* Goal: Use private attributes with getter/setter methods to protext attributes of our class. With a setter you are able to validate what a developer is trying to assign to a variable. So after you can ``trust`` these attributes
  * [2-main.py](./2-main.py): This includes inputs that test the class and return the id.

* **3. Validate attributes**
  * [rectangle.py](./models/rectangle.py): Python class that defines a rectangle. An update to the script for attribute validation whereby:
	* If either of the inputs(`width`, `height`, `x`, and `y`) is not an integer, a `TypeError` is raised with the message `<name of the attribute> must be an integer`
	* if either `width` or `height` is under or equals 0, a `ValueError` is raised with the message `<name of the attribute> must be > 0` Example `width must be > 0`
	* if either `x` or `y` is under 0, a `ValueError` is raised with the message `<name of the attribute> must be >= 0` must be >= 0`
  * [3-main.py](./3-main.py): This file verifies the validation by giving inputs and testing our class.

* **4. Area first**
  * [rectangle.py](./models/rectangle.py): Update the class `Rectangle` by adding the public method `def area(self):` that returns the area of the `Rectangle` instance
  * [4-main.py](./4-main.py): Short script that invokes public method `def area(self):` after feeding it with the inputs of the `width` and `height` attributes.
