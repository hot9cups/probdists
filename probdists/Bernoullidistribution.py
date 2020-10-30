import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
from .Binomialdistribution import Binomial

class Bernoulli(Distribution):
    """ Bernoulli distribution class for calculating and
    visualizing a Bernoulli distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) to be extracted from the data file
        p (float) representing the probability of an event occurring (1).
    """

    def __init__(self, prob=0.5):

        self.p = prob

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """ Method to calculate the mean of a Bernoulli distribution

        Args:
            round_to (int): Round the mean value. Defaults to 2.

        Returns:
            float: mean of the data set
        """

        self.mean = self.p

        return round(self.mean, round_to)


    def calculate_stdev(self, round_to=2):
        """Function to calculate the standard deviation from p.

        Args:
            round_to (int): Round the mean value. Defaults to 2.

        Returns:
            float: standard deviation of the data set
        """
        # variance = p * q or p * ( 1 - p )
        self.stdev = math.sqrt(self.p * (1 - self.p))

        return round(self.stdev, round_to)

    def replace_stats_with_data(self):
        """ Method to calculate p from the data set

        Args:
            None

        Returns:
            float: the p value
        """

        self.p = 1.0 * sum(self.data) / len(self.data)
        self.calculate_mean()
        self.calculate_stdev()

        return self.p

    def plot_bar(self):
        """ Method to plot a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x=['0', '1'], height=[(1 - self.p), self.p])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
        """ Method to calculate pdf for the bernoulli distribution.

        Args:
            k (float): point for calculating the probability density function. Range of k: {0,1}

        Returns:
            float: probability density function output
        """
        try:
            if k != 0 or k != 1:
                raise ValueError
        except ValueError:
            print("Expected k for Bernoulli Distribution: 0, 1")

        return (self.p ** k) * ( 1 - self.p) ** (1 - k)

    def cdf(self, k):
        """ Method to calculate cdf for the bernoulli distribution.

        Args:
            k (float): point for calculating the cumulative distribution function
        Returns:
            float: cumulative distribution function output
        """

        val = 0                 # default value of cdf for k < 0
        if k >= 0 and k < 1:
            val = 1 - self.p
        elif k > 1:
            val = 1
        return val

    def plot_bar_pdf(self):
        """ Method to plot the pdf of the bernoulli distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        x = [0,1]
        y = [self.pdf(i) for i in x]

        # draw the plots
        plt.bar(x, y)
        plt.title("Distribution of Outcomes")
        plt.ylabel("Probability")
        plt.xlabel("Outcome")

        plt.show()

        return x, y

    def __add__(self, other):
        """ Method to add together two Bernoulli distributions with equal p

        Args:
            other (Bernoulli): Bernoulli instance

        Returns:
            Binomial: Resultant Binomial instance
        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError:
            raise

        result = Binomial()
        result.n = 2
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """ Method to output the characteristics of this Bernoulli instance
        Args:
            None

        Returns:
            string: characteristics of this Bernoulli instance
        """

        return 'mean {0}, standard deviation {1}, \
                p {2}, q {3}'.format(self.mean, self.stdev, self.p, 1.0 - self.p)
