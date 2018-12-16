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
Reporting Templates


"""

__all__ = []

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"

def report_title():
    msg =  "                                                                        \n"
    msg += "                _____      __      __                                   " + "\n"
    msg += "               |  __ \     \ \    / /                                   " + "\n"
    msg += "               | |__) |_   _\ \  / /___  _ __  _ __ ___                 " + "\n"
    msg += "               |  ___/| | | |\ \/ // _ \| '__|| '_ ` _ \                " + "\n"
    msg += "               | |    | |_| | \  /|  __/| |   | | | | | |               " + "\n"
    msg += "               |_|     \__, |  \/  \___||_|   |_| |_| |_|               " + "\n"
    msg += "                        __/ |                                           " + "\n"
    msg += "                       |___/                                            " + "\n"
    msg += "                                                                        " + "\n"
    return msg

def transformation():
    msg = "                                                                        \n"
    msg += "Transformation - Helmert                                                " + "\n"
    msg += "========================================================================" + "\n"
    msg += "                                                                        " + "\n"
    msg += "Source		Destination	    dE      dN      dH                          " + "\n"
    msg += "------------------------------------------------------------------------" + "\n"
    msg += "1478523		1478523         -22.00  -22.00  -22.00                      " + "\n"
    msg += "1478523		1478523         -22.00  -22.00  -22.00                      " + "\n"
    msg += "1478523		1478523         -22.00  -22.00  -22.00                      " + "\n"
    msg += "1478523		1478523         -22.00  -22.00  -22.00                      " + "\n"
    msg += "1478523		1478523         -22.00  -22.00  -22.00                      " + "\n"
    msg += "                                                                        " + "\n"
    msg += "Shift	        	Rotation	    Scale                               " + "\n"
    msg += "------------------------------------------------------------------------" + "\n"
    msg += "E   2600000.0000	R1	400.0000  	1.000000000                         " + "\n"
    msg += "N 	2600000.0000    R1	400.0000                                        " + "\n"
    msg += "H 	   0000.0000    R1	400.0000                                        " + "\n"
    msg += "                                                                        " + "\n"
    msg += "Point   	E			 N			  H                                 " + "\n"
    msg += "------------------------------------------------------------------------" + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (source)                " + "\n"
    msg += "84504637	2600000.0000 1200000.0000 0000.0000 (destination)           " + "\n"
    msg += "                                                                        " + "\n"
    return msg

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