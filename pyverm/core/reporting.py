"""Reporting Module

This module defines reporting-engin for pyverm.
"""

__all__ = ["getReport"]



#imports from standard library
import logging

#imports from pyverm
from . import settings


# Module "configuration"
#=======================
# logger
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






#Initialize Report if it doesn't exist
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

