# setup.py
import setuptools
from setuptools import setup

setup(
    name="python_example",
    install_requires=[
        "numpy",
        "pandas==1.5.3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(
        where='src',
    ),
)
