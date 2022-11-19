#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Jiongbin0202
# Created Time:  2022-11-19 19:37:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "serviceCCOVE",
    version = "0.1.0",
    keywords = ("pip", "arcpy","websocket", "magetool", "mage"),
    description = "serviceCove analysis tools",
    long_description = "serviceCove analysis tools",
    license = "MIT Licence",

    url = "https://github.com/Jiongbin0202/serviceCCOVE",
    author = "Jiongbin0202",
    author_email = "c2218239@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
