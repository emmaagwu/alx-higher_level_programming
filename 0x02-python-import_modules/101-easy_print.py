#!/usr/bin/python3
import os

with os.fdopen(1, 'w') as stdout:
    stdout.write("#pythoniscool\n")
