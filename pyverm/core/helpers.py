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
helpers Module


"""
from pyverm.core.points import Point

__all__ = []

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import decimal
import logging

from . import points
from . import settings


logger = logging.getLogger(__name__)
decimal.getcontext().prec = settings.decimal_precision  # decimal.set_precision


def make_decimal(value):
    if value is None:
        return None
    else:
        return decimal.Decimal(value)


def make_point(point):
    if type(point) is points.Point:
        return point
    else:
        try:
            return points.Point(point[0],point[1],point[2])
        except:
            if point is not None:
                return points.Point(point[0], point[1])
            else:
                return None