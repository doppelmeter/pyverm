PyVerm
======

**What is PyVerm?**


PyVerm is a Python-Package for geodetic and surveying calculations. The main focus
is on calculations for surveying in switzerland, but PyVerm should be as versatile
as possible. In addition to its use in education and research, it should also be
possible to use it as a component for software development.

PyVerm is currently in its first phase of development.




**How to install PyVerm?**


.. code-block:: bash

    # Python 3.5 and higher or PyPy3.5
    pip install pyverm

**How to use PyVerm?**

.. code-block:: python

    import pyverm

    standpoint = pyverm.Point(2600000, 1200000, 0)
    orientation = 123.4567

    station = pyverm.station(standpoint, orientation)
    new_point = station.survey(pyverm.ObservationPolar(
                                   reduced_horizontal_angle=375.00,
                                   reduced_distance=575.1234
                                   )
                               )

    azimuth = pyverm.azimuth(standpoint, new_point)




User Guide
----------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user/get_started
   user/documentation


General Information's
---------------------

.. toctree::
   :maxdepth: 2
   :caption: General Information's

   info/faq
   info/road-map
   info/release-notes
   info/license


Developers Guide
----------------

.. toctree::
   :maxdepth: 2
   :caption: Developers Guide

   dev/development
   dev/how-to-git
   dev/translations
   dev/todo




   
