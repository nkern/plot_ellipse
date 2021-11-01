import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command

VERSION = "1.0.1"

setup(
	name="plot_ellipse",
	version=VERSION,
	author="Nicholas Kern",
	url="http://github.com/nkern/plot_ellipse",
	packages=['plot_ellipse'],
    python_requires=">=2.7",
    description="Easily plot 2D ellipses with matplotlib.",
    long_description="Easily plot 2D ellipses with matplotlib." \
    " Accepts 2x2 covariance matrices and plots confidence regions."
    )
