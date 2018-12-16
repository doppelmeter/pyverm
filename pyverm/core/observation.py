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


"""

__all__ = []

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import decimal
import logging

if __name__ == "__main__":
    from pyverm.core import settings
else:
    from . import settings


logger = logging.getLogger(__name__)
decimal.getcontext().prec = settings.decimal_precision  # decimal.set_precision

class _Observation:
    pass


class Polar(_Observation):
    """
    Defines a Polar Observation


    """

    def __init__(self, *, **kwargs):
        """
        """
        self._reduced_horizontal_angle = kwargs.get("reduced_hz", None)

    @property
    def reduced_horizontal_angle(self):
        return "Test"

    @property
    def reduced_zenith_angle(self):
        pass

    @property
    def reduced_horizonal_distance(self):
        pass

    @property
    def observation_purpose(self):
        pass

if __name__ == "__main__":
    ob = Polar()
    print(ob.reduced_horizontal_angle)
