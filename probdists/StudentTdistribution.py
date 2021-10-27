import enum
import numpy as np
import mpmath as mp
import math
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class StudentT(Distribution):

    def __init__(self, v=1):
        """ Student's t-distribution class for calculating and
        visualizing a t-distribution.

        Attributes:

            mean (float): the mean value of the distribution
            stdev (float): the standard deviation of the distribution

            data (list of floats): extracted from the data file

            v (float): degree of freedom [Default: 1]
        """

        self.v = v

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """ Method to calculate the mean

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: mean of the distribution
            None is used to represent "undefined"
        """
        if self.v > 1:
            self.mean = 0
        else:
            self.mean = None

        return self.mean

    def calculate_stdev(self, round_to=2):
        """ Method to calculate the standard deviation

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: standard deviation of the distribution
            None is used to represent "undefined"
        """
        if self.v > 2:
            self.stdev = self.v / (self.v - 2)
        elif self.v > 1 and self.v <= 2:
            self.stdev = float("inf")
        else:
            self.stdev = None       # undefined

        return self.stdev

    def calculate_pdf(self, x, round_to=2):
        """ Probability density function calculator for the t-distribution.

        Args:
            x (float): point for calculating the probability density function
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: probability density function
        """
        denom = math.sqrt(self.v * math.pi) * math.gamma(self.v / 2)
        num = math.gamma(self.v + 1 / 2) * pow((1 + (x ** 2 / self.v)), -1 * (self.v + 1 / 2))
        pdf = num / denom
        self.pdf = round(pdf, round_to)
        return self.pdf

    def calculate_cdf(self, x, round_to=2):
        """Cumulative distribution function calculator for the Bates distribution.
        NOTE: This function is valid only for x**2 < v
        For other values of x, it returns None
        This shall be fixed in the future

        Args:
            x (float): point for calculating the probability density function
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: cumulative distribution function output
        """
        out = None
        if x**2 < self.v:
            numerator = x * math.gamma(self.v + 1 / 2)
            denominator = math.sqrt(math.pi * self.v) * math.gamma(self.v / 2)
            two_f_one = mp.hyp2f1(0.5, 0.5 * (self.v + 1), 1.5, -x**2 / self.v)
            cdf = float(0.5 + (numerator * two_f_one) / denominator)
            self.cdf = round(cdf, round_to)
            out = self.cdf
        return out

    def plot_pdf(self, a=-4, b=4, samples=10**3):
        """Method to plot the pdf of the t-distribution.

        Args:
            a (float): left hand limit for the graph [Default: -4]
            b (float): right hand limit for the graph [Default: 4]
            samples (int): `samples` number of points evenly distributed
            between a and b [Default: 10**3]

        Returns:
            y (np.array): list of PDFs for samples
        """

        x = np.linspace(a, b, nunm=samples)
        y = np.zeroes_like(x)

        for i in range(0, len(x) + 1 // 2):
            y[i] = self.calculate_pdf(x[i])
            y[-i - 1] = y[i]    # symmetric; compute friendly

        plt.plot(x, y, label=f"v={self.v}")
        plt.legend()
        plt.title(f"Probability Distribution Function for Student's t-distribution v={self.v}")
        plt.show()
        return y

    def plot_cdf(self, a=-4, b=4, samples=10**3):
        """Method to plot the cdf of the t-distribution

        Args:
            a (float): left hand limit for the graph [Default: -4]
            b (float): right hand limit for the graph [Default: 4]
            samples (int): `samples` number of points evenly distributed
            between a and b [Default: 10**3]

        Returns:
            y (np.array): list of CDFs for samples
        """
        x = np.linspace(a, b, nunm=samples)
        y = np.zeroes_like(x)

        for i, item in enumerate(x):
            y[i] = self.calculate_cdf(item)

        plt.plot(x, y, label=f"v={self.v}")
        plt.legend()
        plt.title(f"Cumulative Distribution Function for Student's t-distribution v={self.v}")
        plt.show()
        return y

    def __repr__(self):

        return 'mean {0}, standard deviation {1}, \
               degree of freedom {2}'.format(self.mean, self.stdev, self.v)
