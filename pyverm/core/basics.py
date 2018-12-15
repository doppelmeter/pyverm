#imports from standard library
import math
import decimal
import logging

#imports from pyverm
from . import settings

# Module "configuration"
#=======================
# logger
logger = logging.getLogger(__name__)
# decimal.set_precision
decimal.getcontext().prec = settings.decimal_precision

def distance(point_1,point_2):
    """
    Calculates the distance between two points.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :return: distance as decimal
    """
    distance = ((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)**decimal.Decimal('0.5')
    return distance

def azimuth(point_1, point_2):
    """
    Calculates the azimut from point 1 to point 2.

    :param point_1: ``Point``-object or ``(y,x)``-tuple
    :param point_2: ``Point``-object or ``(y,x)``-tuple
    :return: azimuth in gon as decimal
    """
    delta_y = point_2[0]-point_1[0]
    delta_x = point_2[1] - point_1[1]
    if delta_x != 0:
        azimut = math.atan(delta_y/delta_x)/math.pi*200
    elif delta_y < 0:
        azimut = -100
    else:
        azimut = 100

    if delta_x < 0:
        azimut = azimut+200
    elif delta_y < 0:
        azimut = azimut+400
    return azimut

