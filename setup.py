# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tigju_lambdata",  # the name that you will install via pip
    version="1.0",
    author="Iuliia Stanina",
    author_email="your@email.com",
    description="A few basic functions for wrangling data",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/tigju/lambddata-iuliiastanina",
    #keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
