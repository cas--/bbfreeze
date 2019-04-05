#! /usr/bin/env py.test
from __future__ import print_function

import os
import sys

import py

pyexe = py.path.local(sys.executable)


def check_encoding():
    enc = pyexe.sysexec("ex-fsenc.py")
    print("ENC:", enc)
    enc_frozen = py.path.local("dist/ex-fsenc").sysexec()
    assert enc == enc_frozen


def test_getfilesystemencoding(monkeypatch):
    os.system("bbfreeze ex-fsenc.py")

    monkeypatch.setenv("LANG", "en_US.UTF-8")
    check_encoding()

    monkeypatch.setenv("LANG", "")
    check_encoding()

    monkeypatch.setenv("LANG", "de_AT@euro")
    check_encoding()
