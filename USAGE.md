# For Gaussian Distribution

```
>>> from probdists import Gaussian

>>> gaussian = Gaussian()
>>> gaussian.read_data_file('demo_gaussian_data')
# for your own file, replace 'demo_gaussian_data' with 'my_text_file.txt'

# to access data
>>> print(gaussian.data)
[1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31]

# to calculate mean
>>> print(round(gaussian.calculate_mean(), 2))
78.09

# to calculate standard deviation
>>> print(round(gaussian.calculate_stdev(),2))
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

# For Binomial Distribution
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
>>> print(round(binomial.calculate_stdev(), 2))
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
