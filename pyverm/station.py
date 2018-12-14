from pyverm.core.observation import Polar
from pyverm.core.basics import azimuth

class Station:
    """stellt eine station dar

    idee get in diese richtung:
    station_123 = Station()
    #station_123.standpoint = Point(600,200)
    #station_123.addtarget(point=(700,300),direction=123.453,distance=550)
    #station_123.addtarget(point=(800,201),direction=100.453,distance=783)
    #station_123.abriss()
    """

    def __init__(self,*, station_point=None,  orientation=None):
        self.station_point = station_point
        self.orientation = orientation

    def add_observation(self, target_point, horizontal_angle, distance):
        """

        :param point:
        :param direction:
        :param distance:
        :return:
        """
        self.targetlist.append(Polar(target_point, horizontal_angle, 0, distance))

    def abriss(self, targetlist=None):
        """

        :param targetlist:
        :return:
        """
        temp = 0
        for target in self.targetlist:
            temp += azimuth(self.standpoint, target.target_point) - target.horizontal_angle
        self.orientation = temp / (len(self.targetlist) + 1)


    def freestation(self, targetlist=None):
        """

        :param targetlist:
        :return:
        """
        pass