#!/usr/bin/env python

from setuptools import setup

setup(name='kim',
      version='0.1.0',
      description='CLI client for the Kimai HTTP API',
      author='Markus Dittmann',
      author_email='dmarku@posteo.de',
      url='https://github.com/dmarku/kim',

      install_requires=[
          'requests',
      ],

      entry_points={
          'console_scripts': [
              'kim = cli:run',
          ],
      },
 )
