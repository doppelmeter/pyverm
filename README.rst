PyVerm
======

What is PyVerm?
^^^^^^^^^^^^^^^

PyVerm is a Python-Package for geodetic and surveying calculations. The main focus
is on calculations for surveying in switzerland, but PyVerm should be as versatile
as possible. In addition to its use in education and research, it should also be
possible to use it as a component for software development.

PyVerm is currently in its first phase of development.


How to install PyVerm?
^^^^^^^^^^^^^^^^^^^^^^

You can install PyVerm with pip.

.. code-block:: bash

    pip install pyverm

**Requirements** Python 3.6 or higher

How to use PyVerm?
^^^^^^^^^^^^^^^^^^

For more examples and information's you should visit the `documentation <https://pyverm.readthedocs.io/en/latest/index.html>`_.

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


How to contribute?
^^^^^^^^^^^^^^^^^^

Bug Reports
-----------
If you find a bug, please open an bug report on `GitHub <https://github.com/doppelmeter/pyverm/issues/new/choose>`_.

Ideas
-----
If you have a brilliant idea for a new feature, please open an feature request `GitHub <https://github.com/doppelmeter/pyverm/issues/new/choose>`_.

Code
----
In the current development phase, I prefer to write the code myself. But for special things
you can contact me via GitHub.

License
^^^^^^^

PyVerm is licensed under the GNU General Public License version 3.

Links
^^^^^
* **Documentation** `pyverm.readthedocs.io <https://pyverm.readthedocs.io/en/latest/index.html>`_
* **Sourcecode** `github.com/doppelmeter/pyverm <https://github.com/doppelmeter/pyverm>`_
* **PyPi** `pypi.org/project/pyverm <https://pypi.org/project/pyverm/>`_
* **License** `GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_






