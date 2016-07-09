#!/usr/bin/env python3

import sys
import os
import stat

from setuptools import setup
from setuptools.command.install import install
from distutils import log

import speech_recognition

if sys.version_info < (3,3):
    print("THIS MODULE REQUIRES PYTHON 3.3+ ::: Currently Using PYTHON {0}".format(sys.version))
    sys.exit(1)

setup(
    name = "KoboHomeAssistant",
    )
