# Froots
**Froots** is a python package to construct the root system
of the Feingold-Frenkel algebra to arbitrary height.

**Froots** is based on the
SimpLie program written by Teake Nutma, which is available at
https://github.com/teake/simplie. **Froots** extends the
scope of SimpLie by enabling the calculation of roots with
arbitrary height. This is achieved through the implementation
of custom classes for handling very large integers and
fractions.

## Usage
**Froots** requires a Python 3 installation with 
[NumPy](https://numpy.org/).
**Froots** is called with one optional argument from the
command line. The argument is the heigh up to which the root
system will be constructed. If no argument is given, the calculation
defaults to a height of 76.

The output is stored as a .txt file in the current directory.
The first three numbers in each row are the root vector and
the last number is the multiplicity of that root.

To run the package type

```
python3 -m froots [HEIGHT]
```
where [HEIGHT] is the optional argument. It can be either nothing or a 
positive integer.

## Output
The file **roots.txt** contains the roots of the Feingold-Frenkel
algebra up to height 100. It takes about 6 minutes to generate
this file. The file **roots_250.txt** contains all roots of the
Feingold-Frenkel algebra up to height 250. It took 72 hours to
generate this file. Similarly **roots_300.txt** contains all
roots up to height 300. These are about half a million roots.

## License
Copyright © 2025 Hannes Malcha

Froots is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Froots is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Froots. If not, see https://www.gnu.org/licenses/.
