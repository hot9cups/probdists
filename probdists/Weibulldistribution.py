import math
import numpy as np
from matplotlib import pyplot as plt
from .Generaldistribution import Distribution


class Weibull(Distribution):
  def __init__(self, lmbda, k):
    self.lmbda = lmbda
    self.k = k

    Distribution.__init__(self.calculate_mean(), self.calculate_stdev())

  def calculate_mean(self):
    gamma_factor = math.gamma(1 + (1 / self.k))
    return self.lmbda * gamma_factor

  def calculate_stdev(self):
    return self.lmbda * (math.log(2)) ** (1 / self.k)

  def calculate_pdf(self, x):
    if x < 0:
      out = 0
    else:
      exp_factor = math.exp(-(x / self.lmbda) ** self.k)
      out = (self.k / self.lmbda) * exp_factor * \
            (x / self.lmbda) ** (self.k - 1)
    return out

  def calculate_cdf(self, x):
    if x < 0:
      out = 0
    else:
      out = 1 - math.exp(-(x / self.lmbda) ** self.k)
    return out

  def __repr__(self):
    return f"lambda: {self.lmbda}, k: {self.k}, mean: {self.mean}, \
            standard deviation: {self.stdev}"
