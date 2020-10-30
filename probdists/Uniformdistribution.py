import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Uniform(Distribution):
    """ Uniform distribution class for calculating and
    visualizing a Uniform distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) extracted from the data file
        low (float) representing the smallest number in data_list
        high (float) representing the highest number in data_list
    """

    def __init__(self, low=0, high=10):
        self.low = low
        self.high = high
        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def replace_stats_with_data(self):
        """Function to calculate low and high from the data set

                # Args:
                    None

                Returns:
                    float: the low value
                    float: the high value
                """
        self.low = min(self.data)
        self.high = max(self.data)
        self.calculate_mean()
        self.calculate_stdev()
        return self.low, self.high

    def calculate_mean(self, round_to=2):
        """Function to calculate the mean of the data set.

        Args:
             round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
               float: mean of the data set
        """

        self.mean = (self.low + self.high) / 2

        return round(self.mean, round_to)

    def calculate_stdev(self, sample=True, round_to=2):
        """Function to calculate the standard deviation of the data set.

        Args:
             sample (bool): whether the data represents a sample or population
             round_to (int): Round the mean value. [Default value: 2 floating point]

        Returns:
            float: standard deviation of the data set
        """

        sqr_interval = (self.high - self.low) ** 2

        self.stdev = math.sqrt(sqr_interval / 12)

        return round(self.stdev, round_to)

    def calculate_cdf(self, x, round_to=2):
        """Cumulative distribution function calculator for the uniform distribution.

                Args:
                        x (float): point for calculating the
                                   cumulative distribution function

                Returns:
                        float: cumulative distribution function output
                """
        if x < self.low:
            self.cdf = 0
        elif self.low<=x<=self.high:
            self.cdf = (x - self.low)/(self.high-self.low)
        else:
            self.cdf = 1

        return round(self.cdf, round_to)

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using
                matplotlib pyplot library.

                Args:
                        None

                Returns:
                        None
                """
        plt.hist(self.data)
        plt.title("Histogram of Data")
        plt.xlabel("data")
        plt.ylabel("count")
        plt.show()

    def calculate_pdf(self, x, round_to=2):
        """Probability density function calculator for the uniform distribution.

                Args:
                        x (float): point for calculating the
                                   probability density function
                        round_to (int): Round the mean value. [Default value: 2 floating point]

                Returns:
                        float: probability density function output
        """
        self.pdf = 1/(self.high-self.low) if self.high >= x >= self.low else 0
        return round(self.pdf, round_to)

    def plot_bar_pdf(self):
        """Function to plot the pdf of the uniform distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(int(self.low)-5, int(self.high)+5):
            x.append(i)
            self.calculate_pdf(i)
            y.append(self.pdf)

        # make the plots
        plt.bar(x, y)
        plt.title('Probability Density for Uniform Distribution')
        plt.ylabel('Probability')
        plt.xlabel('x')

        plt.show()

        return x, y

    def __repr__(self):
        """Function to output the characteristics of the Uniform instance

                Args:
                        None

                Returns:
                        string: characteristics of the Uniform distribution

                """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
