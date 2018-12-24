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
Test if the samples in the documentation ar working.

"""
import unittest
import decimal

import pyverm


class TestExample1(unittest.TestCase):
    # uses the setUp methode to test if the example raises an error.
    def setUp(self):
        point_1 = pyverm.Point(2600123, 1200456, 0)
        point_2 = pyverm.Point(2600789, 1200123, 0)
        distance = pyverm.distance(point_1, point_2)
        azimuth = pyverm.azimuth(point_1, point_2)

    def test_example1(self):
        self.assertTrue(True, msg="problem in example 1")


class TestExample2(unittest.TestCase):
    # uses the setUp methode to test if the example raises an error.
    def setUp(self):
        standpoint = pyverm.Point(2600000, 1200000, 0)
        orientation = 123.4567
        station = pyverm.station(standpoint, orientation)
        observation = station.stakeout(pyverm.Point(2600010, 1200020, 0))

    def test_example2(self):
        self.assertTrue(True, msg="problem in example 2")


class TestExample3(unittest.TestCase):
    # uses the setUp methode to test if the example raises an error.
    def setUp(self):
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
        station = pyverm.station_helmert(observations)
        standpoint = station.standpoint
        orientation = station.orientation
        new_point = station.survey(pyverm.ObservationPolar(
            reduced_horizontal_angle=375.00,

            reduced_distance=575.1234
        )
        )

    def test_example3(self):
        self.assertTrue(True, msg="problem in example 3")


class TestExample4(unittest.TestCase):
    # uses the setUp methode to test if the example raises an error.
    def setUp(self):
        standpoint = pyverm.Point(2600000, 1200000, 0)
        orientation = 123.4567

        station = pyverm.station(standpoint, orientation)
        new_point = station.survey(pyverm.ObservationPolar(
            reduced_horizontal_angle=375.00,
            reduced_distance=575.1234
        )
        )

        azimuth = pyverm.azimuth(standpoint, new_point)

    def test_example4(self):
        self.assertTrue(True, msg="problem in example 4")
