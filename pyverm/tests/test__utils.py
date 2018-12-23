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

from pyverm._utils import input_decimal, input_point
from pyverm._classes import Point


class TestMakeDecimal(unittest.TestCase):
    def test_make_decimal_from_none(self):
        self.assertIsNone(input_decimal(None), msg="test if None stays none")

    def test_make_decimal_from_decimal(self):
        temp = decimal.Decimal("1.3145")
        self.assertIs(temp, input_decimal(temp), msg="test if decimal stays the same object")
        self.assertEqual(temp, input_decimal(temp), msg="test if value dosen't change")

    def test_make_decimal_from_float(self):
        self.assertIsInstance(input_decimal(float(3.14196345)), decimal.Decimal,
                              msg="test if it returns a decimal value")
        self.assertAlmostEqual(decimal.Decimal("0.123456789"), input_decimal(float("0.123456789")),
                               msg="test if value stays the same")

    def test_make_decimal_from_integer(self):
        self.assertIsInstance(input_decimal(int(3)), decimal.Decimal, msg="test if it returns a decimal value")
        self.assertEqual(int("1000"), input_decimal(int("1000")), msg="test if value stays the same")

    def test_make_decimal_from_string(self):
        self.assertIsInstance(input_decimal(str("3.145")), decimal.Decimal, msg="test if it returns a decimal value")
        self.assertEqual(decimal.Decimal(str("1000")), input_decimal(str("1000")), msg="test if value stays the same")
        with self.assertRaises(TypeError, msg="Test if it raises an exception when called with text string"):
            input_decimal("Test")


class TestMakePoint(unittest.TestCase):
    def test_make_point_from_none(self):
        self.assertIsNone(input_point(None), msg="test if None stays none")

    def test_make_point_from_point(self):
        temp = Point(0, 0, 0)
        self.assertIs(temp, input_point(temp), msg="test if point stays the same object")
        self.assertEqual(temp, input_point(temp), msg="test if value dosen't change")

    def test_make_point_from_list(self):
        temp = Point(1, 2, 3)
        self.assertIsInstance(input_point([1, 2, 3]), Point,
                              msg="test if it returns a point object")
        self.assertEqual(temp[0], input_point([1, 2, 3])[0],
                         msg="test if y value stays the same")
        self.assertEqual(temp[1], input_point([1, 2, 3])[1],
                         msg="test if x value stays the same")
        self.assertEqual(temp[2], input_point([1, 2, 3])[2],
                         msg="test if z value stays the same")

    def test_make_point_from_tuple(self):
        temp = Point(1, 2, 3)
        self.assertIsInstance(input_point((1, 2, 3)), Point,
                              msg="test if it returns a point object")
        self.assertEqual(temp[0], input_point((1, 2, 3))[0],
                         msg="test if y value stays the same")
        self.assertEqual(temp[1], input_point((1, 2, 3))[1],
                         msg="test if x value stays the same")
        self.assertEqual(temp[2], input_point((1, 2, 3))[2],
                         msg="test if z value stays the same")
