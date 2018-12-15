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

from pyverm.core import points

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point_1 = points.Point(0, 1, 2, point_id="Point1")

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

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = points.Database()
        self.point_missing_point_id = points.Point(0,0,0)

    def test_add_point_to_db_with_missing_point_id(self):
        self.assertRaises(ValueError, self.db.add(self.point_missing_point_id) ,msg="didn't throw an exception when point_id is missing")
