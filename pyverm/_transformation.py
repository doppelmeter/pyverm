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
_transformation contains all to transformation relatet intern function
and classes.

"""

import math
from decimal import *

from pyverm import _functions
from . import settings

getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION


class Transformation:
    def __init__(self, sourcepoints, destinationpoints, *, method=None):
        """
        Calls the function of the given transformation method, which
        returns the Fuctions needed to init this class

        :param sourcepoints:
        :param destinationpoints:
        :param method:
        """
        if method is None:
            raise NotImplemented
        elif method == "two_point":
            info, to_destination, to_source = _functions.transformation_two_point(sourcepoints,
                                                                                  destinationpoints)
        elif method == "helmert":
            info, to_destination, to_source = transformation_helmert(sourcepoints,
                                                                     destinationpoints)
        else:
            raise NotImplemented

        self.info = info
        self.to_destination = to_destination
        self.to_source = to_source


def transformation_helmert(sourcepoints, destinationpoints):
    def info():
        str_ = ""
        str_ += "o = " + str(o) + "\n"
        str_ += "a = " + str(a) + "\n"
        str_ += "Y0 = " + str(Y0) + "\n"
        str_ += "X0 = " + str(X0) + "\n"
        str_ += "m = " + str(m) + "\n"
        str_ += "epsilon = " + str(epsilon) + "\n"
        return str_

    def to_destination(point):
        new_y = Y0 + a * point[0] + o * point[1]
        new_x = X0 + a * point[1] - o * point[0]
        return (new_y, new_x)

    def to_source():
        raise NotImplemented

    temp_y = 0
    temp_x = 0
    for point in sourcepoints:
        temp_y += point[0]
        temp_x += point[1]
    ys = temp_y / len(sourcepoints)
    xs = temp_x / len(sourcepoints)

    temp_y = 0
    temp_x = 0
    for point in destinationpoints:
        temp_y += point[0]
        temp_x += point[1]
    Ys = temp_y / len(destinationpoints)
    Xs = temp_x / len(destinationpoints)

    temp_o_oben = 0
    temp_o_unten = 0
    temp_a_oben = 0
    temp_a_unten = 0
    for i in range(len(sourcepoints)):
        yr = sourcepoints[i][0] - ys
        xr = sourcepoints[i][1] - xs
        Yr = destinationpoints[i][0] - Ys
        Xr = destinationpoints[i][1] - Xs
        temp_o_oben += xr * Yr - yr * Xr
        temp_o_unten += xr ** 2 + yr ** 2
        temp_a_oben += xr * Xr + yr * Yr
        temp_a_unten += xr ** 2 + yr ** 2
    o = temp_o_oben / temp_o_unten
    a = temp_a_oben / temp_a_unten

    Y0 = Ys - a * ys - o * xs
    X0 = Xs - a * xs + o * ys

    m = math.sqrt(a ** 2 + o ** 2)
    epsilon = math.atan2(o, a) / math.pi * 200

    return info, to_destination, to_source
