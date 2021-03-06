import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tremulator",
    version="0.0.5",
    author="Stijn Debackere",
    author_email="debackere@strw.leidenuniv.nl",
    description="A package to emulate expensive functions using Gaussian processes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StijnDebackere/tremulator",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "asdf",
        "emcee",
        "george @ git+https://github.com/StijnDebackere/george",
        "pyDOE",
        "tqdm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
