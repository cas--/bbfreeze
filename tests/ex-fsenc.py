#! /usr/bin/env python

from __future__ import print_function

import os
import sys

print(sys.getfilesystemencoding(), os.environ.get("LANG", "<>"))
