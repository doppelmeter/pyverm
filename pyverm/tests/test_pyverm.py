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
import decimal


from pyverm import azimuth, distance, Point
from pyverm import settings

decimal.getcontext().prec = settings.DECIMAL_PRECISION  # decimal.set_precision

class TestDistance(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(
            distance(Point(0, 0, 0), (0, 0)),
            0,
            'incorrect calculation of distance from point 0,0 to point 0,0')

        self.assertEqual(
            distance((-30, -40), (30, 40)),
            100,
            'incorrect calculation of distance from point -30,-40 to point 30,40')

        self.assertAlmostEqual(
            distance((600000, 200000), (2600000, 1200000)),
            decimal.Decimal('2236067.977499789696409173669'),5,
            'incorrect calculation of distance from point 600000,600000 to point 2600000,1200000')

class TestAzimut(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(
            azimuth((0, 0), (0, 1)),
            0,
            'incorrect calculation of azimut from point 0,0 to point 0,1')

        self.assertEqual(
            azimuth((0, 0), (1, 1)),
            50,
            'incorrect calculation of azimut from point 0,0 to point 1,1')

        self.assertEqual(
            azimuth((0, 0), (1, 0)),
            100,
            'incorrect calculation of azimut from point 0,0 to point 1,0')

        self.assertEqual(
            azimuth((0, 0), (1, -1)),
            150,
            'incorrect calculation of azimut from point 0,0 to point 1,-1')

        self.assertEqual(
            azimuth((0, 0), (0, -1)),
            200,
            'incorrect calculation of azimut from point 0,0 to point 0,-1')

        self.assertEqual(
            azimuth((0, 0), (-1, -1)),
            250,
            'incorrect calculation of azimut from point 0,0 to point -1,-1')

        self.assertEqual(
            azimuth((0, 0), (-1, 0)),
            300,
            'incorrect calculation of azimut from point 0,0 to point -1,0')

        self.assertEqual(
            azimuth((0, 0), (-1, 1)),
            350,
            'incorrect calculation of azimut from point 0,0 to point -1,1')

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point_1 = Point(0, 1, 2)

    def test_access_point_data(self):
        self.assertEqual(
            self.point_1[0],
            0,
            'incorrect access of the y-value')

        self.assertEqual(
            self.point_1[1],
            1,
            'incorrect access of the x-value')

        self.assertEqual(
            self.point_1[2],
            2,
            'incorrect access of the z-value')