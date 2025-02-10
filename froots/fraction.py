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
Froots is python package to construct the root system of the 
Feingold-Frenkel algebra to arbitrary height.

This class defines a fraction of very large integers.
"""

import primefac
import math
from collections import Counter

class Fraction:
    """
    A class for dealing with fractions of very large integers.
    
    Attributes:
        numerator: The numerator
        denominator: The denominator
    """

    def __init__(self, numerator, denominator=1):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.normalize()
        
        if denominator != 1 and numerator != 0:
            self.normalize()
        
    def normalize(self):
        if self.numerator == 0:
            self.denominator = 1
        elif self.denominator != 1:
            _num_fac = Counter(primefac.primefac(self.numerator))
            _denom_fac = Counter(primefac.primefac(self.denominator))
            _gcd = {p: min(_num_fac[p], _denom_fac[p]) for p in _num_fac.keys() & _denom_fac.keys()}
            for p in _gcd:
                _num_fac[p] -= _gcd[p]
                _denom_fac[p] -= _gcd[p]
            self.numerator = math.prod([p**_num_fac[p] for p in _num_fac.keys()])
            self.denominator = math.prod([p**_denom_fac[p] for p in _denom_fac.keys()])    
   
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
        if self.denominator == 1:
            return self.numerator
        else:
           print(f"{self.numerator} / {self.denominator} is not an integer!")
           return 0