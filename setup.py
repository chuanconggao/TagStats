#! /usr/bin/env python3

from setuptools import setup

url = "https://github.com/chuanconggao/TagStats"
version = "0.1.2"

setup(
    name="TagStats",

    packages=["tagstats"],

    url=url,

    version=version,
    download_url=f"{url}/tarball/{version}",

    license="MIT",

    author="Chuancong Gao",
    author_email="chuancong@gmail.com",

    description="Statistics for each tag's set of key phrases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    keywords=[
        "sentiment-analysis",
        "string-search"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],

    python_requires=">= 3",
    install_requires=[]
)
