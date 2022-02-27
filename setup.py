from codecs import open
import os
from setuptools import setup, find_packages

# import pypandoc

with open("README.md") as readme_file:
    README = readme_file.read()


VERSION = "0.0.1"
DESCRIPTION = "Option pricer and visualizer"
# LONG_DESCRIPTION = DESCRIPTION
URL = "https://github.com/westonplatter/finx-option-pricer"

deps = [
    "loguru",
    "pandas >=1.3.0,<1.4",
    "numpy",
    "matplotlib==3.4.2",
    "pydantic",
    "requests",
    "seaborn==0.11.1",
    "yfinance==0.1.59",
]

# Setting up
setup(
    name="finx_option_pricer",
    version=VERSION,
    author="westonplatter",
    author_email="westonplatter@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    url=URL,
    license="MIT",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=deps,
)
