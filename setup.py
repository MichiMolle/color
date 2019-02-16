import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-color",
    version="0.0.1",
    author="Michael Moeller",
    author_email="github@mk-moeller.de.com",
    description="Easy color manipulation",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
)