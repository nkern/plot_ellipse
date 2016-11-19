import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

VERSION = "0.0.1"


setup(
	name="plot_ellipse",
	version=VERSION,
	author="Nick Kern",
	url="http://github.com/nkern/plot_ellipse",
	packages=['tests']
)
