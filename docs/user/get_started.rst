Get Started
==================

Installation
------------

You can install pyverm easily over PIP.

.. code-block:: bash

    pip install pyverm


Code Examples
-------------

Distance and Azimuth
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import pyverm

    point_1 = pyverm.Point(2600123, 1200456, 0)
    point_2 = pyverm.Point(2600789, 1200123, 0)

    distance = pyverm.distance(point_1, point_2)

    azimuth = pyverm.azimuth(point_1, point_2)



Polar Stakeout
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import pyverm

    standpoint = pyverm.Point(2600000, 1200000, 0)
    orientation = 123.4567

    station = pyverm.station(standpoint, orientation)
    observation = station.stakeout(pyverm.Point(2600010, 1200020, 0))


Free Station
^^^^^^^^^^^^

.. code-block:: python

    import pyverm

    observations = [
        pyverm.ObservationPolar(
            reduced_targetpoint=(2600100, 1200100),
            reduced_horizontal_angle=0,
            reduced_distance=141.421356237),
        pyverm.ObservationPolar(
            reduced_targetpoint=(2600000, 1199800),
            reduced_horizontal_angle=150,
            reduced_distance=200),
        pyverm.ObservationPolar(
            reduced_targetpoint=(2599900, 1200100),
            reduced_horizontal_angle=300,
            reduced_distance=141.421356237)
    ]

    station = pyverm.station_helmert(observations)

    standpoint = station.standpoint
    orientation = station.orientation

    new_point = station.survey(pyverm.ObservationPolar(
                                   reduced_horizontal_angle=375.00,
                                   reduced_distance=575.1234
                                   )
                               )

