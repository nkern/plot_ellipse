import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

VERSION = "1.0.0"

setup(
	name="plot_ellipse",
	version=VERSION,
	author="Nicholas Kern",
	url="http://github.com/nkern/plot_ellipse",
	packages=['plot_ellipse'],
    python_requires=">=2.7"
)
