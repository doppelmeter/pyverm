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
            basics.azimut((0, 0), (0, 1)),
            0,
            'incorrect calculation of azimut from point 0,0 to point 0,1')

        self.assertEqual(
            basics.azimut((0, 0), (1, 1)),
            50,
            'incorrect calculation of azimut from point 0,0 to point 1,1')

        self.assertEqual(
            basics.azimut((0, 0), (1, 0)),
            100,
            'incorrect calculation of azimut from point 0,0 to point 1,0')

        self.assertEqual(
            basics.azimut((0, 0), (1, -1)),
            150,
            'incorrect calculation of azimut from point 0,0 to point 1,-1')

        self.assertEqual(
            basics.azimut((0, 0), (0, -1)),
            200,
            'incorrect calculation of azimut from point 0,0 to point 0,-1')

        self.assertEqual(
            basics.azimut((0, 0), (-1, -1)),
            250,
            'incorrect calculation of azimut from point 0,0 to point -1,-1')

        self.assertEqual(
            basics.azimut((0, 0), (-1, 0)),
            300,
            'incorrect calculation of azimut from point 0,0 to point -1,0')

        self.assertEqual(
            basics.azimut((0, 0), (-1, 1)),
            350,
            'incorrect calculation of azimut from point 0,0 to point -1,1')

