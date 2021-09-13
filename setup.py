#!/usr/bin/env python
import os

from setuptools import find_packages, setup

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def read_file(relative_path: str) -> str:
    """Return the content of a file.

    :param relative_path: relative path to the file to read
    :type relative_path: str
    :return: the content of the file
    :rtype: str
    """
    with open(os.path.join(_BASE_DIR, relative_path), "r") as file:
        return file.read()


def get_version() -> str:
    """Return the version of the package.

    :return: the version of the package
    :rtype: str

    :raise RuntimeError: if no package version found
    """
    for line in read_file("pairing/__init__.py").splitlines():
        if line.startswith("__version__"):
            return line.split('"' if '"' in line else "'")[1]
    raise RuntimeError("Unable to find package version")


setup(
    name="dgfip-pairing",
    author="Yannis Tannier",
    author_email="tannier.yannis@gmail.com",
    url="https://github.com/yannistannier/pairing",
    version=get_version(),
    packages=find_packages(exclude=["tests*"]),
    description="Librairie de pairing entre 2 bases de donnees",
    long_description=read_file("README.md") + "\n\n" + read_file("CHANGES.md"),
    install_requires=[
        "click==8.0.1",
        "numphy==0.0.1",
        "pandas==1.3.3",
        "rapidfuzz[speed]==1.6.1",
    ],
    extras_require={
        "development": [
            "bandit==1.7.0",
            "black==21.8b0",
            "isort==5.9.3",
            "pylint==2.10.2",
            "pytest-cov==2.12.1",
            "pytest==6.2.5",
            "xenon==0.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dgfip-pairing=pairing.cli:cli",
        ],
    },
    include_package_data=True,
)
