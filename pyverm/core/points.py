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
Points Module


"""

__all__ = ["Point", "Database"]

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import decimal
import logging

from . import settings
from . import helpers


logger = logging.getLogger(__name__)
decimal.getcontext().prec = settings.decimal_precision  # decimal.set_precision

class Point:
    """
    Represents a point with a y, x and z-coordinate and further optional informations like a point_id etc. The
    coordinates of a point will always be possible to access like the coordinates in a ``(y, x, z)`` tuple or a
    ``[y, x, z]`` list. So you can access for example the points y coordinate as ``point[0]``.

    **Example**


    ..  code-block:: python

        from pyverm.core.point import Point

        point = Point(100, 200, 300, point_id="Test")
        sum_yxc = point[0] + point[1] + point[2]

    """

    def __init__(self, y, x, z=0,*, point_id=None, description=None):
        """

        DADSF

        :param y:
        :param x:
        :param z:
        """
        self.y = decimal.Decimal(y)
        self.x = decimal.Decimal(x)
        self.z = decimal.Decimal(z)
        self.point_id = str(point_id)
        self.description = description

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == "y":
                self.y = decimal.Decimal(value)
            elif key == "x":
                self.x = decimal.Decimal(value)
            elif key == "z":
                self.z = decimal.Decimal(value)
            elif key == "point_id":
                self.point_id = str(value)



    def __getitem__(self, key):
        """
        Adds the possibility to interact with the point class like a tuple (y,x,z)

        :param key:
        :return:
        """
        if key == 0:
            return self.y
        if key == 1:
            return self.x
        if key == 2:
            return self.z
        if key == "point_id":
            return self.point_id

    def __str__(self):
        return f"({self.y}, {self.x}, {self.z}, {self.point_id})"


# for campatability
def make_point(point):
    return helpers.make_point(point)

class Database:
    """
    Represents a collection of points, which have either an string or integer point_id, points can be added, edited
    or deleted. Further all points in a Database can be imported or exported from different common point file formats.
    A point in the database is accessible with it's key ``point_db[10]`` or ``point_db["test"]``.

    **Example**


    ..  code-block:: python

        from pyverm.core.point import Point, Database

        point_1 = Point(100, 200, 300, point_id="Test")
        point_2 = Point(200, 300, 400, point_id="1000")

        db = Database()
        db.add(point_1)
        db.add(point_2)

        point_1000 = db[1000]
        point_Test = db["Test"]

        dt.to_csv("points.csv")
    """

    def __init__(self):
        self.point_dict = {}

    def add(self, point):
        """
        Adds a ``Point``-object to the database, and indexes it under it's point_id.

        :param point: Point object
        """
        if point.point_id == None:
            raise ValueError("to add a point, the point_id of the point must be set.")
        self.point_dict[str(point.point_id)] = point

    def __getitem__(self, key):
        """
        Returns the Point with the given ID

        :param key: point id
        :return: Point Instance
        """
        return self.point_dict[str(key)]

    def to_csv(self, file):
        """
        **To-Do**
        """
        pass

    def from_csv(self, file):
        """
        **To-Do**
        """
