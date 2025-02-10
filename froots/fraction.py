#!/usr/bin/env python3

# This file is part of Froots.
#
# Copyright (C) 2025 Hannes Malcha 
#
# Froots is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Froots is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Froots. If not, see <https://www.gnu.org/licenses/>.
#
#
# This class is an exact copy of the Root class from the SimpLie programm
# written by Teake Nutma, which is available at
# https://github.com/teake/simplie.

"""
Froots is a Python package to construct the root system of the 
Feingold-Frenkel algebra to arbitrary height.

This class defines a fraction of very large integers.
"""

import math

class Fraction:
    """
    A class for dealing with fractions of very large integers.
    
    Attributes:
        numerator: The numerator
        denominator: The denominator
    """

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.normalize()
        
  
    def normalize(self):
        """
        Normalize the fraction.
        """
        if self.numerator == 0:
            self.denominator = 1
        elif self.denominator != 1:
            _gcd = math.gcd(self.numerator, self.denominator)
            self.numerator = self.numerator // _gcd
            self.denominator = self.denominator // _gcd
            
    def add(self, fraction):
        """
        Add a fraction to this one.
        """
        _numerator = self.numerator*fraction.denominator + fraction.numerator*self.denominator
        _denominator = self.denominator * fraction.denominator
        return Fraction(_numerator, _denominator)

    def subtract(self, fraction):
        """
        Subtract a fraction from this one.
        """
        _numerator = self.numerator*fraction.denominator - fraction.numerator*self.denominator
        _denominator = self.denominator * fraction.denominator
        return Fraction(_numerator, _denominator)


    def multiply(self, fraction):
        """
        Multiply a fraction to this one.
        """
        _numerator = self.numerator * fraction.numerator
        _denominator = self.denominator * fraction.denominator
        return Fraction(_numerator, _denominator)
    
    def times(self, n):
        """
        Multiply a number to this fraction.
        """
        return Fraction(self.numerator * n, self.denominator)

    def toInt(self):
        """
        Return an integer.
        
        This is only called when it is known that the Fraction must be an integer.
        """
        if self.denominator == 1:
            return self.numerator
        elif self.denominator == -1:
            return -self.numerator
        # If this error is ever raised something is wrong with the calculation
        # of the root system.
        raise ValueError(f"{self.numerator} / {self.denominator} is not an integer!")