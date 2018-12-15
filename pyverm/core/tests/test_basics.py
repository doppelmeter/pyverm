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

import unittest

from pyverm.core import basics, points
import decimal

class TestDistance(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(
            basics.distance(points.Point(0, 0), (0, 0)),
            0,
            'incorrect calculation of distance from point 0,0 to point 0,0')

        self.assertEqual(
            basics.distance((-30, -40), (30, 40)),
            100,
            'incorrect calculation of distance from point -30,-40 to point 30,40')

        self.assertAlmostEqual(
            basics.distance((600000, 200000), (2600000, 1200000)),
            decimal.Decimal('2236067.977499789696409173669'),10,
            'incorrect calculation of distance from point 600000,600000 to point 2600000,1200000')

class TestAzimut(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(
            basics.azimuth((0, 0), (0, 1)),
            0,
            'incorrect calculation of azimut from point 0,0 to point 0,1')

        self.assertEqual(
            basics.azimuth((0, 0), (1, 1)),
            50,
            'incorrect calculation of azimut from point 0,0 to point 1,1')

        self.assertEqual(
            basics.azimuth((0, 0), (1, 0)),
            100,
            'incorrect calculation of azimut from point 0,0 to point 1,0')

        self.assertEqual(
            basics.azimuth((0, 0), (1, -1)),
            150,
            'incorrect calculation of azimut from point 0,0 to point 1,-1')

        self.assertEqual(
            basics.azimuth((0, 0), (0, -1)),
            200,
            'incorrect calculation of azimut from point 0,0 to point 0,-1')

        self.assertEqual(
            basics.azimuth((0, 0), (-1, -1)),
            250,
            'incorrect calculation of azimut from point 0,0 to point -1,-1')

        self.assertEqual(
            basics.azimuth((0, 0), (-1, 0)),
            300,
            'incorrect calculation of azimut from point 0,0 to point -1,0')

        self.assertEqual(
            basics.azimuth((0, 0), (-1, 1)),
            350,
            'incorrect calculation of azimut from point 0,0 to point -1,1')

