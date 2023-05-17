
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = [c.strip() for c in f.readlines()]

setup(name="wagon_common",
      version="0.2.14",
      description="Le Wagon common packages",
      url="https://github.com/lewagon/python-utilities/",
      author="Sébastien Saunier",
      author_email="seb@lewagon.org",
      packages=find_packages(),
      include_package_data=True,  # use MANIFEST.in
      install_requires=requirements)
