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
_classes module defines all the classes

"""



__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"

import decimal
import collections

from . import _functions
from . import _utils



Point = collections.namedtuple("Point",["y", "x", "z"])



# class Point:
#     def __init__(self, y, x, z=None):
#         """Point class
#
#         :param y: y-coordinate
#         :param x: x-coordinate
#         :param z: z-coordinate (optional)
#         """
#         self._y = y
#         self._x = x
#         self._z = z
#
#     def __getitem__(self, key):
#         """
#         Adds the possibility to interact with the point class like a tuple (y,x,z)
#
#         :param key:
#         :return:
#         """
#         if key == 0:
#             return self._y
#         if key == 1:
#             return self._x
#         if key == 2:
#             return self._z
#
#     def __repr__(self):
#         if self._z == None:
#             return f"<Point ({self._y:.5f}, {self._x:.5f}, {self._z})>"
#         else:
#             return f"<Point ({self._y:.5f}, {self._x:.5f}, {self._z:.5f})>"

class Station:
    def __init__(self, standpoint, orientation):
        self.standpoint = standpoint
        self.orientation = _utils.input_decimal(orientation)

    def survey(self, observation):
        """Returns the Point, which was surveyed with the given observation.

        :param observation:
        :type observation: pyverm.ObservationPolar
        :return: :class:`Point <Point>` object
        :rtype: pyverm.Point
        """
        y, x = _functions.cartesian(observation.reduced_distance, observation.reduced_horizontal_angle+self.orientation)
        y += decimal.Decimal(self.standpoint[0])
        x += decimal.Decimal(self.standpoint[1])
        return Point(y,x,0)

    def stakeout(self, point):
        """Return the observation values, which are needed to stakeout the given point.

        :param point: point to stakeout
        :type point: tuple or pyverm.Point
        :return: :class:`ObservationPolar <ObservationPolar>` object
        :rtype: pyverm.ObservationPolar
        """
        dist, azi = _functions.polar(point, origin=self.standpoint)
        hz = azi-self.orientation
        observation = ObservationPolar(reduced_distance=dist, reduced_horizontal_angle=hz)
        return observation


    def __repr__(self):
        return f"<Station at ({self.standpoint[0]:.5f}, {self.standpoint[1]:.5f}, {self.standpoint[2]:.5f}) with orientation {self.orientation:.5f}>"


class ObservationPolar:
    def __init__(self, **kwargs):
        """Represent a polar observation with all associated values as simple and usable as possible.

        Despite all attributes are optional, depending on the function certain attributes must be present.

        :param reduced_targetpoint: (optional) Point which was measured with this observation
        :type reduced_targetpoint: tuple or pyverm.Point
        :param reduced_horizontal_angle: (optional) horizontal angle in gon with all corrections
        :type reduced_horizontal_angle: float or decimal
        :param reduced_zenith_angle: (optional) zenith angle in gon with all corrections
        :type reduced_zenith_angle: float or decimal
        :param reduced_distance: (optional) distance in meters with all corrections
        :type reduced_distance: float or decimal
        """
        self.reduced_targetpoint = kwargs.setdefault("reduced_targetpoint", None)
        self._reduced_horizontal_angle = _utils.input_angle(kwargs.setdefault("reduced_horizontal_angle", None))
        self._reduced_zenith_angle = _utils.input_decimal(kwargs.setdefault("reduced_zenith_angle", None))
        self._reduced_distance = _utils.input_decimal(kwargs.setdefault("reduced_distance", None))

    @property
    def reduced_horizontal_angle(self):
        return _utils.output_angle(self._reduced_horizontal_angle)

    @reduced_horizontal_angle.setter
    def reduced_horizontal_angle(self, reduced_horizontal_angle):
        self._reduced_horizontal_angle = _utils.input_angle(reduced_horizontal_angle)

    @property
    def reduced_zenith_angle(self):
        return self._reduced_zenith_angle

    @reduced_zenith_angle.setter
    def reduced_zenith_angle(self, reduced_zenith_angle):
        self.reduced_zenith_angle = decimal.Decimal(reduced_zenith_angle)

    @property
    def reduced_distance(self):
        return self._reduced_distance

    @reduced_distance.setter
    def reduced_distance(self, reduced_distance):
        self._reduced_distance = decimal.Decimal(reduced_distance)

    def __repr__(self):
        return f"<Polar Observation with Hz {self.reduced_horizontal_angle:.5f} and Dist {self.reduced_distance:.5f}>"

class Orthogonal:
    def __init__(self, point_a, point_b, *, mesured_distande=None):
        pass



class Transformation:
    def __init__(self):
        pass

    def info(self):
        """Return the transformation parameters as dict?

        :return:
        """

    def to_destination(self):
        pass

    def to_source(self):
        pass





