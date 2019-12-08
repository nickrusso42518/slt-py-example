#!/usr/bin/env python

"""
Author: Nick Russo
File: complete.py
Purpose: Entrypoint for our simple application.
"""

import json
import sys
import yaml
from shapes.rectangle import Rectangle
from shapes.circle import Circle


def main(argv):
    """
    Execution starts here.
    """
    # Get the units from the command line arguments or manually
    # from user input
    units = get_units(argv)

    # Read the rectangles from JSON and circles from YAML
    rectangles = get_rectangles("inputs/rectangle.json")
    circles = get_circles("inputs/circle.yml")

    # Combine both shape types into one list
    general_shapes = rectangles + circles

    # Iterate over the shape list using a 'for' loop.
    # Print out the math data for each shape using
    # a different string formatting method each time.
    for general_shape in general_shapes:
        print("Type:  " + str(general_shape))
        print(" Area:  {0} {1} sq".format(general_shape.area(), units))
        print(f" Perim: {general_shape.perimeter()} {units}\n")

    # Create a list of shapes as dictionaries and write as JSON
    with open("outputs/computations.json", "w") as handle:
        json.dump([gs.to_dict() for gs in general_shapes], handle, indent=4)


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
    # Note that the loop condition is case insensitive
    while units != "cm" and units != "in":
        units = input("Choose unit of measure (cm or in): ")

        # Perform slicing if the user enters too much data
        units = units[:2].lower()

    return units


def get_circles(filename):
    """
    Read in from the YAML file supplied and create
    a list of circles based on the input data.
    """
    try:
        handle = open(filename, "r")
        data = yaml.safe_load(handle)
    except yaml.YAMLError as error:
        print(error)
    finally:
        handle.close()

    # Use a list comprehension to create a new Circle
    # object for each radius integer found in the circle_list.
    circle_objects = [Circle(radius) for radius in data["circle_list"]]

    # Return the list of Circle objects
    return circle_objects


def get_rectangles(filename):
    """
    Read in from the JSON file supplied and create
    a list of rectangles based on the input data.
    """
    with open(filename, "r") as handle:
        try:
            data = json.load(handle)
        except json.decoder.JSONDecodeError as error:
            print(error)
            raise

    # Manually iterate over the JSON dictionaries in the list
    # of rectangles. Create a new Rectangle object for each one
    # and add it to the list.
    rectangle_objects = []
    for rect in data["rectangle_list"]:
        length = rect["length"]
        width = rect["width"]
        new_rectangle = Rectangle(length, width)
        rectangle_objects.append(new_rectangle)

    # Return the list of Rectangle objects
    return rectangle_objects


# If the main.py file was directly run from the shell, invoke
# the main function.
if __name__ == "__main__":
    main(sys.argv)
