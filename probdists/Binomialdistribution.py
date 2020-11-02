import math
from typing import List, Tuple

import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials
    """

    def __init__(self, prob=0.5, size=20):

        self.n = size
        self.p = prob

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """Function to calculate the mean from p and n

        Args:
            round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: mean of the data set
        """

        self.mean = self.p * self.n

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """Function to calculate the standard deviation from p and n.

        Args:
            round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: standard deviation of the data set
        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return round(self.stdev, round_to)

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value
        """

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.calculate_mean()
        self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x=["0", "1"], height=[(1 - self.p) * self.n, self.p * self.n])
        plt.title("Bar Chart of Data")
        plt.xlabel("outcome")
        plt.ylabel("count")

    def calculate_pdf(self, k, round_to=2):
        """Probability density function calculator for the gaussian distribution.

        Args:
            k (float): point for calculating the probability density function
            round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: probability density function output
        """

        a = math.factorial(self.n)
        b = math.factorial(k) * math.factorial(self.n - k)
        c = (self.p ** k) * (1 - self.p) ** (self.n - k)
        self.pdf = (a / b) * c

        return round(self.pdf, round_to)

    def cdf(self, x: float) -> float:
        """Cumulative distribution function calculator for the binomial distribution.

        Args:
            x (float): point for calculating the cumulative distribution function

        Returns:
            float: cumulative distribution function output
        """

        total_p = 0
        for i in range(x + 1):
            self.calculate_pdf(i)
            total_p += self.pdf
        return total_p

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            self.calculate_pdf(i)
            y.append(self.pdf)

        # make the plots
        plt.bar(x, y)
        plt.title("Distribution of Outcomes")
        plt.ylabel("Probability")
        plt.xlabel("Outcome")

        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution
        """

        try:
            assert self.p == other.p, "p values are not equal"
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def plot_histogram(self):
        pass

    def plot_histogram_pdf(self, n_spaces: int) -> Tuple[List[float], List[float]]:
        pass

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial
        """

        return f"mean {self.mean}, standard deviation {self.stdev}, \
            p {self.p}, n {self.n}"
