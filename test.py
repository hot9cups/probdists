import unittest
import math
from probdists import Gaussian
from probdists import Binomial
from probdists import Exponential
from probdists import Distribution
from probdists import Gamma
from pathlib import Path


def get_gaussian_data_file() -> str:
    return Path().absolute().joinpath("fixtures/demo_gaussian_data.txt").as_posix()


def get_binomial_data_file() -> str:
    return Path().absolute().joinpath("fixtures/demo_binomial_data.txt").as_posix()


def get_exponential_data_file() -> str:
    return Path().absolute().joinpath("fixtures/demo_exponential_data.txt").as_posix()


def get_gamma_data_file() -> str:
    return Path().absolute().joinpath("fixtures/demo_gamma_data.txt").as_posix()


def get_numbers_spaced_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers_space.txt").as_posix()


def get_numbers_excel_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers.xls").as_posix()


def get_numbers_csv_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers.csv").as_posix()


def get_numbers_semicolon_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers_semicolon.txt").as_posix()


class TestGeneraldistribution(unittest.TestCase):
    def setUp(self):
        self.distribution = Distribution()

    def test_txt(self):
        self.distribution.read_data_file(get_numbers_spaced_file(), separator=" ")
        self.assertEqual(self.distribution.data, [1, 2, 3.4, 5.6, 7], "Txt file not read properly")

    def test_txt_sep(self):
        self.distribution.read_data_file(get_numbers_semicolon_file(), ";")
        self.assertEqual(
            self.distribution.data,
            [1, 2, 2.34, 5.67],
            "Txt file wit custom separator not read properly",
        )

    def test_csv(self):
        self.distribution.read_data_file(get_numbers_csv_file())
        self.assertEqual(
            self.distribution.data,
            [1434.0, 1453.0, 1412.0, 1489.0, 1507.0],
            "CSV file not read properly",
        )

    def test_excel(self):
        self.distribution.read_data_file(get_numbers_excel_file())
        self.assertEqual(
            self.distribution.data, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Xls file not read properly"
        )


class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian.read_data_file(get_gaussian_data_file())

    def test_initialization(self):
        self.assertEqual(self.gaussian.mean, 25, "incorrect mean")
        self.assertEqual(self.gaussian.stdev, 2, "incorrect standard deviation")

    def test_readdata(self):
        self.assertEqual(
            self.gaussian.data,
            [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31],
            "data not read in correctly",
        )

    def test_meancalculation(self):
        self.gaussian.calculate_mean()
        self.assertEqual(
            self.gaussian.mean,
            sum(self.gaussian.data) / float(len(self.gaussian.data)),
            "calculated mean not as expected",
        )

    def test_stdevcalculation(self):
        self.assertEqual(
            self.gaussian.calculate_stdev(), 88.55, "population standard deviation incorrect"
        )

    def test_cdf(self):
        self.assertEqual(
            round(self.gaussian.calculate_cdf(25), 3),
            0.500,
            "cdf function does not give expected result",
        )
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(
            round(self.gaussian.calculate_cdf(75), 3),
            0.486,
            "cdf function after calculating mean and \
                             stdev does not give expected result",
        )

    def test_pdf(self):
        self.assertEqual(
            self.gaussian.calculate_pdf(25, 5),
            0.19947,
            "calculate_pdf function does not give expected result",
        )
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(
            self.gaussian.calculate_pdf(75, 5),
            0.0045,
            "calculate_pdf function after calculating mean and \
                             stdev does not give expected result",
        )

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two

        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)


class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_data_file(get_binomial_data_file())

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, "p value incorrect")
        self.assertEqual(self.binomial.n, 20, "n value incorrect")

    def test_readdata(self):
        self.assertEqual(
            self.binomial.data,
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            "data not read in correctly",
        )

    def test_calculatemean(self):
        self.binomial.calculate_mean()
        self.assertEqual(self.binomial.mean, 8)

    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(stdev, 2.19)

    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p, 3), 0.615)
        self.assertEqual(n, 13)

    def test_pdf(self):
        self.assertEqual(self.binomial.calculate_pdf(5, 5), 0.07465)
        self.assertEqual(self.binomial.calculate_pdf(3, 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(self.binomial.calculate_pdf(5, 5), 0.05439)
        self.assertEqual(self.binomial.calculate_pdf(3, 5), 0.00472)

    def test_cdf(self):
        self.assertEqual(round(self.binomial.calculate_cdf(5), 5), 0.12560)
        self.assertEqual(round(self.binomial.calculate_cdf(3), 5), 0.01596)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.calculate_cdf(5), 5), 0.07889)
        self.assertEqual(round(self.binomial.calculate_cdf(3), 5), 0.00561)

    def test_add(self):
        binomial_one = Binomial(0.4, 20)
        binomial_two = Binomial(0.4, 60)
        binomial_sum = binomial_one + binomial_two

        self.assertEqual(binomial_sum.p, 0.4)
        self.assertEqual(binomial_sum.n, 80)


class TestExponentialClass(unittest.TestCase):
    def setUp(self):
        self.exponential = Exponential(0.25)
        self.exponential.read_data_file(get_exponential_data_file())

    def test_initialization(self):
        self.assertEqual(self.exponential.mean, 4.0, "incorrect mean")
        self.assertEqual(self.exponential.stdev, 4.0, "incoorect standard deviation")

    def test_readdata(self):
        self.assertEqual(
            self.exponential.data,
            [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31],
            "data read incorrectly",
        )

    def test_meancalculation(self):
        self.exponential.calculate_mean()
        self.assertEqual(self.exponential.mean, (1.0 / 0.25), "calculated mean not as expected")

    def test_stdevcalculation(self):
        self.exponential.calculate_stdev()
        self.assertEqual(
            self.exponential.stdev, (1.0 / 0.25), "calculated standard deviation incorrect"
        )

    def test_pdf(self):
        self.assertEqual(
            self.exponential.calculate_pdf(1, 5),
            0.19470,
            "calculate_pdf function does not give expexted result",
        )
        self.exponential.calculate_mean()
        self.exponential.calculate_stdev()
        self.assertEqual(
            self.exponential.calculate_pdf(5, 5),
            0.07163,
            "calculate_pdf function after calculating mean and \
                             stdev does not give expected result",
        )


class TestGammaClass(unittest.TestCase):
    def setUp(self):
        self.gamma = Gamma()
        self.gamma.read_data_file(get_gamma_data_file())
        self.gamma_wdata = Gamma()
        self.gamma_wdata.read_data_file(get_gamma_data_file())

    def test_initialization(self):
        self.assertEqual(self.gamma.k, 2, "incorrect k")
        self.assertEqual(self.gamma.theta, 2, "incorrect theta")

    def test_readdata(self):
        self.assertEqual(
            self.gamma_wdata.data, [1, 2, 2, 3, 3, 4, 5, 6, 8, 9, 13], "data not read in correctly"
        )

    def test_meancalculation(self):
        self.assertEqual(self.gamma.calculate_mean(), 4, "calculated mean not as expected")

    def test_stdevcalculation(self):
        self.gamma.calculate_stdev()
        self.assertEqual(self.gamma.stdev, math.sqrt(8), "standard deviation incorrect")

    def test_pdf(self):
        self.gamma.calculate_pdf(4)
        self.assertEqual(
            self.gamma.pdf,
            (1 / (math.exp(2))),
            "calculate_pdf function does not give expected result",
        )

    def test_add(self):
        gamma_one = Gamma(2, 2)
        gamma_two = Gamma(2, 2)
        gamma_sum = gamma_one + gamma_two

        self.assertEqual(gamma_sum.calculate_mean(), 8)
        self.assertEqual(gamma_sum.calculate_stdev(), 4)


if __name__ == "__main__":
    unittest.main()
