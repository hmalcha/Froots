#!/usr/bin/env python4

# This file is part of Froots.
#
# Copyright (C) 2024 Hannes Malcha
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

"""
Froots is a Python package to construct the root system of the 
Feingold-Frenkel algebra to arbitrary height

This is the __main__.py file of the Froots package that constructs
the root system of the Feingold-Frenkel algebra.

The package is called with one optional argument from the command line.
The argument is the height up to which the root system will be constructed.
If no argument is given the calculation defaults to a height of 76.

Upon executing the Froots package the root system is automatically 
constructed up to the given height and stored as a csv file in the 
current directory. The first three numbers in each row are the root 
vector and the last number is the multiplicity of that root.
"""

import argparse
import time
from .feingold_frenkel_algebra import Feingold_Frenkel_Algebra
from .root_system import Root_System

def _check_positive(value):
        """Check if the argument given to the parser is a positive int."""
        _value = int(value)
        if _value <= 0:
                raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return _value


def _parse_argument():
        """
        Parse an argument from the user or resort to default if 
        no argument is given.
        """
        
        _parser = argparse.ArgumentParser(description="Construct the root system.")
        _parser.add_argument("height", metavar="h", nargs="?", const=76, default=76, 
                             type=_check_positive,
                             help="The height up to which the root system will be constructed.")
        
        return _parser.parse_args()


def main():
        """
        This is the main function that is executed when the rs_constructor
        package is called from the command line.
        
        The main function creates a root system of the Feingold-Frenkel
        algebra, constructs it up to the given height and saves it to
        a file.
        """
        
        # Record the time when the function is called
        _start_time = time.time()
        
        # Define the algebra and the root system
        _algebra = Feingold_Frenkel_Algebra()
        _root_system = Root_System(_algebra)
        _height = _parse_argument().height
        
        # Print a status message
        print("Constructing the root system up to height " + str(_height))
        
        # Construct the root system and save it to a file
        _root_system.construct(_height)      
        _root_system.write_txt_file("roots.txt")
        
        # Write completion message
        _end_time = round(time.time() - _start_time)
        print("Construction completed in " + str(_end_time) + " seconds")
        

if __name__ == "__main__":
        main()
