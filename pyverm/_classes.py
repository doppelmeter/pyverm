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



class Point:
    def __init__(self, y, x, z=None):
        self._y = y
        self._x = x
        self._z = z

    def __getitem__(self, key):
        """
        Adds the possibility to interact with the point class like a tuple (y,x,z)

        :param key:
        :return:
        """
        if key == 0:
            return self._y
        if key == 1:
            return self._x
        if key == 2:
            return self._z

class Station:
    def __init__(self, standpoint, orientation):
        self.standpoint = standpoint
        self.orientation = orientation

    def survey(self, observation_polar):
        pass

    def stakeout(self, point):
        pass


class ObservationPolar:
    def __init__(self, targetpoint, reduced_horizontal_angle, reduced_zenith_angle, reduced_distance):
        self.targetpoint = targetpoint
        self.reduced_horizontal_angle = reduced_horizontal_angle
        self.reduced_zenith_angle = reduced_zenith_angle
        self.reduced_distance = reduced_distance






