# probdists

Python package to model probability distributions.<br>
Currently supports Gaussian and Binomial Distributions.

# Usage
Please see [usage](usage.MD)

# Installation

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


# Files

The main classes are inside the probdists folder
- Generaldistribution.py is the base class
- Gaussiandistribution.py and Binomialdistribution.py are subclasses of Generaldistribution.py
- numbers.txt and numbers_binomial.txt are sample data files
- tests.py contains unittests for the package

# Licence

[MIT Licence](LICENCE.txt)
