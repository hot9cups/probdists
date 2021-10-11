import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Poisson(Distribution):
    """
    """

    def __init__(self, lmbda):

        self.lmbda = lmbda

        Distribution.__init__(self, self.calculate_mean()
                            self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        """
        """
        self.mean = math.sqrt(self.lmbda)

        return round(self.mean, round_to)
    
    def calculate_stdev(self, round_to=2):
        """
        """
        self.stdev = math.sqrt(self.lmbda)

        return round(self.stdev, round_to)
    
    def calculate_pdf(self, x, round_to=2):
        """
        """

        fact = math.factorial(x)
        self.pdf = ( math.exp(-self.lmbda) * self.lmbda ** x) / fact
        return round(self.pdf, round_to)
    
    def calculate_cdf(self, x, round_to=2):
        """
        """
        value = 0
        for i in range(x):
            value += _calc_discrete_pdf(i)
        return round(value, round_to)
    
    def _calc_discrete_pdf(x):
        """
        """
        fact = math.factorial(x)
        pdf = ( math.exp(-self.lmbda) * self.lmbda ** x) / fact
        return round(pdf, round_to)
    
    def plot_bar_pdf(self, points=100):
        """
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
        """
        """

        return "mean {0}, standard deviation {1}, lambda {2}".format(self.mean, self.stdev, self.lmbda)

