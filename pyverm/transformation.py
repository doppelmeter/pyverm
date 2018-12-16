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
module transformations


"""

__all__ = []

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import math

from core import points


class _Transformation():
    """
    metaclass for all transformations

    defines the general class variables, the following variables can be used from transformations

        _start_points
        _destination_points
        _is_calculated
        _transformation_typ


    the transformation should set the folowwing variables

        _is_calculated -> True, when calculate is run
        _transformation_typ -> "Name of the transformation"


    all transformation parameters should be stored in the following schema

        _parameter_??? -> for example _parameter_a


    defines the general functions of a transformation, the following function must be implemented in the child classes

        calculate(self, report_on=False)  -> calculates the transformation parameter

        _y_to_destination(self, source_point) -> returns destination_y
        _x_to_destination(self, source_point) -> returns destination_x
        _z_to_destination(self, source_point) -> returns destination_z

        _y_to_source(self, destination_point) -> returns source_y
        _x_to_source(self, destination_point) -> returns source_x
        _z_to_source(self, destination_point) -> returns source_z
    """
    def calculate(self, *,report_on=False):
        """
        must be implementet in the transformation
        """
        pass

    def _y_to_destination(self, source_point):
        """
        must be implementet in the transformation
        """
        pass

    def _x_to_destination(self, source_point):
        """
        must be implementet in the transformation
        """
        pass

    def _z_to_destination(self, source_point):
        """
        must be implementet in the transformation
        """
        return 0

    def _y_to_source(self, destination_point):
        """
        must be implementet in the transformation
        """
        pass

    def _x_to_source(self, destination_point):
        """
        must be implementet in the transformation
        """
        pass

    def _z_to_source(self, destination_point):
        """
        must be implementet in the transformation
        """
        return 0

    def __init__(self, *args, point_pairs=None):
        self._start_points = []
        self._destination_points = []

        self._add_transformation_points(*args, point_pairs=point_pairs)

    def _add_transformation_points(self, *args, point_pairs=None):
        # processing of the input arguments
        if len(args) == 2:  # then it will probably be two lists, one with the start and one with the destination points
            if isinstance(args[0], (list, tuple)) and isinstance(args[1], (list, tuple)) and len(args[0]) == len(
                    args[1]):
                for arg in args[0]:  # start points
                    try:
                        self._start_points.append(points.make_point(arg))
                    except:
                        raise ValueError
                for arg in args[1]:  # destination points
                    try:
                        self._destination_points.append(points.make_point(arg))
                    except:
                        raise ValueError
            else:
                raise ValueError
        elif len(args) > 2:  # input will be a tuple per transformation point, with start and destination points
            for arg in args:
                if isinstance(arg, (list, tuple)) and len(arg) == 2:
                    try:
                        self._start_points.append(points.make_point(arg[0]))
                        self._destination_points.append(points.make_point(arg[1]))
                    except:
                        raise ValueError
                else:
                    raise NotImplementedError
        else:
            raise NotImplementedError


    def to_destination(self, point, output="point"):
        point = points.make_point(point)
        new_y = self._y_to_destination(point)
        new_x = self._x_to_destination(point)
        new_z = self._z_to_destination(point)
        if output == "point":
            return points.Point(new_y, new_x, new_z, point_id=point["point_id"])
        elif output == "tuple":
            return (new_y, new_x, new_z)
        elif output == "update":
            point.update(y=new_y, x=new_x)

    def to_source(self, point, output="point"):
        point = points.make_point(point)
        new_y = self._y_to_source(point)
        new_x = self._x_to_source(point)
        new_z = self._z_to_source(point)
        if output == "point":
            return points.Point(new_y, new_x, new_z, point_id=point["point_id"])
        elif output == "tuple":
            return (new_y, new_x, new_z)
        elif output == "update":
            point.update(y=new_y, x=new_x)



class Helmert(_Transformation):
    """
    Helmert 2D transformation
    """
    def calculate(self):
        temp_y = 0
        temp_x = 0
        for point in self._start_points:
            temp_y += point[0]
            temp_x += point[1]
        ys = temp_y/len(self._start_points)
        xs = temp_x / len(self._start_points)

        temp_y = 0
        temp_x = 0
        for point in self._destination_points:
            temp_y += point[0]
            temp_x += point[1]
        Ys = temp_y/len(self._destination_points)
        Xs = temp_x / len(self._destination_points)

        temp_o_oben = 0
        temp_o_unten = 0
        temp_a_oben = 0
        temp_a_unten = 0
        for i in range(len(self._start_points)):
            yr = self._start_points[i][0]-ys
            xr = self._start_points[i][1] - xs
            Yr = self._destination_points[i][0] - Ys
            Xr = self._destination_points[i][1] - Xs
            temp_o_oben += xr*Yr - yr*Xr
            temp_o_unten += xr**2 + yr**2
            temp_a_oben += xr * Xr + yr * Yr
            temp_a_unten += xr ** 2 + yr ** 2
        o = temp_o_oben/temp_o_unten
        a = temp_a_oben/temp_a_unten

        Y0 = Ys- a*ys - o*xs
        X0 = Xs - a*xs + o*ys

        m = math.sqrt(a**2+o**2)
        epsilon = math.atan2(o,a)/math.pi*200

        self._o = o
        self._a = a
        self._Y0 = Y0
        self._X0 = X0
        self._m = m
        self._epsilon = epsilon

    def _y_to_destination(self, source_point):
        new_y = self._Y0 + self._a * source_point[0] + self._o * source_point[1]
        return new_y

    def _x_to_destination(self, source_point):
        new_x = self._X0 + self._a * source_point[1] - self._o * source_point[0]
        return new_x




    def __str__(self):
        str_ = ""
        str_ += "o = "+ str(self._o)+"\n"
        str_ += "a = " + str(self._a) + "\n"
        str_ += "Y0 = " + str(self._Y0) + "\n"
        str_ += "X0 = " + str(self._X0) + "\n"
        str_ += "m = " + str(self._m) + "\n"
        str_ += "epsilon = " + str(self._epsilon) + "\n"
        return str_








if __name__ == "__main__":
    trans = Helmert(((1,0), (0,0), (10,15)),((1,0), (0,0), (10,15)))
    for point in trans._start_points:
        print(point)
    for point in trans._destination_points:
        print(point)

    trans = Helmert(((1, 0), (0, 0)), ((1, 20), (10, 15)), ((21, 20), (10, 30)))
    trans.calculate()
    print(trans)
    point = points.Point(100, 200)
    p = trans.to_destination(point, output="point")
    print(p)
    for point in trans._start_points:
        print(point)
    for point in trans._destination_points:
        print(point)


