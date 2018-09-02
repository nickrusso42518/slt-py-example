'''
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
'''

from shapes.rectangle import Rectangle
from shapes.circle import Circle

def test_rectangle():
    '''
    Defines tests on some specific rectangle objects.
    '''
    len7wid3 = Rectangle(7, 3)
    len1wid6 = Rectangle(1, 6)
    len5wid5 = Rectangle(5, 5)

    # Test areas
    assert len7wid3.area() == 21
    assert len1wid6.area() == 6
    assert len5wid5.area() == 25

    # Test perimeters
    assert len7wid3.perimeter() == 20
    assert len1wid6.perimeter() == 14
    assert len5wid5.perimeter() == 20

    # Test for squares
    assert not len7wid3.is_square()
    assert not len1wid6.is_square()
    assert len5wid5.is_square()

def test_circle():
    '''
    Defines tests on some specific circle objects.
    '''
    radius5 = Circle(5)
    radius8 = Circle(8)

    # Test areas
    assert radius5.area() == 78.54
    assert radius8.area() == 201.06

    # Test perimeters (circumferences)
    assert radius5.perimeter() == 31.42
    assert radius8.perimeter() == 50.27

    # Test diameters
    assert radius5.diameter() == 10
    assert radius8.diameter() == 16
