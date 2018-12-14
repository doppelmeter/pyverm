import decimal
from .points import Point


class Axis:
    """
    Represents an axis.
    """

    def __init__(self,*, point_1=None, point_2=None, azimuth=None, orientation=None,
                 left_right=None, left_right_through_point=None, plumb=None,
                 plumb_through_point=None, plumb_trough_middle=False, in_out=None):
        """

        Initialice an instance of an axis

        :param point_1: ``Point``-object or ``(y,x)``-tuple
        :param point_2: ``Point``-object or ``(y,x)``-tuple
        :param azimuth: azimuth in gon if only one point is given
        :param orientation: angle in gon
        :param left_right: distance in meter to displace the axis to the left or right
        :param left_right_through_point: ``Point``-object or ``(y,x)``-tuple
        :param plumb: turn the axis with 100gon
        :param plumb_through_point: ``Point``-object or ``(y,x)``-tuple
        :param plumb_trough_middle: boolean -> builds perpendicular bisector
        :param in_out: distance in meter do displace axis in line
        """