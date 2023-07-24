""" Setup file for Python MVC Shell Framework Package """

from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding="utf-8") as f:
    requirements = f.readlines()

LONG_DESCRIPTION_CONS = '''Python MVC Shell Framework Package is a tiny
framework for shell projects in Python.'''
KEYWORDS_CONS = '''pmvcs, python shell, python mvc, python shell
framework, python mvc, python mvc shell framework'''

setup(
    name='pmvcs',
    version='1.0.0',
    author='Gonzalo Mahserdjian',
    author_email='gsmx64@outlook.com',
    url='https://github.com/gsmx64/pmvcs',
    description='Python MVC Shell Framework Package',
    long_description=LONG_DESCRIPTION_CONS,
    long_description_content_type="text/markdown",
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    package_data={'pmvcs': ['app/*',]},
    entry_points={
            'console_scripts': [
                'pmvcs = pmvcs:main',
                'pmvcs.cli = pmvcs.cli:main'
            ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    keywords=KEYWORDS_CONS,
    install_requires=requirements,
    zip_safe=False
)
