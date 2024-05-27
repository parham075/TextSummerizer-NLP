import setuptools
import json
from io import open

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


console_scripts = []

console_scripts.append(
    "{0}={1}.main:main".format(
        find_packages("src")[0].replace("_", "-"), find_packages("src")[0]
    )
)

setup(
    entry_points={"console_scripts": console_scripts},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)