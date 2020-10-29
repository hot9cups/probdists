# Usage

## For Gaussian Distribution

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
>>> print(gaussian.pdf(25))
0.00365

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

## For Binomial Distribution

```
>>> from probdists import Binomial

>>> binomial = Binomial()
>>> binomial.read_data_file('demo_binomial_data')

# to access data
>>> print(binomial.data)
[0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]

# to calculate mean    
>>> print(binomial.calculate_mean())
8

# to calculate standard deviation
>>> print(binomial.calculate_stdev())
2.19

# to calculate p and n from the data set
>>> p, n = binomial.replace_stats_with_data()
>>> print(round(p,3))
0.615
>>> print(n)
13
        
# to calculate pdf
>>> print(round(binomial.pdf(5), 5))
0.07465

# to add two individual distributions
>>> binomial_one = Binomial(.4, 20)
>>> binomial_two = Binomial(.4, 60)
>>> binomial_sum = binomial_one + binomial_two
        
>>> print(binomial_sum.p)
0.4
>>> print(binomial_sum.n)
80

# plot bar graph of data
>>> binomial.plot_bar()

# plot bar graph of probability distribution function of data
>>> binomial.plot_bar_pdf()
```

## For Exponential Distribution 

```
>>> from probdists import Exponential 

# default value of lmbda(rate) is 0.5 
>>> exponential = Exponential()

>>> exp_2 = Exponential(0.25)
# rate of exp_2 is 0.25 

>>> exponential.read_data_file('demo_exponential_data')
# pass in your filename to read data from filename

# to access data 
>>> print(exponential.data)
[1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31] 

# to calculate mean
>>> print(exponential.calculate_mean())
2.0 

# to calculate standard deviation 
>>> print(exponential.calculate_stdev())
2.0 

# to calculate pdf 
>>> print(round(exponential.pdf(5), 5))
0.04104

# plot pdf of exponential distribution 
>>> exponential.plot_bar_pdf() 
```

## For Gamma Distribution
```
>>> from probdists import Gamma

# By default Gamma will create a gamma dist. with k=2, theta=2 and won't fit to data
# This is useful if you want a simple Gamma distribution to play around with the pdf
# HOWEVER: It will not make use of data passed into the distribution
>>> gamma = Gamma()

# To use of the sample data or your own data, and approximate a gamma fit to that data:
>>> gamma = Gamma(fit=True, data_file='demo_gamma_data')
# for your own file, replace 'demo_gamma_data' with 'my_data_file.txt' 
# Ensure there is no extra whitespace at end of file
# The sample data will fit k=2 (rounded to integer), theta~=2.37

# The above is IMPORTANT. 
# If you don't specify fit=true the Gamma distribution won't fit 
# but will model using default or inputted k & theta
# If you specify fit, Gamma distribution will fit and disregard any k,theta argument
# To provide data for fitting a new Gamma instance will need to be made

# to calculate mean:
>>> print(gamma.calculate_mean())

# to calculate standard deviation:
>>> print(gamma.calculate_stddev())

# to calculate pdf, call function and give argument x
>>> print(gamma.pdf(x))
0.18165

# to access data 
>>> print(gamma.data)
[1, 2, 2, 3, 3, 4, 5, 6, 8, 9, 13]

# plot pdf of exponential distribution 
>>> gamma.plot_bar_pdf() 

# to add two gamma distributions
>>> gamma_one = Gamma(2, 2)
>>> gamma_two = Gamma(1, 2)
>>> gamma_three = gamma_one + gamma_two
# The resulting gamma three will have k=3, theta=2. 
# This add magic method fails if thetas are not equal since they wouldn't be summable
```
