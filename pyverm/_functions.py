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

import math
from decimal import *

from . import _utils
from . import settings

getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION


def distance(point_1, point_2):
    """
    Calculates the 2D distance between two points.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :return: distance as decimal
    """
    # input preprocessing
    point_1 = _utils.input_point(point_1)
    point_2 = _utils.input_point(point_2)
    # calculation
    delta_y = point_2[0] - point_1[0]
    delta_x = point_2[1] - point_1[1]
    distance = ((delta_y ** 2) + (delta_x ** 2)) ** 0.5
    return distance


def azimuth(point_1, point_2):
    """
    Calculates the azimut from point 1 to point 2.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :param report_on: boolean
    :return: azimuth in gon as decimal
    """
    # input preprocessing
    point_1 = _utils.input_point(point_1)
    point_2 = _utils.input_point(point_2)
    # calculation
    delta_y = point_2[0] - point_1[0]
    delta_x = point_2[1] - point_1[1]
    azimuth = math.atan2(delta_y, delta_x)
    # considering that the azimuth is always positive
    if azimuth < 0:
        azimuth += math.pi * 2
    return _utils.output_angle(azimuth)


def cartesian(distance, azimuth):
    """Calculate the cartesian coordinates form polar coordinates

    :param distance: distance as decimal
    :param azimuth: azimuth as decimal
    :return: y, x as decimal
    """
    # input preprocessing
    distance = _utils.input_decimal(distance)
    azimuth = _utils.input_angle(azimuth)
    # calculation
    y = distance * math.sin(azimuth)
    x = distance * math.cos(azimuth)
    return y, x


def polar(point, origin=(0, 0)):
    """

    :param point:
    :param origin:
    :return:
    """
    # input preprocessing
    point = _utils.input_point(point)
    origin = _utils.input_point(origin)
    # calculation
    dist = distance(origin, point)
    azi = azimuth(origin, point)
    return dist, azi


def abriss(standpoint, observations):
    """Calculate the orientation

    :param standpoint: ``Point``-object or ``(y,x)``-tuple
    :param observations: list or tuple of observation-objects
    :return: orientation in gon
    """
    # input preprocessing
    standpoint = _utils.input_point(standpoint)
    observations = _utils.input_observations_polar(observations)
    # calculation
    temp = 0
    for observation in observations:
        azi = azimuth(standpoint, observation.reduced_targetpoint)
        ori = azi - observation.reduced_horizontal_angle
        temp += ori
    orientation = temp / len(observations)
    return orientation


def free_station(observations):
    """Calculate the standpoint and orientation

    :param observations: list or tuple of observation-objects
    :return: standpoint and orientation
    """
    # input preprocessing
    observations = _utils.input_observations_polar(observations)
    # calculation
    temp_ys = 0
    temp_xs = 0
    temp_Ys = 0
    temp_Xs = 0
    for observation in observations:
        y, x = cartesian(observation.reduced_distance, observation.reduced_horizontal_angle)
        temp_ys += y
        temp_xs += x
        temp_Ys += observation.reduced_targetpoint[0]
        temp_Xs += observation.reduced_targetpoint[1]
    n = len(observations)
    ys = temp_ys / n
    xs = temp_xs / n
    Ys = temp_Ys / n
    Xs = temp_Xs / n

    temp_o_oben = 0
    temp_o_unten = 0
    temp_a_oben = 0
    temp_a_unten = 0
    for observation in observations:
        y, x = cartesian(observation.reduced_distance, observation.reduced_horizontal_angle)
        y_ = y - ys
        x_ = x - xs
        Y_ = observation.reduced_targetpoint[0] - Ys
        X_ = observation.reduced_targetpoint[1] - Xs
        temp_o_oben += x_ * Y_ - y_ * X_
        temp_o_unten += x_ ** 2 + y_ ** 2
        temp_a_oben += x_ * X_ + y_ * Y_
        temp_a_unten += x_ ** 2 + y_ ** 2
    o = temp_o_oben / temp_o_unten
    a = temp_a_oben / temp_a_unten

    standpoint = ((Ys - a * ys - o * xs), (Xs - a * xs + o * ys), 0)

    orientation = abriss(standpoint, observations)
    return standpoint, orientation

