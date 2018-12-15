########################################################################
#                                                                      #
# Copyright (C) 2018,  Marius Hürzeler                                 #
#                                                                      #
# This file is part of PyVerm.                                         #
#                                                                      #
# PyVerm is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# PyVerm is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                      #
########################################################################

from distutils.core import setup
import setuptools

setup(
    name='pyverm',
    version='0.0.2',
    author='Marius Huerzeler',
    author_email='huerzeler.marius@gmail.com',
    packages=setuptools.find_packages(exclude=['tests*']),
    url='https://doppelmeter.github.io/pyverm/index.html',
    license='GNU GPLv3+',
    description='Modul for geodetic and surveying calculations',
    python_requires='>=3',
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering :: GIS',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
		  'Programming Language :: Python :: 3.7',
          ],

)
