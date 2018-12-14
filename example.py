from pyverm import *


print(distance((0,0),(1,1)))

print(azimut((0,0),(-1,1)))


points = PointDatabase()

points.add(Point(0,0,0,"1000"))

print(points[1000])


station_123 = Station()
station_123.standpoint = Point(600,200)
station_123.add_target(point=(700,300),horizontal_angle=123.453,distance=550)
station_123.add_target(point=(800,201),horizontal_angle=100.453,distance=783)
station_123.abriss()


print(station_123.orientation)

p = Point(600,200)
print(p[1])

import pyverm.tests