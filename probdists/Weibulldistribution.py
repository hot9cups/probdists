import math
import numpy as np
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class Weibull(Distribution):
  """ Weibull distribution class for calculating and
  visualizing a Weibull distribution.

  Attributes:

      mean (float): the mean value of the distribution
      stdev (float): the standard deviation of the distribution

      data (list of floats): extracted from the data file

      lmbda (float): scale parameter of the distribution
      (missing an 'a' to prevent name clash with Python keyword)
      k (float): shape parameter of the distribution

  """
  def __init__(self, lmbda=1, k=1.5):
    self.lmbda = lmbda
    self.k = k
    self.calculate_mean()
    self.calculate_stdev()

  def calculate_mean(self, round_to=2):
    """ Method to calculate the mean

    Args:
        round_to (int): Round the mean value. [Default value: 2 floating point]

    Returns:
        float: mean of the distribution
    """
    gamma_factor = math.gamma(1 + (1 / self.k))
    self.mean = self.lmbda * gamma_factor
    return round(self.mean, round_to)

  def calculate_stdev(self, round_to=2):
    """ Method to calculate the standard deviation

    Args:
        round_to (int): Round the mean value. [Default value: 2 floating point]

    Returns:
        float: standard deviation of the distribution
    """
    first = math.gamma(1 + (2 / self.k))
    second = math.gamma(1 + (1 / self.k)) ** 2
    self.stdev = math.sqrt(self.lmbda ** 2 * (first - second))
    return round(self.stdev, round_to)

  def calculate_pdf(self, x, round_to=2):
    """ Probability density function calculator for the Weibull distribution.

    Args:
        x (float): point for caluclating the probability density function
        round_to (int): Round the mean value. [Default value: 2 floating point]

    Returns:
        float: probability density function
    """
    if x < 0:
      out = 0
    else:
      exp_factor = math.exp(-(x / self.lmbda) ** self.k)
      out = (self.k / self.lmbda) * exp_factor * \
            (x / self.lmbda) ** (self.k - 1)
    return round(out, round_to)

  def calculate_cdf(self, x, round_to=2):
    """
    Cumulative density function calculator for the Weibull distribution.
    Args:
        x (float): point for calculating the cumulative density function
        round_to (int): Round the mean value. [Default value: 2 floating point]

    Returns:
        float: cumulative density function output
    """
    if x < 0:
      out = 0
    else:
      out = 1 - math.exp(-(x / self.lmbda) ** self.k)
    return round(out, round_to)

  def plot_pdf(self, samples=250):
    """ Method to plot the pdf of the Weibull distribution.

    Args:
        samples (int): number of discrete data points

    Returns:
        list: y values for the pdf plot

    """
    x = np.linspace(0, 2.5, num=samples)
    y = np.zeros_like(x)

    for index, value in enumerate(x):
      y[index] = self.calculate_pdf(value)

    plt.plot(x, y, label=f"lambda={self.lmbda}; k={self.k}")
    plt.legend()
    plt.title(f"Probability Distribution Function for Weibull \
              Distribution lambda={self.lmbda} k={self.k}")
    plt.show()
    return y

  def __repr__(self):
    """ Method to output the characteristics of the Weibull instace.
    Args:
        None
    Returns:
        string: characteristics of the Weibull
    """
    return f"lambda: {self.lmbda}, k: {self.k}, mean: {self.mean}, \
            standard deviation: {self.stdev}"
