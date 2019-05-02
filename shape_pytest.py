"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""
import pytest
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import Triangle


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


def test_triangle():
    """
    Defines tests on some specific triangle objects.
    """
    a3b3c3 = Triangle(3, 3, 3)
    a3b4c5 = Triangle(3, 4, 5)
    a4b4c5 = Triangle(4, 4, 5)
    a5b4c8 = Triangle(5, 4, 8)
    a2b4c8 = Triangle(2, 4, 8)
    a2b6c8 = Triangle(2, 6, 8)

    assert a3b3c3.area() == 3.9
    assert a3b4c5.area() == 6.0
    assert a4b4c5.area() == 7.81
    assert a5b4c8.area() == 8.18
    assert a2b6c8.area() == 0
    assert a3b3c3.perimeter() == 9
    assert a3b4c5.perimeter() == 12
    assert a4b4c5.perimeter() == 13
    assert a5b4c8.perimeter() == 17
    assert a2b4c8.perimeter() == 14
    assert a2b6c8.perimeter() == 16

    assert a4b4c5.is_isosceles()
    assert not a3b3c3.is_isosceles()
    assert not a3b4c5.is_isosceles()
    assert not a5b4c8.is_isosceles()
    assert not a2b4c8.is_isosceles()
    assert not a2b6c8.is_isosceles()

    assert a3b3c3.is_equilateral()
    assert not a3b4c5.is_equilateral()
    assert not a4b4c5.is_equilateral()
    assert not a5b4c8.is_equilateral()
    assert not a2b4c8.is_equilateral()
    assert not a2b6c8.is_equilateral()

    with pytest.raises(ValueError):
        a2b4c8.area()
