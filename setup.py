#! /usr/bin/env python

import sys

from setuptools import setup


def get_version():
    d = {}
    try:
        file_ = "bbfreeze/__init__.py"
        exec(compile(open(file_).read(), file_, 'exec'), d)
    except Exception:
        pass
    return d["__version__"]


version = get_version()


def main():
    install_requires = [
        "altgraph>=0.12",
        "bbfreeze-loader>=1.1.0,<1.2.0",
        "modulegraph>=0.12",
    ]

    if sys.platform == "win32":
        install_requires.append("pefile")

    setup(
        name="bbfreeze",
        version=version,
        entry_points={
            "console_scripts": [
                "bb-freeze = bbfreeze:main",
                "bbfreeze = bbfreeze:main",
            ],
            "distutils.commands": [
                "bdist_bbfreeze = bbfreeze.bdist_bbfreeze:bdist_bbfreeze"
            ],
        },
        install_requires=install_requires,
        packages=["bbfreeze"],
        zip_safe=False,
        maintainer="Ralf Schmitt",
        maintainer_email="ralf@systemexit.de",
        url="https://pypi.python.org/pypi/bbfreeze/",
        description="create standalone executables from python scripts",
        platforms="Linux Windows",
        license="zlib/libpng license",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "License :: OSI Approved :: zlib/libpng License",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.4",
            "Programming Language :: Python :: 2.5",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Build Tools",
            "Topic :: System :: Software Distribution",
        ],
        long_description=open("README.rst").read(),
    )


if __name__ == "__main__":
    main()
