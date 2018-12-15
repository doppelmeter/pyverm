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

#imports from standard library
import decimal
import logging

#imports from pyverm
from . import settings
from .points import Point

# Module "configuration"
#=======================
# logger
logger = logging.getLogger(__name__)
# decimal.set_precision
decimal.getcontext().prec = settings.decimal_precision


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