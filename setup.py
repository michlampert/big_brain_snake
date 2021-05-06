from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("map_distances.pyx", language_level = "3", annotate=True)
)