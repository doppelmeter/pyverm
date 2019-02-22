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
import unittest
import decimal

import pyverm
from pyverm import azimuth, distance, Point, Line, Circle
from pyverm import settings

decimal.getcontext().prec = settings.DEFAULT_DECIMAL_PRECISION  # decimal.set_precision


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

class Test_Line:
    def test_line_class(self):
        line = Line([0,0,0],(1,1,1))

class Test_Circle:
    def test_circle_class(self):
        circle = Circle([0,0,0],3.2)