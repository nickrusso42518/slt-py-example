'''
Author: Nick Russo
File: main.py
Purpose: Entrypoint for our simple application.
'''

import json
import sys
import yaml
from rectangle import Rectangle
from circle import Circle

def main(argv):
    '''
    Execution starts here.
    '''
    print("Starting  program")
    # Get the units from the command line arguments or manually
    # from user input
    units = get_units(argv)

    # Read the rectangles from JSON file
    rectangles = get_rectangles('inputs/rectangle.json')

    # Read the circles from YAML file
    circles = get_circles('inputs/circle.yml')

    # Combine both shape types into one list
    general_shapes = rectangles + circles

    # Iterate over the shape list using a generator and
    # print out the math data for each shape using # a different string formatting method each time.
    for i, general_shape in enumerate(general_shapes):
        print('Shape ' + str(i + 1))
        print(' Type:  %s' % general_shape)
        print(' Area:  {0} {1} sq'.format(general_shape.area(), units))
        print(f' Perim: {general_shape.perimeter()} {units}\n')

    print("Finishing program")

def get_units(argv):
    '''
    Return the unit of measure, either centimeters (cm) or
    inches (in) based on user input via command line arguments
    or via interactive input collection.
    '''

    # If the user did not specify measurement, use a dummy value
    # to kick off the while loop.
    if len(argv) < 2:
        units = 'dummy'

    # If the user did specify measurement, copy the first value to 'units'
    else:
        units = argv[1][:2].lower()
  
    # Continue to loop until the user enters 'in' or 'cm'
    # Note that the loop condition is case insensitive
    while units.lower() != 'cm' and units.lower() != 'in':
        units = input("Choose unit of measure (cm or in): ")

        # Perform slicing if the user enters too much data
        units = units[:2]

    return units

def get_circles(filename):
    '''
    Read in from the YAML file supplied and create
    a list of circles based on the input data.
    '''
    try:
        handle = open(filename, 'r')
        data = yaml.load(handle)
    except yaml.YAMLError as error:
        print(error)
    finally:
        handle.close()

    circle_objects = [Circle(radius) for radius in data['circle_list']]
    return circle_objects

def get_rectangles(filename):
    '''
    Read in from the JSON file supplied and create
    a list of rectangles based on the input data.
    This function is a generator.
    '''
    with open(filename, 'r') as handle:
        try:
            data = json.load(handle)
        except json.decoder.JSONDecodeError as error:
            print(error)
            raise

    rectangle_objects = []
    for rect in data['rectangle_list']:
        length = rect['length']
        width = rect['width']
        new_rectangle = Rectangle(length, width)
        rectangle_objects.append(new_rectangle)

    return rectangle_objects

if __name__ == "__main__":
    main(sys.argv)
