#!/usr/bin/env python

"""
Author: Nick Russo
File: rectangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains 3 length values - sidea, sideb and sidec
    """

    def __init__(self, sidea, sideb, sidec):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        self.sep = float(0)
        self.decimal_places = 2

    def area(self):
        """
        Compute the area using the formula:
        If a, b and c are ithe sides of a triangle. Then,
        s = (a+b+c)/2
        area = √(s(s-a)*(s-b)*(s-c))
        """
        self.sep = (self.sidea + self.sideb + self.sidec) / 2
        return round(
            (self.sep * (self.sep - self.sidea) * (self.sep - self.sideb) * (self.sep - self.sidec))
            ** 0.5,
            self.decimal_places,
        )

    def perimeter(self):
        """
        Compute the perimeter using the formula (a + b + c)
        """
        return self.sidea + self.sideb + self.sidec

    def is_equilateral(self):
        """
        Determine if the Triangle is an equilateral by comparing the lengths a, b and c
        for equality. Only triangles can be equilateral.
        """
        return self.sidea == self.sideb == self.sidec

    def is_isoceles(self):
        """
        Determine if the Triangle is an equilateral by comparing the lengths a, b and c
        for 2 being equal. Only triangles can be isoceles.
        """
        return (
            self.sidea == self.sideb or self.sideb == self.sidec or self.sidea == self.sidec
        ) and not self.sidea == self.sideb == self.sidec
