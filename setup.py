"""
Python packaging file for setup tools.
"""

# isort: STDLIB
import os

# isort: THIRDPARTY
import setuptools


def local_file(name):
    """
    Function to obtain the relative path of a filename.
    """
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


with open(local_file("src/into_dbus_python/_version.py"), encoding="utf-8") as o:
    exec(o.read())  # pylint: disable=exec-used

with open(local_file("README.rst"), encoding="utf=8") as o:
    long_description = o.read()

setuptools.setup(
    name="into-dbus-python",
    version=__version__,  # pylint: disable=undefined-variable
    author="Anne Mulhern",
    author_email="amulhern@redhat.com",
    description="transforms values into properly wrapped dbus-python objects",
    long_description=long_description,
    platforms=["Linux"],
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["dbus-signature-pyparsing", "dbus-python>=1.2.10"],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    url="https://github.com/stratis-storage/into-dbus-python",
)
