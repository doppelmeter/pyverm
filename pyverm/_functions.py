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
API defines the interface you can use to interact with the PyVerm library.

"""



__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"

import math
import decimal


def distance(point_1, point_2, *, report_on=False):
    """
    Calculates the distance between two points.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :param report_on: boolean
    :return: distance as decimal
    """
    distance = ((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)**decimal.Decimal('0.5')
    return distance


def azimuth(point_1, point_2,*,report_on=False):
    """
    Calculates the azimut from point 1 to point 2.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :param report_on: boolean
    :return: azimuth in gon as decimal
    """
    point_1 = helpers.make_point(point_1)
    point_2 = helpers.make_point(point_2)
    delta_y = point_2[0]-point_1[0]
    delta_x = point_2[1] - point_1[1]
    if delta_x != 0:
        azimut = math.atan(delta_y/delta_x)/math.pi*200
    elif delta_y < 0:
        azimut = -100
    else:
        azimut = 100

    if delta_x < 0:
        azimut = azimut+200
    elif delta_y < 0:
        azimut = azimut+400
    return azimut

