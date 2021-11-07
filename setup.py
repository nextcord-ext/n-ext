from setuptools import setup
import re

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = "2021.3.1"
extras_require = {
    'menus': [
        'nextcord-ext-menus==1.3.2',
    ],
    'ipc': [
        'nextcord-ext-ipc==2.2.1',
    ],
    'events': [
        'nextcord-ext-events==0.1.0a0',
    ],
    'alternatives': [
        'nextcord-ext-alternatives==2021.1',
    ],
    'core': ['nextcord==2.0.0a3'],
        
    'lava': [
        'nextcord-ext-lava==3.1.4'],
        
    'music': [
        'nextcord-ext-lava==3.1.4'],
}

setup(
    name="n-ext",
    author="nextcord-ext",
    python_requires=">=3.8.0",
    url="https://github.com/nextcord-ext/n-ext",
    version=version,
    license="Apache Software License",
    description="Project interface for nextcord-ext's",
    install_requires=requirements,
    extras_require=extras_require,
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
