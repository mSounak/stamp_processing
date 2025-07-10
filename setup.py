# -*- coding: utf-8 -*-
"""
Created on  
@author: Sun* AI Research Team
"""
import sys

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    "gdown>=4.7.1",
    "Pillow>=10.0.0",
    "opencv-python>=4.8.0",
    "torch>=2.0.0",
    "torchvision>=0.15.0",
    "fastai>=2.7.0",
    "numpy>=1.21.0",
    "PyYAML>=6.0",
    "setuptools>=65.0.0",  # for pkg_resources
]

DISTNAME = "better_stamp_processing"
DESCRIPTION = "Stamp processing package"
AUTHOR = "Sun* AI Research Team"
EMAIL = "sun.converter.team@gmail.com"
URL = "https://github.com/mSounak/stamp_processing/"
DOWNLOAD_URL = "https://github.com/mSounak/stamp_processing/"


setup(
    name=DISTNAME,
    author=AUTHOR,
    author_email=EMAIL,
    use_scm_version={
        "write_to": "stamp_processing/__version__.py",
        "version_scheme": "guess-next-dev",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    project_urls={
        "Bug Tracker": "https://github.com/mSounak/stamp_processing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.8",
    include_package_data=True
)
