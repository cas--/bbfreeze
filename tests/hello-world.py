#! /usr/bin/env python

from __future__ import print_function, unicode_literals

import sys

print("hello".encode("utf8"), "world!".encode("ascii"))

print("sys.path:", sys.path)
print("__file__:", __file__)
print("__name__:", __name__)

print("locals():", locals())

print("sys.argv", sys.argv)
print("sys.executable:", sys.executable)
