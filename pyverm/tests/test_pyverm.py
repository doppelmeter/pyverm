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

import pytest

import pyverm




class Test_pyverm_api:
    def test_version(self):
        pyverm.__meta__

    def test_entry_points(self):

        # basics
        pyverm.azimuth
        pyverm.distance

        # classes
        pyverm.Point
        pyverm.ObservationPolar

        # polar stations
        pyverm.station
        pyverm.station_abriss
        pyverm.station_helmert

    def test_settings(self):
        pyverm.settings.DEFAULT_ANGLE_UNIT
        pyverm.settings.DEFAULT_DECIMAL_PRECISION




