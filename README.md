# probdists

Python package to model probability distributions.<br>
Currently supports Gaussian, Gamma, Binomial, Bernoulli and Exponential Distributions.

## Usage
Please see [usage](USAGE.md)

## Installation

Installing using pip:
```
>>> pip install probdists
```

Installing using virtual-environment(recommended):
```
>>> conda create -n myEnv python=3.6 anaconda
>>> conda activate myEnv
>>> pip install probdists
```

You can find the project on PyPi [here](https://pypi.org/project/probdists/)


## Files

The main classes are inside the probdists folder
-   [Generaldistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Generaldistribution.py) is the base class
-   [Gaussiandistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Gaussiandistribution.py), [Binomialdistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Binomialdistribution.py), [Bernoullidistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Bernoullidistribution.py), [Gammadistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Gammadistribution.py) and [Exponentialdistribution.py](https://github.com/hot9cups/probdists/blob/main/probdists/Exponentialdistribution.py) are subclasses of Generaldistribution.py
-   [numbers.txt](https://github.com/hot9cups/probdists/blob/main/probdists/numbers.txt), [numbers_binomial.txt](https://github.com/hot9cups/probdists/blob/main/probdists/numbers_binomial.txt), [numbers_bernoulli.txt](https://github.com/hot9cups/probdists/blob/main/probdists/numbers_bernoulli.txt), [numbers_gamma.txt](https://github.com/hot9cups/probdists/blob/main/probdists/numbers_gamma.txt) and [numbers_exponential.txt](https://github.com/hot9cups/probdists/blob/main/probdists/numbers_exponential.txt) are sample data files
-   [tests.py](https://github.com/hot9cups/probdists/blob/main/test.py) contains unittests for the package

## Licence

[MIT Licence](LICENCE.txt)
