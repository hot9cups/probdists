import numpy as np
from mpmath import *
import math
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class StudentT(Distribution):

    def __init__(self, v=1):

        self.v = v

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        if self.v > 1:
            self.mean = 0
        else:
            self.mean = None

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        if self.v > 2:
            self.stdev = self.v / (self.v - 2)
        elif self.v > 1 and self.v <= 2:
            self.stdev = float("inf")
        else:
            self.stdev = None       # undefined

        return round(self.stdev, round_to)

    def calculate_pdf(self, x, round_to=2):
        denom = math.sqrt(self.v * math.pi) * math.gamma(self.v / 2)
        num = math.gamma(self.v + 1 / 2) * pow((1 + (x ** 2 / self.v)), -1 * (self.v + 1 / 2))
        pdf = num / denom
        return round(pdf, round_to)

    def calculate_cdf(self, x, round_to=2):
        """
        NOTE: This function is valid only for x**2 < v
        For other values of x, it returns None
        This shall be fixed in the future
        """
        if x**2 < self.v:
            numerator = x * math.gamma(self.v + 1 / 2)
            denominator = math.sqrt(math.pi * self.v) * math.gamma(self.v / 2)
            two_f_one = hyp2f1(0.5, 0.5 * (self.v + 1), 1.5, -x**2 / self.v)
            out = 0.5 + (numerator * two_f_one) / denominator
            return out
        else:
            return None

    def plot_pdf(self, a=-4, b=4, samples=10**3):
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
        x = np.linspace(a, b, nunm=samples)
        y = np.zeroes_like(x)

        for i in range(0, len(x)):
            y[i] = self.calculate_cdf(x[i])

        plt.plot(x, y, label=f"v={self.v}")
        plt.legend()
        plt.title(f"Cumulative Distribution Function for Student's t-distribution v={self.v}")
        plt.show()
        return y

    def __repr__(self):

        return 'mean {0}, standard deviation {1}, \
               degree of freedom {2}'.format(self.mean, self.stdev, self.v)
