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
import pyverm._transformation
from . import _functions
from . import _classes


def azimuth(point_a, point_b):
    """ Return the azimuth form point A to point B.

    The azimuth is the clockwise angle from the north (x axis) and the connecting line from point a to point b.
    It is calculated with the following formula:

    .. math::

       azimuth = \\arctan2 (\\Delta y / \\Delta x)

    :param point_a: Point A
    :type point_a: tuple or pyverm.Point
    :param point_b: Point B
    :type point_b: tuple or pyverm.Point
    :return: azimuth in gon
    :rtype: Decimal
    """
    return _functions.azimuth(point_a, point_b)


def distance(point_a, point_b):
    """Return the 2D distance from point A to Point B.

    .. math::

       distance = \\sqrt{\\Delta y^2 + \\Delta x^2}

    :param point_a: Point A
    :type point_a: tuple or pyverm.Point
    :param point_b: Point B
    :type point_b: tuple or pyverm.Point
    :return: distance in meters
    :rtype: Decimal
    """
    return _functions.distance(point_a, point_b)


def station(standpoint, orientation):
    """Return a station with standpoint and orientation.

    :param standpoint: standpoint
    :type standpoint: tuple or pyverm.Point
    :param orientation: azimuth of null direction
    :type orientation: int or decimal
    :return: :class:`Station <Station>` object
    :rtype: pyverm.Station
    """
    return _classes.Station(standpoint, orientation)


def station_abriss(standpoint, observations):
    """Calculate the orientation from the observations and return the station object.

    .. math::

       abriss = \\frac{\\sum_{i=1}^{n} (azimuth_{standpoint_{i}\\rightarrow targetpoint_{i}} - horizontal\\:angle_{i})}{n}

    :param standpoint: standpoint
    :type standpoint: tuple or pyverm.Point
    :param observations: a list or a tuple containing the Observations
    :type observations: list or tuple with pyverm.ObservationPolar
    :return: :class:`Station <Station>` object
    :rtype: pyverm.Station
    """
    orientation = _functions.abriss(standpoint, observations)
    return _classes.Station(standpoint, orientation)


def station_helmert(observations):
    """Calculate the standpoint and orientation and return the station object.

    The station is calculated locally an then transformed in the coordinate system truth a helmert transformation.
    The orientation gets determined over an abriss.

    :param observations: a list or a tuple containing the Observations
    :type observations: list or tuple with pyverm.ObservationPolar
    :return: :class:`Station <Station>` object
    :rtype: pyverm.Station
    """
    standpoint, orientation = _functions.free_station(observations)
    return _classes.Station(standpoint, orientation)



def transformation_helmert(sourcepoints, destinationpoints):
    """Calculates the transformation and returns a :class:`Transformation <Transformation>` object.


    :param sourcepoints: the source points for the transformation
    :type sourcepoints: list or tuple with pyverm.Point
    :param destinationpoints: the destination points for the transformation
    :type destinationpoints: list or tuple with pyverm.Point
    :return: :class:`Transformation <Transformation>` object
    :rtype: pyverm.Station
    """
    return pyverm._transformation.Transformation(sourcepoints, destinationpoints, method="helmert")

def line(startpoint, endpoint):
    """Return a line object

    :param startpoint: the start point of the line
    :type startpoint: pyverm.Point
    :param endpoint: the end point of the line
    :type endpoint: pyverm.Point
    :return: :class:`Line <Line>` object
    :rtype: pyverm.Line
    """
    return pyverm._classes.Line(startpoint, endpoint)


def circle(center, radius):
    """Return a line object

    :param center: the center of the circle
    :type center: pyverm.Point
    :param radius: radius of the circle
    :type radius: int or decimal
    :return: :class:`Circle <Circle>` object
    :rtype: pyverm.Circle
    """
    return pyverm._classes.Circle(center, radius)

def intersect( object_a, object_b):
    """To-Do

    :param object_a:
    :type object_a: pyverm.Circle or pyverm.Line
    :param object_b:
    :type object_b: pyverm.Circle or pyverm.Line
    :return: tuple with all intersection points
    """
    raise NotImplemented

def area(definition):
    """To-Do

    :param definition:
    :return:
    """
    raise NotImplemented