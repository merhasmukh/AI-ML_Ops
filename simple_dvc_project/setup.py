from setuptools import setup,find_packages


with open("README.md","r",encoding="UTF-8") as f:
    long_description=f.read()


setup(
    name="src",
    version="0.0.1",
    author="hasmukh",
    description="A small package for DVC ML pipeline demo"
    long_description=long_description,
    author_email="mhgn0001@gmail.com"
)