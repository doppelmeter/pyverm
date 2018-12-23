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
Basics Module


"""


__all__ = ["distance", "azimuth"]

from decimal import *
import logging
import math

from . import settings
from ._classes import Point

logger = logging.getLogger(__name__)
getcontext().prec = settings.DECIMAL_PRECISION  # decimal.set_precision


def make_decimal(value):
    """
    Fuction to make shure a value to a decimal value.

    :param value: numeric value or ``None``
    :return: value as ``Decimal`` or ``None``
    """
    if value is None:
        return None
    else:
        try:
            return Decimal(value)
        except:
            raise ValueError

def make_point(point):
    """
    Function to make shure it is a point object

    :param point: `Point``-object or ``(y,x,(z))``-tuple ore ``None``
    :return: ``Point``-object or ``None``
    """
    if type(point) is Point:
        return point
    elif point is None:
        return None
    else:
        try:
            return Point(point[0],point[1],point[2])
        except:
            if point is not None:
                return Point(point[0], point[1])
            else:
                return None

def angle_input(angle, *, local_angle_unit=None):
    """
    Return the given angle in rad, the input unit can be set localli or it uses the default settings.

    :param angle: value
    :param local_angle_unit: "deg", "rad", "grad"
    :return: angle in rad as decimal
    """

    def grad_to_rad(x): return x/Decimal(200)* Decimal(math.pi)
    def deg_to_rad(x): return x /Decimal(180) * Decimal(math.pi)

    angle = make_decimal(angle)

    if local_angle_unit is None:
        if settings.DEFAULT_ANGLE_UNIT == "grad":
            rad = grad_to_rad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "deg":
            rad = deg_to_rad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "rad":
            rad = angle
        else:
            raise NotImplemented
    else:
        if local_angle_unit == "grad":
            rad = grad_to_rad(angle)
        elif local_angle_unit == "deg":
            rad = deg_to_rad(angle)
        elif local_angle_unit == "rad":
            rad = angle
        else:
            raise NotImplemented
    return Decimal(rad)


def angle_output(angle,*,local_angle_unit=None):
    def rad_to_grad(x): return (x / Decimal(math.pi)) * Decimal(200)

    def rad_to_deg(x): return (x / Decimal(math.pi)) * Decimal(180)

    angle = make_decimal(angle)

    if local_angle_unit is None:
        if settings.DEFAULT_ANGLE_UNIT == "grad":
            output = rad_to_grad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "deg":
            output = rad_to_deg(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "rad":
            output = angle
        else:
            raise NotImplemented
    else:
        if local_angle_unit == "grad":
            output = rad_to_grad(angle)
        elif local_angle_unit == "deg":
            output = rad_to_deg(angle)
        elif local_angle_unit == "rad":
            output = angle
        else:
            raise NotImplemented
    return Decimal(output)