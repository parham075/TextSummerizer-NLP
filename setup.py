import setuptools
import json
from io import open

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('./codemeta.json', 'r') as f:
    code_setup = json.load(f)

__version__ = code_setup['version']

REPO_NAME = code_setup['name']
AUTHOR = code_setup['author']
SRC_REPO = "textSummarizer"
AUTHOR_USER_NAME = code_setup['author'][0]['username']
AUTHOR_EMAIL = code_setup['author'][0]['email']
console_scripts = []
description="A small python package for NLP app",
    

console_scripts.append(
    "{0}={1}.main:main".format(
        find_packages("src")[0].replace("_", "-"), find_packages("src")[0]
    )
)

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=description,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    entry_points={"console_scripts": console_scripts},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)