import math
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

    def __init__(self, k=2, theta=2, fit=False, data_file='demo_gamma_data'):
        """
        Init function to instantiate Gamma distribution
            Args:
                k (float) shape parameter representing shape of distribution (k > 0)
                theta (float) scale parameter that stretches/shrinks distribution (theta > 0)
        """
        if k <= 0 or theta <= 0:
            raise ValueError
        if not fit:
            self.fit = False
            self.k = k
            self.theta = theta
            Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        else:
            self.fit = True
            self.data_file = data_file
            self.read_data_file(data_file)
            total = sum(self.data)
            sample_mean = total / float(len(self.data))
            running = 0
            for each in self.data:
                running += math.pow((each-sample_mean), 2)
            sample_var = running / float(len(self.data))
            self.k = round(math.pow(sample_mean, 2) / sample_var)
            self.theta = sample_var / sample_mean
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
        self.pdf = (1 / (math.factorial(self.k - 1) * math.pow(self.theta, self.k))) * (math.pow(x, self.k - 1)) * (
            math.exp((-1 * x / self.theta)))
        return round(self.pdf, round_to)

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
        plt.title('Probability Density Plot for Gamma Distribution')
        plt.ylabel('Probability')
        plt.xlabel('x')

        plt.show()
        return x, y

    def calculate_cdf(self, x, is_upper=True, round_to=2):
        """
        Cumulative density function calculator for the Gamma distribution.
            Args:
                x (float): Point for calculating the cumulative distribution function
                is_upper (boolean): Upper or lower CDF results. [Default value: True]
                round_to (int): Round the CDF results. [Default value: 2]
            Returns:
                float: CDF output based on 'is_upper' argument rounded to 'round_to'
        """
        #initialize and declare the return variable self.cdf
        self.cdf = 0
        if x >= 0:
            #initiate cdfvalue variable
            cdfvalue = 0
            for i in range (self.k):
                cdfvalue += (math.pow((x / self.theta), i) * math.exp(-1 * x / self.theta)) / math.factorial(i)
            if is_upper == True:
                self.cdf = cdfvalue
            elif is_upper == False:
                self.cdf = 1 - cdfvalue
        else:
            raise Exception ('x has to be a positive real number')
        return round(self.cdf, round_to)

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
