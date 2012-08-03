#!/usr/bin/env python

from distutils.core import setup

setup(
    name='hgallpaths',
    version='0.1',
    author='Keegan Carruthers-Smith',
    author_email='keegan.csmith@gmail.com',
    url='https://bitbucket.org/keegan_csmith/hgallpaths',
    license='BSD',
    py_modules=['hgallpaths'],
    description=('A mercurial extension to allow pushing and pulling from '
                 'all paths.'),
    long_description=file('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
