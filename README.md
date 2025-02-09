# Froots
Froots is a python module to construct the root system of the Feingold-Frenkel 
algebra to arbitrary height.

## Rootsystem
Included in VisualLie is a Python package called **rootsystem**. It constructs
the root system of the Feingold-Frenkel algebra. This package is based on the
SimpLie program written by Teake Nutma, which is available at
https://github.com/teake/simplie.

**rootsystem** requires a Python installation with [NumPy](https://numpy.org/).
**rootsystem** is called with one optional argument from the command line.
The argument is the height up to which the root system will be constructed.
If no argument is given, the calculation defaults to a height of 76.

Upon executing the **rootsystem** package, the root system is automatically
constructed up to the given height and stored as a CSV file in the data/ 
directory. The first three numbers in each row are the root vector and
the last number is the multiplicity of that root.

To run the package type

```
python -m rootsystem [HEIGHT]
```
where [HEIGHT] is the optional argument. It can be either nothing or a 
positive integer.

Note that the root multiplicities are huge numbers. When constructing the
root system of the Feingold-Frenkel algebra for heights > 80, there are
some issues due to dealing with numbers greater than 2^64. This will
hopefully be fixed in a future version.
