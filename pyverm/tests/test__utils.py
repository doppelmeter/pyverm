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
import math

from pyverm._utils import input_decimal, input_point, input_angle, output_angle
from pyverm._classes import Point


class TestInputDecimal(unittest.TestCase):
    def test_input_decimal_from_none(self):
        self.assertIsNone(input_decimal(None), msg="test if None stays none")




class TestInputPoint(unittest.TestCase):
    def test_input_point_from_none(self):
        self.assertIsNone(input_point(None), msg="test if None stays none")

    def test_input_point_from_point(self):
        temp = Point(0, 0, 0)
        self.assertIs(temp, input_point(temp), msg="test if point stays the same object")
        self.assertEqual(temp, input_point(temp), msg="test if value dosen't change")

    def test_input_point_from_list(self):
        temp = Point(1, 2, 3)
        self.assertIsInstance(input_point([1, 2, 3]), Point,
                              msg="test if it returns a point object")
        self.assertEqual(temp[0], input_point([1, 2, 3])[0],
                         msg="test if y value stays the same")
        self.assertEqual(temp[1], input_point([1, 2, 3])[1],
                         msg="test if x value stays the same")
        self.assertEqual(temp[2], input_point([1, 2, 3])[2],
                         msg="test if z value stays the same")

    def test_input_point_from_tuple(self):
        temp = Point(1, 2, 3)
        self.assertIsInstance(input_point((1, 2, 3)), Point,
                              msg="test if it returns a point object")
        self.assertEqual(temp[0], input_point((1, 2, 3))[0],
                         msg="test if y value stays the same")
        self.assertEqual(temp[1], input_point((1, 2, 3))[1],
                         msg="test if x value stays the same")
        self.assertEqual(temp[2], input_point((1, 2, 3))[2],
                         msg="test if z value stays the same")

import pytest


class Test_input_angle():
    def test_input_angle_from_none_is_none(self):
        var = input_angle(None)
        assert var is None


    def test_input_angle_from_int(self):
        var = input_angle(int(200))
        assert var == pytest.approx(math.pi, abs=1e-7)

    def test_input_angle_from_string(self):
        var = input_angle(str(200))
        assert var == pytest.approx(math.pi, abs=1e-7)

    def test_input_angle_from_float(self):
        var = input_angle(float(200.0))
        assert var == pytest.approx(math.pi, abs=1e-7)

    def test_input_angle_from_local_unit_grad(self):
        var = input_angle(200, unit="grad")
        assert var == pytest.approx(math.pi, abs=decimal.Decimal(1e-7))

    def test_input_angle_from_local_unit_deg(self):
        var = input_angle(180, unit="deg")
        assert var == pytest.approx(decimal.Decimal(math.pi), abs=1e-7)

    def test_input_angle_from_local_unit_rad(self):
        var = input_angle(math.pi, unit="rad")
        assert var == pytest.approx(math.pi, abs=1e-7)

class Test_output_angle:
    def test_output_angle_from_none(self):
        var = output_angle(None)
        assert var is None

    def test_output_angle_from_float(self):
        var = output_angle(float(math.pi))
        assert var == pytest.approx(200, abs=1e-7)

    def test_output_angle_from_sting(self):
        var = output_angle(str(math.pi))
        assert var == pytest.approx(200, abs=1e-7)

    def test_output_angle_from_local_unit_grad(self):
        var = output_angle(200, input_unit="grad")
        assert var == pytest.approx(200, abs=1e-7)

    def test_output_angle_to_local_unit_grad(self):
        var = output_angle(math.pi, unit="grad")
        assert var == pytest.approx(200, abs=1e-7)

    def test_output_angle_to_local_unit_deg(self):
        var = output_angle(math.pi, unit="deg")
        assert var == pytest.approx(180, abs=1e-7)

    def test_output_angle_to_local_unit_rad(self):
        var = output_angle(math.pi, unit="rad")
        assert var == pytest.approx(math.pi, abs=1e-7)



