import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Poisson(Distribution):
    """ Poisson distribution class for calculating and
    visualizing a Poisson distribution.

    Attributes:

        mean (float): the mean value of the distribution
        stdev (float): the standard deviation of the distribution

        data (list of floats): extracted from the data file

        lmbda (float): rate of the poisson distribution
        (missing an 'a' to prevent name clash with Python keyword)

    """
    def __init__(self, lmbda):

        self.lmbda = lmbda

        Distribution.__init__(self,
                              self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """ Method to calculate the mean from lambda

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: mean of the distribution
        """
        self.mean = math.sqrt(self.lmbda)

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """ Method to calculate the standard deviation from lmbda

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: standard deviation of the distribution
        """
        self.stdev = math.sqrt(self.lmbda)

        return round(self.stdev, round_to)

    def calculate_pdf(self, x, round_to=2):
        """ Probability density function calculator for the Poisson distribution.

        Args:
            x (float): point for caluclating the probability density function
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: probability density function
        """

        self.pdf = self._calc_discrete_pdf(x)
        return round(self.pdf, round_to)

    def calculate_cdf(self, x, round_to=2):
        """  Probability density function calculator for the Poisson distribution.
            Args:
                x (float): point for calculating the probability density function
                round_to (int): Round the mean value.
                [Default value: 2 floating point]

            Returns:
                float: probability density function output
        """
        value = 0
        for i in range(0, x + 1):
            value += self._calc_discrete_pdf(i)
        self.cdf = value
        return round(value, round_to)

    def _calc_discrete_pdf(self, x):
        """ Internal function to calculate probability density function at a point.
        Should not be used by end user.

        Args:
            x (int): point for calculating the mean value.
        """
        fact = math.factorial(x)
        pdf = (math.exp(-self.lmbda) * self.lmbda ** x) / fact
        return pdf

    def plot_bar_pdf(self, points=100):
        """ Method to plot the pdf of the Poisson distribution.

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
            y.append(self._calc_discrete_pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title("Probability Mass Plt for Poisson Distribution")
        plt.ylabel("Probability")
        plt.xlabel("x")

        plt.show()

        return x, y

    def __repr__(self):
        """  Method to output the characteristics of the Poisson instace.
        Args:
            None
        Returns:
            string: characteristics of the Poisson
        """

        return "mean {0}, standard deviation {1}, lambda {2}".format(self.mean,
                                                                     self.stdev, self.lmbda)
