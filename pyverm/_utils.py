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
from ._classes import Point, ObservationPolar

logger = logging.getLogger(__name__)
getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION  # decimal.set_precision


def input_decimal(value):
    """
    Function to make sure a value to a decimal value.

    :param value: numeric value or ``None``
    :return: value as ``Decimal`` or ``None``
    """
    if value is None:
        return None
    else:
        try:
            return float(value)
        except:
            raise TypeError


def input_point(point):
    """
    Function to make sure it is a point object

    :param point: `Point``-object or ``(y,x,(z))``-tuple ore ``None``
    :return: ``Point``-object or ``None``
    """
    if type(point) is Point:
        return point
    elif point is None:
        return None
    else:
        try:
            return Point(point[0], point[1], point[2])
        except:
            if point is not None:
                return Point(point[0], point[1], None)
            else:
                raise TypeError("argument must be a point or None")


def input_observations_polar(observations):
    if all(isinstance(x, ObservationPolar) for x in observations):
        return observations
    else:
        raise TypeError("argument must be a list or tuple of ObservationPolar")


def input_angle(angle, *, unit=None, output_unit="rad"):
    """
    Return the given angle in rad, the input unit can be set localli or it uses the default settings.

    :param angle: value
    :param local_angle_unit: "deg", "rad", "grad"
    :return: angle in rad as decimal
    """

    def grad_to_rad(x):
        return x / 200 * math.pi

    def deg_to_rad(x):
        return x / 180 * math.pi

    if angle is None:
        return None
    elif isinstance(angle, str):
        angle = float(angle)
    else:
        pass


    if unit is None:
        if settings.DEFAULT_ANGLE_UNIT == "grad":
            rad = grad_to_rad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "deg":
            rad = deg_to_rad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "rad":
            rad = angle
        else:
            raise NotImplemented
    else:
        if unit == "grad":
            rad = grad_to_rad(angle)
        elif unit == "deg":
            rad = deg_to_rad(angle)
        elif unit == "rad":
            rad = angle
        else:
            raise NotImplemented

    # if for any reason the output should not be in rad
    if output_unit != "rad":
        output = output_angle(rad, unit=output_unit)
    else:
        output=rad

    return output


def output_angle(angle, *, unit=None, input_unit="rad"):
    def rad_to_grad(x):
        return (x / math.pi) * 200

    def rad_to_deg(x):
        return (x / math.pi)* 180

    if angle is None:
        return None
    elif isinstance(angle, str):
        angle = float(angle)
    else:
        pass


    # if for any reason the input should not be in rad
    if input_unit != "rad":
        angle = input_angle(angle, unit=input_unit)

    if unit is None:
        if settings.DEFAULT_ANGLE_UNIT == "grad":
            output = rad_to_grad(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "deg":
            output = rad_to_deg(angle)
        elif settings.DEFAULT_ANGLE_UNIT == "rad":
            output = angle
        else:
            raise NotImplemented
    else:
        if unit == "grad":
            output = rad_to_grad(angle)
        elif unit == "deg":
            output = rad_to_deg(angle)
        elif unit == "rad":
            output = angle
        else:
            raise NotImplemented
    return output
