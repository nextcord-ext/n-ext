from setuptools import setup
import re

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = "2021.1"

setup(
    name="nextcord-ext-events",
    author="VincentRPS",
    python_requires=">=3.8.0",
    url="https://github.com/vincentrps/nextcord-ext-events",
    version=version,
    license="Apache Software License",
    description="Project interface for nextcord-ext's",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ]
)
