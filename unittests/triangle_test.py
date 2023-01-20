"""
Author: Nick Russo
File: triangle_test.py
Purpose: Unit tests for the Rectangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Rectangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.a2b2c2 = Triangle(2, 2, 2)
        self.a3b4c4 = Triangle(3, 4, 4)
        self.a4b5c6 = Triangle(4, 5, 6)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.a2b2c2.area(), 1.73)
        self.assertEqual(self.a3b4c4.area(), 5.56)
        self.assertEqual(self.a4b5c6.area(), 9.92)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.a2b2c2.perimeter(), 6)
        self.assertEqual(self.a3b4c4.perimeter(), 11)
        self.assertEqual(self.a4b5c6.perimeter(), 15)

    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is an equilateral
        """
        self.assertTrue(self.a2b2c2.is_equilateral())
        self.assertFalse(self.a3b4c4.is_equilateral())
        self.assertFalse(self.a4b5c6.is_equilateral())

    def test_is_isoceles(self):
        """
        Confirm or deny if the triangle is an isoceles.
        """
        self.assertTrue(self.a2b2c2.is_isoceles())
        self.assertTrue(self.a3b4c4.is_isoceles())
        self.assertFalse(self.a4b5c6.is_isoceles())
