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

def point(point):
    point_id = point["point_id"]
    y = point[0]
    x = point[1]
    z = point[2]
    template = "{point_id:<20}{y:>13.4f}  {x:>13.4f}  {z:>13.4f}"
    message = template.format(point_id=point_id, y=y, x=x, z=z)
    return message


def point_title():
    template = "{point_id:<20} {y:<12}   {x:<12}  {z:<9}"
    message = template.format(point_id="Point", y="E", x="N", z="Height")
    return message