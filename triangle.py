# -*- coding: utf-8 -*-

"""
Updated sept 21, 2022
The primary goal of this file is to demonstrate a simple python program to classify
triangles
@author: Amith vishnu
"""
__author__ = "Amith vishnu"


def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

   
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a - b)):
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'