from rectangle import rectangle
from circle import circle
import yaml
import json

def main():
    print("Starting  program")
    units = input("What unit of measure? ")

    # Read the rectangles from JSON file
    rectangles = get_rectangles('inputs/rectangle.json')

    # Read the circles from YAML file
    circles = get_circles('inputs/circle.yml')

    # Combine both shape types into one list
    shapes = rectangles + circles

    # Iterate over the shape list using a generator and
    # print out the math data for each shape
    for i, s in enumerate(shapes):
        print('Shape {}'.format(i + 1))
        print(' Type:  {}'.format(s))
        print(' Area:  {0} {1} sq'.format(s.area(), units))
        print(' Perim: {0} {1}\n'.format(s.perimeter(), units))
    print("Finishing program")

def get_circles(filename):
    try:
        handle = open(filename, 'r')
        data = yaml.load(handle)
    except yaml.YAMLError as error:
        print(error)
    finally:
        handle.close()

    circle_objects = []
    for radius in data['circle_list']:
        new_circle = circle(radius)
        circle_objects.append(new_circle)

    return circle_objects

def get_rectangles(filename):
    with open(filename, 'r') as handle:
        try:
            data = json.load(handle)
        except error:
            print(error)

    rectangle_objects = []
    i = 0
    while i < len(data['rectangle_list']):
        current_dict = data['rectangle_list'][i]
        length = current_dict['length']
        width = current_dict['width']
        new_rectangle = rectangle(length, width)
        rectangle_objects.append(new_rectangle)
        i += 1

    return rectangle_objects

if __name__ == "__main__":
    main()
