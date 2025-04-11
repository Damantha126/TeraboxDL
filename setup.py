import os
from typing import Dict
from setuptools import setup, find_packages

about: Dict = {}

base_path = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(
        base_path,
        'TeraboxDL',
        '__version__.py',
    ), encoding='utf-8',
) as f:
    exec(f.read(), about)

setup(
    name="terabox-downloader",
    version=about['__version__'],
    license="MIT",
    author="DamanthaJasinghe",
    author_email="damanthaja@gmail.com",
    description="TeraboxDL is a Python package for interacting with Terabox, enabling you to fetch file details such as name, download link, thumbnail, and size, and download files with support for custom progress tracking via a callback function.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Damantha126/TeraboxDL",
    packages=find_packages(),
    keywords=["terabox", "python-package","terabox-bypass", "terabox-downloader", "damanthaja", "mritzme", "damantha126", "direct-download", "jasinghe", "damantha-jasinghe"],
    install_requires=[
        "requests",
    ],
    project_urls={
        "Community": "https://t.me/SDBOTs_inifinity"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)