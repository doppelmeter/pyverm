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