#!/usr/bin/env python

from distutils.core import setup

setup(name='gregex',
      version='0.1',
      description='Regular Expression Playground',
      author='Thura Hlaing',
      author_email='thurahlaing06@gmail.com',
      #url='bump',

      requires=['gtk (>=2.10.0)'],
      data_files=[('share/doc/gregex', ['README', 'COPYING', 'ChangeLog']),
		  ('share/gregex/data',['data/gregex.glade']),
		  ('share/gregex/po',['po/gregex.pot'])],
      scripts=['gregex'],

      classifiers=[
          'Development Status :: 1 - Alpha',
          'Environment :: X11 Applications :: GTK',
          'License :: DFSG approved',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Programming'
          ]
      )

