import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Exponential(Distribution):
    """ Exponential distribution class for calculating and
    visualizing a Exponential distribution.

    Attributes:

       mean (float): the mean value of the distribution
       stdev (float): the standard deviation of the distribution

       data (list of floats): extracted from the data file

       lmbda (float): rate of the exponential distribution (missing an 'a' to prevent name clash with Python keyword)

    """

    def __init__(self, lmbda=.5):

        self.lmbda = lmbda

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """ Method to calculate the mean from lambda

        Args:
            round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: mean of the distribution
        """

        self.mean = (1.0 / self.lmbda)

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """ Method to calculate the standard deviation from lmbda

        Args:
            round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: standard deviation of the distribution
        """

        self.stdev = (1.0 / self.lmbda)

        return round(self.stdev, round_to)

    def pdf(self, x):
        """ Probability density function calculator for the exponential distribution.

        Args:
            x (float): point for caluclating the probability density function
        Returns:
            float: probability density function
        """
        value = 0  # default value of exponential distribution for x < 0
        if x >= 0:
            value = self.lmbda * math.exp(-self.lmbda * x)
        return value

    def plot_bar_pdf(self, points=100):
        """ Method to plot the pdf of the exponential distribution.

        Args:
            points (int): number of discrete data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(points + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Probability Density Plot for Exponential Distribution')
        plt.ylabel('Probability')
        plt.xlabel('x')

        plt.show()

        return x, y

    #
    #   def __add__(self, other):
    #       """ Method to add together two Exponential distributions with
    #       """
    #       pass
    #

    def __repr__(self):
        """ Method to outputthe characteristics of the Exponential instace.
        Args:
            None
        Returns:
            string: characteristics of the Exponential
        """

        return "mean {0}, standard deviation {1}, lambda{2}".format(self.mean, self.stdev, self.lmbda)
