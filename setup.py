from setuptools import setup, find_packages
import os.path

here = os.path.dirname(__file__)
descr_file = os.path.join(here, "README.md")

setup(
    name="pyff",
    version="0.0.1",
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    description=f"pyff is a wrapper for the Flyff Project M API",
    long_description=open(descr_file).read(),
    author="Donovan Wright",
    url="https://github.com/Donny208/pyff",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    install_requires=["requests"],
)