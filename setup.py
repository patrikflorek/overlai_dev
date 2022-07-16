import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="overlai",
    version="0.1.0-alpha",
    description="A Kivy derived UI widget on which can be drawn on by a finger.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/patrikflorek/overlai",
    author="Patrik Florek",
    author_email="patrik.florek@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha" "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: User Interfaces",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["kivymd"],
)
