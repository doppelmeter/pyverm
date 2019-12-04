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
PyVerm is a Python-Package for geodetic and surveying calculations. The main focus is
on calculations for surveying in switzerland, but PyVerm should be as versatile as
possible. In addition to its use in education and research, it should also be possible
to use it as a component for software development.


..  module:: pyverm

..  autoclass:: ObservationPolar
    :members:
    :inherited-members:
    :special-members: __init__

..  autoclass:: Station
    :members:
    :inherited-members:


"""

__all__ = ["Point", "azimuth", "distance", "station", "station_abriss", "Line", "Circle", "station_helmert", "transformation_helmert", "ObservationPolar"]



from .api import azimuth, distance, station, station_abriss, station_helmert, transformation_helmert, line, circle
from ._classes import ObservationPolar, Point, Station, Line, Circle
from . import __meta__
from . import settings

