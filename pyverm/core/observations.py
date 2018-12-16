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
Observations Module

..  todo::

    * write unittest
    * write documentation
    * finsih with code


"""

__all__ = []

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import decimal
import logging

if __name__ == "__main__":
    from pyverm.core import settings
    from pyverm.core import helpers
else:
    from . import settings
    from . import helpers


logger = logging.getLogger(__name__)
decimal.getcontext().prec = settings.decimal_precision  # decimal.set_precision

#Observation Purposes
BACKSIGHT = 10
FORESIGHT = 20
NEWPOINT = 30

class _Observation:
    pass


class Polar(_Observation):
    """
    Defines a Polar Observation


    """

    def __init__(self, **kwargs):
        """
        """
        self._purpose = kwargs.get("purpose", None)
        self._target_point = helpers.make_point(kwargs.get("target_point", None))
        self._station_point = helpers.make_point(kwargs.get("station_point", None))

        self._reduced_horizontal_angle = helpers.make_decimal(kwargs.get("reduced_hz", None))
        self._reduced_zenith_angle = helpers.make_decimal(kwargs.get("reduced_vz", None))
        self._reduced_horizontal_distance = helpers.make_decimal(kwargs.get("reduced_distance", None))

        self._raw_horizontal_angle_1 = helpers.make_decimal(kwargs.get("raw_hz_1", None))
        self._raw_horizontal_angle_2 = helpers.make_decimal(kwargs.get("raw_hz_2", None))
        self._raw_zenith_angle_1 = helpers.make_decimal(kwargs.get("raw_vz_1", None))
        self._raw_zenith_angle_2 = helpers.make_decimal(kwargs.get("raw_vz_2", None))

    @property
    def target_point(self):
        return self._target_point

    @property
    def reduced_horizontal_angle(self):
        return self._reduced_horizontal_angle

    @property
    def reduced_zenith_angle(self):
        return self._reduced_zenith_angle

    @property
    def reduced_horizonal_distance(self):
        return self._reduced_horizontal_distance

    @property
    def purpose(self):
        return self._purpose

if __name__ == "__main__":
    ob = Polar()
    print(ob.reduced_horizontal_angle)
