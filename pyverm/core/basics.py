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

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import math
import decimal
import logging

from . import settings
from . import reporting
from . import reporting_templates
from . import helpers
from . import points


logger = logging.getLogger(__name__)
report = reporting.getReport()
decimal.getcontext().prec = settings.decimal_precision  # decimal.set_precision


def distance(point_1, point_2, *, report_on=False):
    """
    Calculates the distance between two points.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :param report_on: boolean
    :return: distance as decimal
    """
    distance = ((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)**decimal.Decimal('0.5')
    if report_on:
        template = "Point           E               N             \n                {point_1[0]:<15} {point_1[1]:<15} \n                {point_2[0]:<15} {point_2[1]:<15} \nResults: \nDistance: {distance:<15}"
        message = template.format(point_1=point_1,point_2=point_2,distance=distance)
        report.add(message)
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
    if report_on:
        message = reporting_templates.point_title()+"\n"
        message += reporting_templates.point(point_1)+"   "
        message += reporting_templates.point(point_2)+"\n"
        report.add(message)
    return azimut

