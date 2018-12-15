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