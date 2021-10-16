import math
import numpy as np
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class Bates(Distribution):

    def __init__(self, n, a=0, b=1):

        self.n = n
        self.a = a
        self.b = b
        Distribution.__init__(self,
                              self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self, round_to=2):
        self.mean = 0.5 * (self.a + self.b)

        return round(self.mean, round_to)

    def calculate_stdev(self, round_to=2):
        var = (self.b - self.a) / (12 * self.n)

        self.stdev = math.sqrt(var)

        return round(self.stdev, round_to)

    def _fx(self, x):
        if x < 0 or x > 1:
            value = 0
        else:
            g = 0
            for i in range(0, int(self.n * x + 1)):
                g += pow(-1, i) * math.comb(self.n, i) * pow(x - i / self.n, self.n - 1)
            value = (self.n**self.n / math.factorial(self.n - 1)) * g
        return value

    def calculate_pdf(self, x, round_to=2):
        self.pdf = self._fx((x - self.a) / (self.b - self.a)
                            ) / (self.b - self.a)
        return round(self.pdf, round_to)

    def calculate_cdf(self, x, round_to=2):
        value = 0
        for i in range(0, x + 1):
            value += self.calculate_pdf(i)
        return round(value, round_to)

    def plot_bar_pdf(self, points=100):

        x = np.linspace(self.a, self.b, num=10**6)
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

        return "mean {0}, standard deviation {1}, n {2}".format(self.mean,
                                                                self.stdev, self.n)
