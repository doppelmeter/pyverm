import unittest

from pyverm.core import points

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point_1 = points.Point(0, 1, 2, "Point1")

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
