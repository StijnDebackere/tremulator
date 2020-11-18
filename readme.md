# Function emulation using Gaussian processes

`tremulator` provides the `Emulator` class for easy emulation
of expensive functions with user-defined training and acquisition
functions. It is built upon [`george`](https://github.com/dfm/george)
and allows the trained emulator to be saved to an
[`asdf`](https://github.com/spacetelescope/asdf) file. The saved file
can be read by the `Interpolator` class which then requires no more
training.

## Installation

### Using pip

`tremulator` is available on [PyPI](https://pypi.org/), install using

```
pip install tremulator --upgrade
```

### Github

The package can be installed from Github by running the following
commands in the preferred installation location:
```
git clone https://github.com/StijnDebackere/tremulator
cd tremulator
pip install .
```

### Dependencies
`tremulator` will automatically install the following packages
- numpy
- scipy
- asdf
- emcee
- george
- pyDOE
- tqdm
