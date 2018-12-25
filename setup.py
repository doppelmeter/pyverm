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
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


about = {}
with open(os.path.join(here, 'pyverm', '__meta__.py'), 'r', encoding='utf-8') as f:
    exec (f.read(), about)
with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()
# with open('HISTORY.rst', 'r', 'utf-8') as f:
#     history = f.read()

setup(
    name=about['__title__'],
    version=about['__release__'],
    author=about['__author__'],
    author_email='huerzeler.marius@gmail.com',
    packages=setuptools.find_packages(exclude=['tests*']),
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],
    long_description=readme,
    python_requires='>=3',
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering :: GIS',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
		  'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',

          ],

)
