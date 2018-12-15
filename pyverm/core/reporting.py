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
Reporting Module

This module defines reporting-engin for pyverm.
"""

__all__ = ["getReport"]

__author__ = "Marius Hürzler"
__copyright__ = "Copyright (C) 2018, Marius Hürzeler"
__license__ = "GNU GPLv3"


import logging

from . import settings


logger = logging.getLogger(__name__)


class _Report:
    def __init__(self):
        self._report = ""

    def add(self, message):
        """
        Adds the given message to the report

        :param message:
        """
        self._report = self._report + message

    def clear(self):
        """
        Emptyes the report, this function can't be redone


        """
        self._report = ""

    def to_txt(self, filename):
        """
        Saves current report to the given filename as txt.

        :param filename: string (path with filename)
        """
        file = open(file, "w", encoding="UTF-8")
        file.write(self._report)
        file.close()

    def __str__(self):
        return self._report


# Initialize Report if it doesn't exist
try:
    s = str(_report)
except:
    _report = _Report()


def getReport():
    """
    Fuction to get the pyverm reporting engin, so you can interact with it.

    :return: report-instance
    """
    return _report

