#imports from standard library
import decimal
import logging

#imports from pyverm
from .points import Point
from . import settings

# Module "configuration"
#=======================
# logger
logger = logging.getLogger(__name__)
# decimal.set_precision
decimal.getcontext().prec = settings.decimal_precision

class Circle:
    """
    Represents a Circle
    """
    def __init__(self,*, center_point=None, radius=None):
        """
        initialise a circle object.

        :param center_point: ``Point``-object or ``(y,x)``-tuple
        :param radius: distance in meter
        """
        if radius is not None:
            self.radius = decimal.Decimal(radius)

        if center_point is Point:
            self.center_point = center_point
        elif center_point is not None:
            self.center_point = Point(center_point[0],center_point[1])

    def from_3_points(self, point_1, point_2, point_3):
        """
        Calculates Radius and center_point out of 3 points, and sets the circle to the calculated values.

        **To-To**

        :param point_1: ``Point``-object or ``(y,x)``-tuple
        :param point_2: ``Point``-object or ``(y,x)``-tuple
        :param point_3: ``Point``-object or ``(y,x)``-tuple
        """
        pass

    def from_2_points_radius(self, point_1, point_2, radius):
        """
        Calculates Radius and center_point out of 2 points and the radius, and sets the circle to the calculated values.

        **To-To**

        :param point_1: ``Point``-object or ``(y,x)``-tuple
        :param point_2: ``Point``-object or ``(y,x)``-tuple
        :param radius: radius in meter
        """
