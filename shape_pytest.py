#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""

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
    a2b2c2 = Triangle(2, 2, 2)
    a3b4c4 = Triangle(3, 4, 4)
    a4b5c6 = Triangle(4, 5, 6)

    assert a2b2c2.area() == 1.73
    assert a3b4c4.area() == 5.56
    assert a4b5c6.area() == 9.92
    assert a2b2c2.perimeter() == 6
    assert a3b4c4.perimeter() == 11
    assert a4b5c6.perimeter() == 15
    assert a2b2c2.is_equilateral()
    assert not a3b4c4.is_equilateral()
    assert not a4b5c6.is_equilateral()
    assert a2b2c2.is_isoceles()
    assert a3b4c4.is_isoceles()
    assert not a4b5c6.is_isoceles()
