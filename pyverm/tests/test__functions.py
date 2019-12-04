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

import decimal


from .. import _functions
import pyverm

from .. import settings
decimal.getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION

class Test_distance:
    def test_distance_between_the_same_points(self):
        point = (10,10)
        var = _functions.distance(point,point)
        assert var == 0


    def test_distance_returns_correct_value(self):
        var_1 =  _functions.distance((-30, -40), (30, 40))
        assert var_1 == pytest.approx(100, abs=1e-7)
        var_2 = _functions.distance((600000, 200000), (2600000, 1200000))
        assert var_2 == pytest.approx(2236067.977499789696409173669, abs=1e-7)
        var_3 = _functions.distance((0, 1), (0, 1200001))
        assert var_3 == 1200000

class Test_azimuth:
    def test_distance_between_the_same_points(self):
        point = (10,10)
        var = _functions.distance(point,point)
        assert var == 0


    def test_distance_returns_correct_value(self):
        # tuple of point, azimuth tuples which should be tested
        test_values = (
            ((0,1), 0),
            ((1, 1), 50),
            ((1, 0), 100),
            ((1, -1), 150),
            ((0, -1), 200),
            ((-1, -1), 250),
            ((-1, 0), 300),
            ((-1, 1), 350),
            ((-1, -1), 250),
        )
        for point, azimuth in test_values:
            var = _functions.azimuth((0,0),point)
            assert var == pytest.approx(azimuth, abs=1e-7)

class Test_cartesian:
    def test_cartesian_returns_correct_value(self):
        # tuple with points and corresponding azimuths on unit circle
        test_values = (
            ((0, 1), 0),
            ((1, 0), 100),
            ((0, -1), 200),
            ((-1, 0), 300),
        )
        for point, azimuth in test_values:
            y, x = point
            var_y, var_x = _functions.cartesian(1, azimuth)
            assert var_y == pytest.approx(y, abs=1e-7)
            assert var_x == pytest.approx(x, abs=1e-7)

class Test_polar:
    def test_cartesian_returns_correct_value(self):
        # tuple with points and corresponding azimuths on unit circle
        test_values = (
            ((0, 1), 0),
            ((1, 0), 100),
            ((0, -1), 200),
            ((-1, 0), 300),
        )
        for point, azimuth in test_values:
            var_dist, var_azimuth = _functions.polar(point)
            assert var_dist == pytest.approx(1, abs=1e-7)
            assert var_azimuth == pytest.approx(azimuth, abs=1e-7)

class Test_abriss:
    def test_abriss_returns_correct_value(self):
        observations = [
            pyverm.ObservationPolar(
                reduced_targetpoint=(2600100, 1200100),
                reduced_horizontal_angle=0,
                reduced_distance=141.421356237),
            pyverm.ObservationPolar(
                reduced_targetpoint=(2600000, 1199800),
                reduced_horizontal_angle=150,
                reduced_distance=200),
            pyverm.ObservationPolar(
                reduced_targetpoint=(2599900, 1200100),
                reduced_horizontal_angle=300,
                reduced_distance=141.421356237)
        ]
        var = _functions.abriss((2600000,1200000), observations)
        assert var == pytest.approx(50, abs=1e-7)

class Test_free_station:
    def test_abriss_returns_correct_value(self):
        observations = [
            pyverm.ObservationPolar(
                reduced_targetpoint=(2600100, 1200100),
                reduced_horizontal_angle=0,
                reduced_distance=141.421356237),
            pyverm.ObservationPolar(
                reduced_targetpoint=(2600000, 1199800),
                reduced_horizontal_angle=150,
                reduced_distance=200),
            pyverm.ObservationPolar(
                reduced_targetpoint=(2599900, 1200100),
                reduced_horizontal_angle=300,
                reduced_distance=141.421356237)
        ]
        var_standpoint, var_ori = _functions.free_station( observations)
        var_y, var_x, z= var_standpoint
        assert var_ori == pytest.approx(50, abs=1e-7)
        assert var_y == pytest.approx(2600000, abs=1e-7)
        assert var_x == pytest.approx(1200000, abs=1e-7)



