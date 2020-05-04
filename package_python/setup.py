# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------
copyright info
# ----------------------------------------------------------------------------------------------------

from setuptools import setup, find_packages
import os
import sys
import textwrap
import warnings
import urllib
from setuptools.extension import Extension
from Cython.Build import cythonize

with open("VERSION", "r") as f_ver:
    VERSION = f_ver.read()

if sys.version_info[:2] < (2, 7):
    raise RuntimeError("Python version 2.7 required.")

if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

extensions = []
for directory in [directories to load: "","",""]:
    extensions.extend([Extension(directory.replace("/", ".") + "." + item[:-3], [os.path.join(directory, item)])
                       for item in os.listdir(directory) if item.endswith(".py") and "__" not in item])

ext_params = {
    "force": True,
    "compiler_directives": {
        "language_level": 3,
        "warn.unreachable": False
    }
}

setup(
    name="package_name",
    version=VERSION,
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Natural Language :: English",
                 "License :: OSI Approved :: Apache Software License",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Operating System :: MacOS :: MacOS X",
                 "Operating System :: POSIX :: Linux",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "Topic :: Software Development :: Libraries",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence",
                 "Topic :: Scientific/Engineering :: Information Analysis",
                 "Topic :: Internet"],
    keywords=[],
    url="doc_url",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "scikit-learn", "tqdm==4.32.1"],
    include_package_data=True,
    ext_modules=cythonize(extensions, **ext_params)
)
