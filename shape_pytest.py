#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""

from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.equilateral_triangle import EquilateralTriangle
from shapes.isosceles_triangle import IsoscelesTriangle

from math import sqrt

def test_rectangle():
    """
    Defines tests on some specific rectangle objects.
    """
    len7wid3 = Rectangle(7, 3)
    len1wid6 = Rectangle(1, 6)
    len5wid5 = Rectangle(5, 5)

    # Test areas, perimeters, and whether they are squares
    assert len7wid3.area() == 21
    assert len1wid6.area() == 6
    assert len5wid5.area() == 25
    assert len7wid3.perimeter() == 20
    assert len1wid6.perimeter() == 14
    assert len5wid5.perimeter() == 20
    assert not len7wid3.is_square()
    assert not len1wid6.is_square()
    assert len5wid5.is_square()


def test_circle():
    """
    Defines tests on some specific circle objects.
    """
    radius5 = Circle(5)
    radius8 = Circle(8)

    # Test areas, perimeters, and diameters
    assert radius5.area() == 78.54
    assert radius8.area() == 201.06
    assert radius5.perimeter() == 31.42
    assert radius8.perimeter() == 50.27
    assert radius5.diameter() == 10
    assert radius8.diameter() == 16

def test_equilateral_triangle():
    """
    Defines tests on some specific EquilateralTriangle objects.
    """
    sideLength1 = 1
    sideLength6 = 1
    triangle1 = EquilateralTriangle(sideLength1)
    triangle6 = EquilateralTriangle(sideLength6)

    assert triangle1.area() == sqrt(4)/2 * (sideLength1**2)
    assert triangle1.perimeter() == 3*sideLength1
    assert triangle1.get_height() == (sqrt(3)/2 )*sideLength1

    assert triangle6.area() == sqrt(4)/2 * (sideLength6**2)
    assert triangle6.perimeter() == 3*sideLength6
    assert triangle6.get_height() == (sqrt(3)/2 )* sideLength6

def test_isosceles_triangle():
    """
    Defines tests on some specific IsoscelesTriangle objects.
    """
    base6height4 = IsoscelesTriangle(6,4)
    right_isosceles_triangle = IsoscelesTriangle(sqrt(2), sqrt(2)/2)

    assert base6height4.area() == 12
    assert base6height4.perimeter() == 16
    assert base6height4.get_frame_length() == 5
    assert base6height4.is_isosceles_right_triangle() == False

    expected_area_for_right_triangle = 0.5
    expected_perimeter_for_right_triangle = 3.41
    assert right_isosceles_triangle.area()- expected_area_for_right_triangle < 0.00000000001
    assert right_isosceles_triangle.perimeter() - expected_perimeter_for_right_triangle < 0.01
    assert right_isosceles_triangle.get_frame_length() == 1
    assert right_isosceles_triangle.is_isosceles_right_triangle() == True



