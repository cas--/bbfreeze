#! /usr/bin/env py.test

import os
import sys

import bbfreeze


def test_icon():
    if sys.platform == "win32":
        f = bbfreeze.Freezer()
        f.addScript("ex-mbox.py", False)
        f.setIcon("python.ico")
        f()
        err = os.system("dist\\ex-mbox")
        assert err == 0


if __name__ == "__main__":
    test_icon()
