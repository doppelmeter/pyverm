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

from decimal import *
import collections
import math

from . import _functions
from . import _utils
from . import settings

getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION



Point = collections.namedtuple("Point", ["y", "x", "z"])


class Station:
    def __init__(self, standpoint, orientation):
        standpoint = _utils.input_point(standpoint)
        orientation = _utils.input_angle(orientation)
        self.standpoint = standpoint
        self._orientation = orientation

    @property
    def orientation(self):
        return _utils.output_angle(self._orientation)

    @orientation.setter
    def orientation(self, orientation):
        orientation = _utils.input_angle(orientation)
        self._orientation = orientation

    def survey(self, observation):
        """Returns the Point, which was surveyed with the given observation.

        :param observation:
        :type observation: pyverm.ObservationPolar
        :return: :class:`Point <Point>` object
        :rtype: pyverm.Point
        """
        y, x = _functions.cartesian(observation.reduced_distance,
                                    observation.reduced_horizontal_angle + self.orientation)
        y += self.standpoint[0]
        x += self.standpoint[1]
        return Point(y, x, 0)

    def stakeout(self, point):
        """Return the observation values, which are needed to stakeout the given point.

        :param point: point to stakeout
        :type point: tuple or pyverm.Point
        :return: :class:`ObservationPolar <ObservationPolar>` object
        :rtype: pyverm.ObservationPolar
        """
        point = _utils.input_point(point)
        dist, azi = _functions.polar(point, origin=self.standpoint)
        hz = azi - self.orientation
        observation = ObservationPolar(reduced_distance=dist, reduced_horizontal_angle=hz)
        return observation

    def __repr__(self):
        return "<Station at ({:.5f}, {:.5f}, {:.5f}) with orientation {:.5f}>".format(self.standpoint[0], self.standpoint[1],self.standpoint[2], self.orientation)


class ObservationPolar:
    def __init__(self, **kwargs):
        """Represent a polar observation with all associated values as simple and usable as possible.

        Despite all attributes are optional, depending on the function certain attributes must be present.

        ..  todo::

            * Document the reduction of the raw values
            * implement the reduction of the distance
            * add unittest for this class

        :param reduced_targetpoint: (optional) Point which was measured with this observation
        :type reduced_targetpoint: tuple or pyverm.Point
        :param reduced_horizontal_angle: (optional) horizontal angle in gon with all corrections
        :type reduced_horizontal_angle: float or decimal
        :param reduced_zenith_angle: (optional) zenith angle in gon with all corrections
        :type reduced_zenith_angle: float or decimal
        :param reduced_distance: (optional) distance in meters with all corrections
        :type reduced_distance: float or decimal

        :param raw_horizontal_angle: (optional) horizontal angle in gon
        :type raw_horizontal_angle: float or decimal
        :param raw_horizontal_angle_2: (optional) horizontal angle in gon in second direction
        :type raw_horizontal_angle_2: float or decimal
        :param raw_zenith_angle: (optional) zenith angle in gon
        :type raw_zenith_angle: float or decimal
        :param raw_zenith_angle_2: (optional) zenith angle in gon in second direction
        :type raw_zenith_angle_2: float or decimal
        :param raw_distance: (optional) distance in meters **not yet implemented**
        :type raw_distance: float or decimal
        :param raw_distance_2: (optional) distance in meters in second direction **not yet implemented**
        :type raw_distance_2: float or decimal


        """
        # reduced values
        self.reduced_targetpoint = kwargs.setdefault("reduced_targetpoint", None)
        self._reduced_hz = _utils.input_angle(kwargs.setdefault("reduced_horizontal_angle", None))
        self._reduced_v = _utils.input_angle(kwargs.setdefault("reduced_zenith_angle", None))
        self._reduced_distance = _utils.input_decimal(kwargs.setdefault("reduced_distance", None))

        # raw values
        self._raw_hz_1 = _utils.input_angle(kwargs.setdefault("raw_horizontal_angle", None))
        self._raw_hz_2 = _utils.input_angle(kwargs.setdefault("raw_horizontal_angle_2", None))
        self._raw_v_1 = _utils.input_angle(kwargs.setdefault("raw_zenith_angle", None))
        self._raw_v_2 = _utils.input_angle(kwargs.setdefault("raw_zenith_angle_2", None))
        self._raw_distance_1 = _utils.input_decimal(kwargs.setdefault("raw_distance", None))
        self._raw_distance_2 = _utils.input_decimal(kwargs.setdefault("raw_distance_2", None))

    @property
    def reduced_horizontal_angle(self):
        """
        Return reduced_horizontal_angle or if None and raw in two direction present, return calculated reduced angle
        :return:
        """
        if self._reduced_hz is None:
            # average from to directions
            if self._raw_hz_2 is not None and self._raw_hz_1 is not None:
                if self._raw_hz_2 > self._raw_hz_1:
                    temp = -1
                else:
                    temp = +1
                reduced = ((self._raw_hz_1 + (
                        self._raw_hz_2 + Decimal(math.pi * temp)))) / Decimal(2)
            elif self._raw_hz_1 is not None:
                reduced = self._raw_hz_1
            else:
                raise NotImplemented("there is no zenith angle")
            output = reduced
        else:
            output = self._reduced_hz
        return _utils.output_angle(output)

    @reduced_horizontal_angle.setter
    def reduced_horizontal_angle(self, reduced_horizontal_angle):
        self._reduced_hz = _utils.input_angle(reduced_horizontal_angle)

    @property
    def reduced_zenith_angle(self):
        """
        Return reduced_zenith_angle or if None and raw in two direction present, return calculated reduced angle
        :return:
        """
        if self._reduced_v is None:
            # average from to directions
            if self._raw_v_2 is not None and self._raw_v_1 is not None:
                reduced = ((self._raw_v_1 - self._raw_v_2) + math.pi * 2) / 2
            elif self._raw_v_1 is not None:
                reduced = self._raw_v_1
            else:
                raise NotImplemented("there is no zenith angle")
            output = reduced
        else:
            output = self._reduced_v
        return _utils.output_angle(output)

    @reduced_zenith_angle.setter
    def reduced_zenith_angle(self, reduced_zenith_angle):
        self._reduced_v = _utils.input_angle(reduced_zenith_angle)

    @property
    def reduced_distance(self):
        if self._reduced_distance is None:
            raise NotImplemented("reduction of raw distance is not implemented")
        else:
            return self._reduced_distance

    @reduced_distance.setter
    def reduced_distance(self, reduced_distance):
        self._reduced_distance = reduced_distance

    def __repr__(self):
        return "<Polar Observation with Hz {:.5f} and Dist {:.5f}>".format(self.reduced_horizontal_angle, self.reduced_distance)



class Orthogonal:
    def __init__(self, point_a, point_b, *, mesured_distande=None):
        pass

class Line:
    def __init__(self, startpoint, endpoint):
        startpoint = _utils.input_point(startpoint)
        endpoint = _utils.input_point(endpoint)
        self.startpoint = startpoint
        self.endpoint = endpoint

class Circle:
    def __init__(self, center, radius):
        center = _utils.input_point(center)
        radius = _utils.input_decimal(radius)
        self.center = center
        self.radius = radius



