from setuptools import setup
from Cython.Build import cythonize
import numpy 

setup ( 
    ext_modules=cythonize("cython_files/process_offsets_cy.pyx", language_level=3),
    include_dirs=[numpy.get_include()]
)
