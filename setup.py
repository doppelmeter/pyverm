from distutils.core import setup
import setuptools

setup(
    name='pyverm',
    version='0.0.1',
    author='Marius Huerzeler',
    author_email='huerzeler.marius@gmail.com',
    packages=setuptools.find_packages(exclude=['tests*']),
    url='',
    license='MIT',
    description='Modul for geodetic and surveying calculations',
    python_requires='>=3',
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering :: GIS',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
		  'Programming Language :: Python :: 3.7',
          ],

)
