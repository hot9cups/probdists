import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
from collections import Counter


class Triangular(Distribution):
    """
    Triangular distribution class for calculating and visualizing the
    triangular distribution: a continuous probability distribution shaped
    like a triangle
    Note: a <= mode <= b

    Attributes:

        a (float): the minimum lower limit value
        b (float): the maximum upper limit value
        mode (float): the mode, where min <= mode <= max

        mean (float): the mean value of the distribution
        stdev (float): the standard deviation of the distribution

    """

    def __init__(self, a=0, b=1, mode=0.5):
        if mode < a or b < mode:
            raise ValueError

        self.a = a
        self.b = b
        self.mode = mode

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """
        Method to calculate the mean from the min, max and mode

        Args:
            round_to (int): Round the mean value. Defaults to 2.

        Returns:
            float: mean of the data set
        """

        self.mean = 1/3 * (self.a + self.b + self.mode)

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        """
        Method to calculate the standard deviation from the min, max and mode

        Args:
            round_to (int): Round the mean value. Defaults to 2.

        Returns:
            float: standard deviation of the data set
        """

        summation = (self.a ** 2) + (self.b ** 2) + (self.mode ** 2) - \
                    (self.a * self.b) - (self.a * self.mode) - \
                    (self.b * self.mode)
        variance = summation / 18
        self.stdev = math.sqrt(variance)

        return round(self.stdev, round_to)

    def replace_stats_with_data(self):
        """ Method to calculate a, b, mode from the data set

        Args:
            None

        Returns:
            float: a, the minimum value
            float: b, the maximum value
            float: mode, the mode of the dataset
        """
        if not self.data:
            # Use default values
            self.a, self.b, self.mode = 0, 1, 0.5
        else:
            self.a = min(self.data)
            self.b = max(self.data)
            self.calculate_mode()

        return self.a, self.b, self.mode

    def calculate_mode(self, round_to=2):
        """
        Calculates the mode of a dataset
        If no single mode, it will approximate the mode using the mean

        Args:
            round_to (int): Round the mode value. [Default value: 2]

        Returns:
            float: mode of data
        """
        data = Counter(self.data)
        dict_data = dict(data)

        # Create list of modes from data
        mode = [k for k, v in dict_data.items() if v == max(list(data.values()))]

        if len(mode) == 1:
            self.mode = mode[0]
        else:
            # Multiple modes
            # Approximates mode using mean
            self.mode = sum(self.data) / len(self.data)
        return round(self.mode, round_to)

    def calculate_pdf(self, x, round_to=2):
        """
        Probability density function calculator for the Triangular distribution.

        Args:
            x (float): point for calculating the probability density function
            round_to (int): Round the pdf value. [Default value: 2]

        Returns:
            float: probability density function
        """
        value = 0  # default value for when x < min or x > max
        if self.a <= x <= self.mode:
            value = (2 * (x - self.a)) / (
                    (self.b - self.a) * (self.mode - self.a))
        elif self.mode < x <= self.b:
            value = (2 * (self.b - x)) / (
                    (self.b - self.a) * (self.b - self.mode))

        self.pdf = value
        return round(self.pdf, round_to)

    def calculate_cdf(self, x, round_to=2):
        """
        Cumulative density function calculator for the Triangular distribution.

        Args:
            x (float): point for calculating the cumulative density function
            round_to (int): Round the value. [Default value: 2]

        Returns:
            float: cumulative density function output
        """
        if x < self.a:
            value = 0
        elif self.a <= x <= self.mode:
            num = ((x - self.a) ** 2)
            den = (self.b - self.a) * (self.mode - self.a)
            value = num / den
        elif self.mode < x <= self.b:
            num = ((self.b - x) ** 2)
            den = (self.b - self.a) * (self.b - self.mode)
            value = 1 - (num / den)
        else:
            value = 1

        self.cdf = value
        return round(self.cdf, round_to)

    def plot_bar_pdf(self):
        """
        Method to plot the pdf of the triangular distribution.

        Args:
            self
        Returns:
            None
        """
        x = [self.a, self.mode, self.b]

        peak = 2 / (self.b - self.a)
        y = [0, peak, 0]

        plt.plot(x, y)
        plt.title('Probability Density Plot for Triangular Distribution')
        plt.xlabel('Probability')
        plt.ylabel('x')

        plt.show()

        return x, y

    def __repr__(self):
        """
        Outputs the characteristics of the Triangular Distribution instance.

        Args:
            self
        Returns:
            string: characteristics of the Triangle
        """

        return f"minimum: {self.a}, maximum: {self.b}, mode: {self.mode}, " \
               f"mean: {self.mean}, standard deviation: {self.stdev}"
