#! /usr/bin/env python

from __future__ import print_function
import sys, os

print(sys.getfilesystemencoding(), os.environ.get("LANG", "<>"))
