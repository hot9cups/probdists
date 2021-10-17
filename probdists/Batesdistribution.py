import math
import numpy as np
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class Bates(Distribution):

    def __init__(self, n=20, a=0, b=1):
        """ Bates distribution class for calculating and
        visualizing a Bates distribution.

        Attributes:

            mean (float): the mean value of the distribution
            stdev (float): the standard deviation of the distribution

            data (list of floats): extracted from the data file

            n (int): The number of samples
            a (int): The lower limit of distribution [Default: 0]
            b (int): The upper limit of distribution [Default: 1]
        """
        self.n = n
        self.a = a
        self.b = b
        Distribution.__init__(self,
                              self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """ Method to calculate the mean from n

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: mean of the distribution
        """
        self.mean = 0.5 * (self.a + self.b)

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """ Method to calculate the standard deviation from n

        Args:
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: standard deviation of the distribution
        """
        var = (self.b - self.a) / (12 * self.n)

        self.stdev = math.sqrt(var)

        return round(self.stdev, round_to)

    def _fx(self, x):
        """ Internal function to calculate probability density function at a point.
        Should not be used by end user.

        Args:
            x (int): point for calculating the mean value.
        """
        if x < 0 or x > 1:
            value = 0
        else:
            g = 0
            for i in range(0, int(self.n * x + 1)):
                g += pow(-1, i) * math.comb(self.n, i) * pow(x - i / self.n, self.n - 1)
            value = (self.n**self.n / math.factorial(self.n - 1)) * g
        return value

    def calculate_pdf(self, x, round_to=2):
        """ Probability density function calculator for the Bates distribution.

        Args:
            x (float): point for caluclating the probability density function
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: probability density function
        """
        self.pdf = self._fx((x - self.a) / (self.b - self.a)
                            ) / (self.b - self.a)
        return round(self.pdf, round_to)

    def calculate_cdf(self, x, round_to=2):
        """  Probability density function calculator for the Bates distribution.
        Args:
            x (float): point for calculating the probability density function
            round_to (int): Round the mean value.
            [Default value: 2 floating point]

        Returns:
            float: probability density function output
        """
        value = 0
        for i in range(0, x + 1):
            value += self.calculate_pdf(i)
        self.cdf = value
        return round(value, round_to)

    def plot_bar_pdf(self, samples=10**6):
        """ Method to plot the pdf of the Bates distribution.

        Args:
            points (int): number of discrete data points

        Returns:
            F (np.array): list of PDFs for samples
        """
        x = np.linspace(self.a, self.b, num=samples)
        y = (x - self.a) / (self.b - self.a)

        F = np.zeros_like(y)

        for i in range(0, len(y) + 1 // 2):
            F[i] = self.calculate_pdf(y[i])
            F[-i - 1] = F[i]      # symmetric graph

        plt.plot(x, F, label=f'n={self.n}')
        plt.legend()
        plt.title(f"Probability Distribution Function for Bates n={self.n}")
        plt.show()
        return F

    def __repr__(self):
        """  Method to output the characteristics of the Bates instace.
        Args:
            None
        Returns:
            string: characteristics of the Bates
        """
        return "mean {0}, standard deviation {1}, n {2}".format(self.mean,
                                                                self.stdev, self.n)
