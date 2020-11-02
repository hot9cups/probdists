import math
from typing import List, Tuple

import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Gamma(Distribution):
    """ Gamma distribution class for calculating and visualizing a Gamma distribution.
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) extracted from the data file
            k (float) shape parameter representing shape of distribution (k > 0)
            theta (float) scale parameter that stretches/shrinks distribution (theta > 0)
    """

    def __init__(self, k=2, theta=2):
        """
        Init function to instantiate Gamma distribution
            Args:
                k (float) shape parameter representing shape of distribution (k > 0)
                theta (float) scale parameter that stretches/shrinks distribution (theta > 0)
        """
        if k <= 0 or theta <= 0:
            raise ValueError(f"k and theta must be > 0, k: {k}, theta: {theta}")
        self.k = k
        self.theta = theta
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """
        Function to calculate the mean of the data set.
            Args:
                 round_to (int): Round the mean value. [Default value: 2 floating point]
            Returns:
                   float: mean of the data set
        """
        avg = self.k * self.theta
        self.mean = avg
        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """
        Function to calculate the standard deviation of the data set.
            Args:
                 sample (bool): whether the data represents a sample or population
                 round_to (int): Round the mean value. [Default value: 2 floating point]
            Returns:
                float: standard deviation of the data set
        """
        self.stdev = math.sqrt(self.k * math.pow(self.theta, 2))
        return round(self.stdev, round_to)

    def calculate_pdf(self, x, round_to=2):
        """
        Probability density function calculator for the Gamma distribution.
            Args:
                x (float): point for calculating the probability density function
                round_to (int): Round the mean value. [Default value: 2 floating point]

            Returns:
                float: probability density function output
        """
        self.pdf = (
            (1 / (math.factorial(self.k - 1) * math.pow(self.theta, self.k)))
            * (math.pow(x, self.k - 1))
            * (math.exp((-1 * x / self.theta)))
        )
        return round(self.pdf, round_to)

    def cdf(self, x: float) -> float:
        pass

    def plot_bar_pdf(self, points=25):
        """
        Method to plot the pdf of the exponential distribution.
            Args:
                points (int): number of discrete data points
            Returns:
                list: x values for the pdf plot
                list: y values for the pdf plot
        """
        x = []
        y = []

        # calculate the x values to visualize (doesn't reuse the old data)
        for i in range(points + 1):
            x.append(i)
            self.calculate_pdf(i)
            y.append(self.pdf)

        # make the plots
        plt.bar(x, y)
        plt.title("Probability Density Plot for Gamma Distribution")
        plt.ylabel("Probability")
        plt.xlabel("x")

        plt.show()
        return x, y

    def plot_histogram(self):
        pass

    def plot_histogram_pdf(self, n_spaces: int) -> Tuple[List[float], List[float]]:
        pass

    def __add__(self, other):
        """
        Function to add together two Gamma distributions
            Args:
                other (Gamma): Gamma instance
            Returns:
                Gamma: Gamma distribution
        """
        if self.theta == other.theta:
            result = Gamma()
            result.k = self.k + other.k
            result.theta = self.theta
            result.calculate_mean()
            result.calculate_stdev()
            return result

    def __repr__(self):
        """
        Function to output the characteristics of the Gamma instance
            Args:
               None
            Returns:
               string: characteristics of the Gamma
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
