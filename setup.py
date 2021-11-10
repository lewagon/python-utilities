
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="wagon_common",
      version="0.2.0",
      description="Le Wagon common packages",
      packages=find_packages(),
      install_requires=requirements)
