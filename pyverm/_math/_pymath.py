#=======================================================================
#=======================================================================
#  _____                                      _                     _
# |_   _|                                    | |                   | |
#   | |    _ __ ___    _ __     ___    _ __  | |_    __ _   _ __   | |_
#   | |   | '_ ` _ \  | '_ \   / _ \  | '__| | __|  / _` | | '_ \  | __|
#  _| |_  | | | | | | | |_) | | (_) | | |    | |_  | (_| | | | | | | |_
# |_____| |_| |_| |_| | .__/   \___/  |_|     \__|  \__,_| |_| |_|  \__|
#                     | |
#                     |_|
#=======================================================================
#
# This file is only a facade for the built in math module, but it returns
# always an Decimal types
#
#=======================================================================
#=======================================================================


########################################################################
#                                                                      #
# Copyright (C) 2018,  Marius Hürzeler                                 #
#                                                                      #
# This file is part of PyVerm.                                         #
#                                                                      #
# PyVerm is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# PyVerm is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                      #
########################################################################
"""
decimal math stores the functions to make precise math with decimals
"""
import math as standard_math
from ._pydecimal import Decimal


__all__ = [
    'ceil', 'copysign', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
    'gcd', 'ldexp', 'modf', 'remainder', 'sign', 'signt', 'exp',
    'expm1', 'log', 'log1p', 'log2', 'log10', 'pow', 'sqrt', 'acos', 'asin',
    'atan', 'atan2', 'cos', 'hypot', 'sin', 'tan',
    'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh',
    'pi'
]


pi = Decimal(standard_math.pi)

def acos(x):
    """Return the arc cosine (measured in radians) of x."""

    return Decimal(standard_math.acos(x))


def asin(x):
    """Return the arc sine (measured in radians) of x."""

    return Decimal(standard_math.asin(x))


def atan(x):
    """Return the arc tangent (measured in radians) of x."""
    return Decimal(standard_math.atan(x))


def atan2(y, x):
    """Return the arc tangent (measured in radians) of y/x.
    Unlike atan(y/x), the signs of both x and y are considered."""
    return Decimal(standard_math.atan2(y, x))


def cos(x):
    """Return the cosine of x as measured in radians."""
    return Decimal(standard_math.cos(x))


def hypot(x, y):
    """Return the Euclidean distance, sqrt(x*x + y*y)."""
    return Decimal(standard_math.hypot(x, y))


def sin(x):
    """Return the sine of x as measured in radians."""
    return Decimal(standard_math.sin(x))


def tan(x):
    """Return the tangent of x (measured in radians)."""
    return Decimal(standard_math.tan(x))

def exp(x):
    """Return e raised to the power of x."""
    return Decimal(standard_math.exp(x))


def expm1(x):
    """Return e raised to the power of x, minus one."""
    # Decimal handles this perfecly so no need for complexity
    return Decimal(standard_math.expm1(x))


def log(x, base=None):
    """log(x[, base]) -> the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x."""
    return Decimal(standard_math.log(x, base=None))


def log1p(x):
    """Return the natural logarithm of 1+x (base e)."""
    # Decimal handles this perfecly so no need for complexity.
    return Decimal(standard_math.log1p(x))


def log2(x):
    """log2(x) -> the base 2 logarithm of x."""
    return Decimal(standard_math.log2(x))


def log10(x):
    """log10(x) -> the base 10 logarithm of x."""
    return Decimal(standard_math.log10(x))


def pow(x, y):
    """Return x raised to the power y."""
    return Decimal(standard_math.pow(x, y))


def sqrt(x):
    """Return the square root of x."""
    return Decimal(standard_math.sqrt(x))


# Number-theoretic and representation functions


def ceil(x):
    """Return the smallest integral value >= x."""
    return Decimal(standard_math.ceil(x))


def copysign(x, y):
    """Return a Decimal with the magnitude (absolute value) of x but the sign of
       y. On platforms that support signed zeros, copysign(1.0, -0.0)
       returns -1.0."""
    return Decimal(standard_math.copysign(x, y))


def fabs(x):
    """Return the absolute value of x."""
    return Decimal(standard_math.fabs(x))

def factorial(x):
    """Return x factorial. Raises ValueError if x is not integral or is
       negative."""
    return Decimal(standard_math.factorial(x))


def floor(x):
    """Return the largest integral value <= x."""
    return Decimal(standard_math.floor(x))


def fmod(x, y):
    """Returns the remainder of x and y, using the remainder_near() function
       in Decimal, which comes close to the function in the math library"""
    return Decimal(standard_math.fmod(x, y))


def frexp(x):
    """Return the mantissa and exponent of x as the pair (m, e). m is a Decimal
       and e is an integer such that x == m * 2**e exactly. If x is zero,
       returns (0.0, 0), otherwise 0.5 <= abs(m) < 1."""
    return Decimal(standard_math.frexp(x))


def fsum(iterable):
    """Return an accurate floating point sum of values in the iterable."""
    return Decimal(standard_math.fsum(iterable))


def gcd(a, b):
    """ Return the greatest common divisor of the integers a and b.
        If either a or b is nonzero, then the value of gcd(a, b) is
        the largest positive integer that divides both a and b.
        gcd(0, 0) returns 0. """
    return Decimal(standard_math.gcd(a, b))


def ldexp(x, i):
    """Return x * (2**i). This is essentially the inverse of function
       frexp()."""
    return Decimal(standard_math.ldexp(x, i))


def modf(x):
    """Return the fractional and integer parts of x. Both results carry
       the sign of x."""
    return Decimal(standard_math.modf(x))


def remainder(x, y):
    """Returns the remainder of x and y, using the remainder_near() function
       in Decimal, which comes close to the function in the math library"""
    return Decimal(standard_math.remainder(x, y))


def sign(x):
    """Return -1 for negative numbers and 1 for positive numbers."""
    return Decimal(standard_math.sign(x))


def signt(x):
    """Return -1 for negative numbers and 1 for positive numbers and 0 for
       zeroes and NaNs."""
    return Decimal(standard_math.signt(x))


def acosh(x):
    """Return the inverse hyperbolic cosine of x."""
    return Decimal(standard_math.acosh(x))


def asinh(x):
    """Return the inverse hyperbolic sine of x."""
    return Decimal(standard_math.asinh(x))


def atanh(x):
    """Return the inverse hyperbolic tangent of x."""
    return Decimal(standard_math.atanh(x))


def cosh(x):
    """Return the hyperbolic cosine of x."""
    return Decimal(standard_math.cosh(x))


def sinh(x):
    """Return the hyperbolic sine of x."""
    return Decimal(standard_math.sinh(x))


def tanh(x):
    """Return the hyperbolic tangent of x."""
    return Decimal(standard_math.tanh(x))
