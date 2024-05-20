import setuptools
import json

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

codemeta = open('codemeta.json')
with open('./codemeta.json', 'r') as f:
    code_setup = json.load(f)


__version__ = code_setup['version']

REPO_NAME = code_setup['name']
AUTHOR = code_setup['author']
SRC_REPO = "textSummarizer"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    description="A python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=code_setup['codeRepository'],
    keywords= code_setup['keywords'],
    dateCreated = code_setup['dateCreated'],
    programmingLanguage= code_setup['programmingLanguage'],
    softwareRequirements = code_setup['softwareRequirements'],
    project_urls={
        "Bug Tracker": f"{code_setup['codeRepository']}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)