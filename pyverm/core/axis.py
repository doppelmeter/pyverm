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
Axis Module


"""

__all__ = ["Axis"]

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import decimal
import logging
import math

from . import settings
from . import points


logger = logging.getLogger(__name__)
decimal.getcontext().prec = settings.decimal_precision  # set decimal precision


class Axis:
    """
    Represents an axis.
    """

    def __init__(self,*, point_1=None, point_2=None, azimuth=None, orientation=None,
                 left_right=None, left_right_through_point=None, plumb=None,
                 plumb_through_point=None, plumb_trough_middle=False, in_out=None):
        """

        Initialice an instance of an axis

        :param point_1: ``Point``-object or ``(y,x)``-tuple
        :param point_2: ``Point``-object or ``(y,x)``-tuple
        :param azimuth: azimuth in gon if only one point is given
        :param orientation: angle in gon
        :param left_right: distance in meter to displace the axis to the left or right
        :param left_right_through_point: ``Point``-object or ``(y,x)``-tuple
        :param plumb: turn the axis with 100gon
        :param plumb_through_point: ``Point``-object or ``(y,x)``-tuple
        :param plumb_trough_middle: boolean -> builds perpendicular bisector
        :param in_out: distance in meter do displace axis in line
        """
        self._a = 0  # linear equation
        self._b = 0  # linear equation

        self._point_1 = points.make_point(point_1)
        self._point_2 = points.make_point(point_2)
        self._azimuth = (azimuth)
        self._orientation = (orientation)
        self._left_right = (left_right)
        self._left_right_trough_point = points.make_point(left_right_through_point)
        self._plumb = plumb
        self._plumb_trough_point = points.make_point(plumb_through_point)
        self._plumb_trough_middle = plumb_trough_middle
        self._in_out = (in_out)

        self._a = (self._point_2[1]-self._point_1[1])/(self._point_2[0]-self._point_1[0])
        self._b = self._a*self._point_1[0]-self._point_1[1]

        print("a= "+str(self._a)+"  b= "+str(self._b))

