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

from . import _functions
from . import _classes


__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


def azimuth(point_a, point_b):
    """ Return the azimuth form point A to point B.

    :param point_a: ``Point``-object or ``(y,x)``-tuple
    :param point_b: ``Point``-object or ``(y,x)``-tuple
    :return: azimuth in gon as decimal
    """
    return _functions.azimuth(point_a, point_b)

def distance(point_a, point_b):
    """Return the 2D distance from point A to Point B.

    :param point_a: ``Point``-object or ``(y,x)``-tuple
    :param point_b: ``Point``-object or ``(y,x)``-tuple
    :return: distance in meters as decimal
    """
    return _functions.distance(point_a, point_b)



def station(standpoint, orientation):
    """Return a station object.

    :param standpoint:
    :param orientation:
    :return:
    """
    return _classes.Station(standpoint, orientation)

def station_abriss(standpoint, observations):
    pass

def station_helmert(observations):
    pass


