## probdists

### Overview  

`probdists` is a Python package to model probability distributions.  
Supports Bernoulli, Binomial, Exponential, Gamma, Gaussian, Triangular, and Uniform Distributions with support for Poisson, Bates, and Irwin-Hall on the way!  

For usage, see [here](#usage).

### Installation 

Installing using pip:
```
>>> pip install probdists
```

Installing using virtual-environment (recommended):
```
>>> conda create -n myEnv python=3.6 anaconda
>>> conda activate myEnv
>>> pip install probdists
```

You can find the project on PyPi [here](https://pypi.org/project/probdists/).

### Usage  

Here, we shall demonstrate a general workflow by taking a particular class, say, Gaussian. 

After installation, we can likewise interact with the package:  

```
>>> from probdists import Gaussian

>>> gaussian = Gaussian()
>>> gaussian.read_data_file('demo_gaussian_data')
# for your own file, replace 'demo_gaussian_data' with 'my_text_file.txt'

# to access data
>>> print(gaussian.data)
[1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31]

# to calculate mean
>>> print(gaussian.calculate_mean())
78.09

# to calculate standard deviation
>>> print(gaussian.calculate_stdev())
92.87

# to calculate pdf
>>> print(gaussian.calculate_pdf(25, 5))
0.00365

# to calculate cdf
>>> print(gaussian.cdf(25, 5))
0.28378

# to add two individual distributions
>>> gaussian_one = Gaussian(25, 3)
>>> gaussian_two = Gaussian(30, 4)
>>> gaussian_sum = gaussian_one + gaussian_two
>>> print(gaussian_sum.mean)
55
>>> print(gaussian_sum.stdev)
5.0

# plot histogram of data
>>> gaussian.plot_histogram()

# plot normalized histogram of data and plot of pdf along same range
>>> gaussian.plot_histogram_pdf(n_spaces = 50)
```

## Documentation   

### Distribution  

The Distribution class is a base class that all other concrete classes inherit from. It provides common fields such as `mean`, `stdev`, `pdf`, and `cdf` and implements `read_data_file()` function.  

> `read_data_file(self, file_name, separator='\\n', header=None)` 
Function to read in data from a txt file, csv file
and excel formats (xls, xlsx, xlsm, xlsb, odf, ods and odt)

The txt file should have one number (float) per line or
numbers should be separator seperated.

No need for separator argument with csv file, it will
by default be ',' so csv files should have , seperated
numbers

For excel file formats. There should only be one column
containing numbers, and if 0th row is header then header
argument should be 0. The numbers are taken from next row
mentioned in header parameter.

The numbers are stored in the data attribute.

**Args**:   
    file_name (string): name of a file to read from   
    separator (character): custom separator to use if required   
    header (int or by default None): to specify if excel file   
    contains header.    
**Returns**:   
    None    

You should instantiate a child of Distribution class and not this class itself.  

### Bernoulli Distribution   

Bernoulli distribution class for calculating and
    visualizing a Bernoulli distribution.

**Attributes**:   
    mean (float) representing the mean value of the distribution   
    stdev (float) representing the standard deviation of the distribution   
    data_list (list of floats) to be extracted from the data file   
    p (float) representing the probability of an event occurring (1). Default 0.5   

> ` __init__(self, prob=0.5)`   
Constructor function for Bernoulli class. 

**Args**:   
    p (float): representing the probability of an event occurring (1). Default 0.5
> `calculate_mean(self, round_to=2)`  
Method to calculate the mean of a Bernoulli distribution

**Args**:   
    round_to (int): Round the mean value. Defaults to 2.      
**Returns**:    
    float: mean of the data set      

> `calculate_stdev(self, round_to=2)`  
Function to calculate the standard deviation from p.

**Args**:   
    round_to (int): Round the mean value. Defaults to 2.     
**Returns**:   
    float: standard deviation of the data set.     

> `replace_stats_with_data(self)` 
Method to calculate p from the data set

**Args**:   
    None     
**Returns**:   
    float: the p value      

> `plot_bar(self)`  
Method to plot a histogram of the instance variable data using matplotlib pyplot library.

**Args**:   
    None   
**Returns**:  
    None   

> `calculate_pdf(self, k, round_to=2)`
Method to calculate pdf for the bernoulli distribution.

**Args**:   
    k (float): point for calculating the probability density function. Range of k: {0, 1}
    round_to (int): Round the mean value. [Default value: 2 floating point]   
**Returns**:   
    float: probability density function output   

> `calculate_cdf(self, k, round_to=2)` 
Method to calculate cdf for the bernoulli distribution.

**Args**:   
    k (float): point for calculating the cumulative distribution function   
    round_to (int): Round the mean value. [Default value: 2 floating point]   
**Returns**:   
    float: cumulative distribution function output   

> `plot_bar_pdf(self)`
Method to plot the pdf of the bernoulli distribution

**Args**:   
    None   
**Returns**:   
    list: x values for the pdf plot   
    list: y values for the pdf plot   

The Bernoulli class overrides `__add__()` and `__repr__()` functions to allow you to
add two objects and get characteristic about it, respectively.  

### Binomial Distribution   
Binomial distribution class for calculating and visualizing a Binomial distribution.

**Attributes**:   
    mean (float) representing the mean value of the distribution   
    stdev (float) representing the standard deviation of the distribution   
    data_list (list of floats) to be extracted from the data file   
    p (float) representing the probability of an event occurring   
    n (int) number of trials   

> `__init__(self, prob=.5, size=20)`  
Constructor function for Binomial Distribution.   

> `calculate_mean(self, round_to=2)`  
Function to calculate the mean from p and n

**Args**:   
    round_to (int): Round the mean value. [Default value: 2 floating point]   
**Returns**:   
    float: mean of the data set    

> `calculate_stdev(self, round_to=2)`   
Function to calculate the standard deviation from p and n.

**Args**:   
    round_to (int): Round the mean value. [Default value: 2 floating point]    
**Returns**:    
    float: standard deviation of the data set    

> `replace_stats_with_data(self)`   
Function to calculate p and n from the data set

**Args**:   
    None   
**Returns**:   
    float: the p value   
    float: the n value   

> `plot_bar(self)`  
Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

**Args**:   
    None   
**Returns**:   
    None   

> `calculate_pdf(self, k, round_to=2)`   
Probability density function calculator for the binomial distribution.

**Args**:   
    k (float): point for calculating the probability density function    
    round_to (int): Round the mean value. [Default value: 2 floating point]   
**Returns**:   
    float: probability density function output   

> `calculate_cdf(self, k, round_to=2)`   
Cumulative distribution function calculator for the binomial distribution.

**Args**:
    k (float): point for calculating the cumulative distribution function   
    round_to (int): Round the mean value. [Default value: 2 floating point]   
**Returns**:    
    float: cumulative distribution function output   

> `plot_bar_pdf(self)`   
Function to plot the pdf of the binomial distribution

**Args**:   
    None   
**Returns**:   
    list: x values for the pdf plot   
    list: y values for the pdf plot   

The Binomial class overrides `__add__()` and `__repr__()` functions to allow you to
add two objects and get characteristic about it, respectively.  

<!-- TODO:
### Gamma Distribution
### Gaussian Distribution
### Triangular Distribution
### Uniform Distribution -->

## Code Repository    

Please find the code repository for `probdists` [here](https://github.com/hot9cups/probdists/).   

## About   

<!-- TODO: Add demo plots in ## usage -->
<!-- TODO: Link to documentation page when page is online -->

## License  

`probdists` is distributed under [MIT License](LICENCE.txt).
