#!/usr/bin/env python

"""
Author: Nick Russo
File: fundamental.py
Purpose: Fundamental techniques demonstration.
"""
import sys
from math import pi


def main(argv):
    """
    Execution starts here.
    """

    # Get the units from the command line arguments or manually
    # from user input
    units = get_units(argv)

    # Create radius list where each element is an integer.
    radius_list = [5, 8, 11]

    # Iterate over each each radius and compute the circle's area.
    for radius in radius_list:
        area = round(pi * (radius ** 2), 2)
        print(f"radius {radius} -> area {area} {units} sq")

    # Iterate again, except use a dangerous and error-prone technique.
    # Notice that the previous loop is simpler and risk-free.
    for i in range(len(radius_list) + 0):
        try:
            radius = radius_list[i]
        except IndexError as exc:
            print("Hmm, are we off by 1 somewhere? " + str(exc))
            raise

        perim = round(pi * radius * 2, 2)
        print(f"radius {radius} -> perim {perim} {units}")

    # Create rectangle dictionary where key is a string and value
    # is a 2-tuple of length and width integers, respectively.
    rectangle_dict = {
        "rectangle1": (8, 2),
        "rectangle2": (3, 3),
        "rectangle3": (1, 6),
    }

    # Iterate over each dictionary item, including the key and the value,
    # and compute the rectangle's area.
    for key, val in rectangle_dict.items():
        length = val[0]
        width = val[1]
        area = length * width
        perim = (length + width) * 2
        print(key)
        print(f" {length}x{width} -> area {area} {units} sq")
        print(f" ({length}+{width})x2 -> perim {perim} {units}")


def get_units(argv):
    """
    Return the unit of measure, either centimeters (cm) or
    inches (in) based on user input via command line arguments
    or via interactive input collection.
    """

    # If the user did not specify measurement, use a dummy value
    # to kick off the while loop.
    if len(argv) < 2:
        units = "dummy"

    # If the user did specify measurement, copy the first value to 'units'
    else:
        units = argv[1][:2].lower()

    # Continue to loop until the user enters 'in' or 'cm'
    while units != "cm" and units != "in":
        units = input("Choose unit of measure (cm or in): ")

        # Perform slicing if the user enters too much data
        # Note that the loop condition becomes case insensitive
        units = units[:2].lower()

    return units


# If the main.py file was directly run from the shell, invoke
# the main function. See the following files for more info:
#   - small/testmod.py
#   - small/namemain.py
if __name__ == "__main__":
    main(sys.argv)
