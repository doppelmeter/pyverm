#imports from standard library
import logging

#imports from pyverm
from . import settings


# Module "configuration"
#=======================
# logger
logger = logging.getLogger(__name__)

class Report:
    def __init__(self):
        self._report = ""

    def add(self, repport):
        self._report = self._report + repport

    def clear(self):
        self._report = ""

    def __str__(self):
        return self._report

#Initialize Report if it doesn't exist
try:
    s = str(_report)
except:
    _report = Report()

def getReport():
    return _report

