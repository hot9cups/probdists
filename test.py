import unittest
import math
from probdists import Gaussian, Binomial, Exponential, Distribution, Gamma, Bernoulli, Uniform


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


def get_numbers_uniform_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers_uniform.txt").as_posix()


def get_numbers_bernoulli_file() -> str:
    return Path().absolute().joinpath("fixtures/numbers_bernoulli.txt").as_posix()


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
            round(self.gaussian.calculate_stdev(), 2),
            88.55,
            "population standard deviation incorrect",
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
            round(self.gaussian.calculate_pdf(25), 5),
            0.19947,
            "calculate_pdf function does not give expected result",
        )
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(
            round(self.gaussian.calculate_pdf(75), 4),
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
        self.assertEqual(stdev, 2.1908902300206643)

    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p, 3), 0.615)
        self.assertEqual(n, 13)

    def test_pdf(self):
        self.assertEqual(round(self.binomial.calculate_pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.calculate_pdf(3), 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.calculate_pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.calculate_pdf(3), 5), 0.00472)

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
            round(self.exponential.calculate_pdf(1), 5),
            0.19470,
            "calculate_pdf function does not give expexted result",
        )
        self.exponential.calculate_mean()
        self.exponential.calculate_stdev()
        self.assertEqual(
            round(self.exponential.calculate_pdf(5), 5),
            0.07163,
            "calculate_pdf function after calculating mean and \
                             stdev does not give expected result",
        )

    def test_cdf(self):
        self.assertEqual(
            self.exponential.calculate_cdf(-2.5),
            0,
            "calculate_cdf does not return expected result",
        )
        self.assertEqual(
            round(self.exponential.calculate_cdf(12.3), 5),
            0.95381,
            "calculate_cdf does not return expected result",
        )

        self.exponential.calculate_mean()
        self.exponential.calculate_stdev()

        self.assertEqual(
            self.exponential.calculate_cdf(-1.3),
            0,
            "calculate_cdf does not return expected result after calculating mean and stdev",
        )
        self.assertEqual(
            round(self.exponential.calculate_cdf(9.5), 3),
            0.907,
            "calculate_cdf does not return expected result after calculating mean and stdev",
        )


class TestUniformClass(unittest.TestCase):
    def setUp(self):
        self.uniform = Uniform(0, 10)
        self.uniform.read_data_file(get_numbers_uniform_file())

    def test_initialization(self):
        self.assertEqual(self.uniform.low, 0, "incorrect initialization of interval start")
        self.assertEqual(self.uniform.high, 10, "incorrect initialization of interval end")

    def test_invalid_interval_exception(self):
        self.assertRaises(Exception, Uniform, 5, 5)

    def test_readdata(self):
        self.assertEqual(
            self.uniform.data,
            [4, 5, 2, 3, 3, 2, 2, 5, 4, 3, 1, 3, 5, 3, 4],
            "data read incorrectly",
        )

    def test_replace_stats_with_data(self):
        l, h = self.uniform.replace_stats_with_data()
        self.assertEqual(l, 1)
        self.assertEqual(h, 5)

    def test_meancalculation(self):
        self.uniform.calculate_mean()
        self.assertEqual(self.uniform.mean, 5, "calculated mean not as expected")

    def test_stdevcalculation(self):
        self.assertEqual(
            round(self.uniform.calculate_stdev(), 2),
            2.89,
            "calculated standard deviation incorrect",
        )

    def test_pdf(self):
        self.assertEqual(
            round(self.uniform.calculate_pdf(5), 1),
            0.1,
            "calculate_pdf function does not give expected result",
        )
        self.assertEqual(
            round(self.uniform.calculate_pdf(15), 1),
            0,
            "calculate_pdf function does not give expected result",
        )
        self.uniform.replace_stats_with_data()
        self.assertEqual(
            self.uniform.calculate_pdf(5),
            0.25,
            "calculate_pdf function does not give expected result",
        )
        self.assertEqual(
            self.uniform.calculate_pdf(15),
            0,
            "calculate_pdf function does not give expected result",
        )

    def test_cdf(self):
        self.uniform.replace_stats_with_data()
        self.assertEqual(
            self.uniform.calculate_cdf(0), 0, "calculate_cdf function does not give expected result"
        )
        self.assertEqual(
            self.uniform.calculate_cdf(7), 1, "calculate_cdf function does not give expected result"
        )
        self.assertEqual(
            self.uniform.calculate_cdf(4),
            0.75,
            "calculate_cdf function does not give expected result",
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


class TestBernoulliClass(unittest.TestCase):
    def setUp(self):
        self.bernoulli = Bernoulli(0.3)
        self.bernoulli.read_data_file(get_numbers_bernoulli_file())

    def test_initialization(self):
        self.assertEqual(self.bernoulli.p, 0.3, "p value incorrect")

    def test_readdata(self):
        self.assertEqual(
            self.bernoulli.data, [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], "data not read in correctly"
        )

    def test_calculatemean(self):
        self.bernoulli.calculate_mean()
        self.assertEqual(self.bernoulli.mean, 0.3)

    def test_calculatestdev(self):
        stdev = self.bernoulli.calculate_stdev()
        self.assertEqual(stdev, 0.458257569495584)

    def test_replace_stats_with_data(self):
        p = self.bernoulli.replace_stats_with_data()
        self.assertEqual(round(p, 2), 0.17, "p value not correct after reading data")

    def test_pdf(self):
        self.assertEqual(round(self.bernoulli.calculate_pdf(0), 2), 0.7)
        self.assertEqual(round(self.bernoulli.calculate_pdf(1), 2), 0.3)

        self.bernoulli.replace_stats_with_data()
        self.assertEqual(round(self.bernoulli.calculate_pdf(0), 2), 0.83)
        self.assertEqual(round(self.bernoulli.calculate_pdf(1), 2), 0.17)

    def test_cdf(self):
        self.assertEqual(round(self.bernoulli.calculate_cdf(0.5), 1), 0.7)

        self.bernoulli.replace_stats_with_data()

        self.assertEqual(self.bernoulli.calculate_cdf(2), 1.0)

    def test_add(self):
        bernoulli_one = Bernoulli(0.2)
        bernoulli_two = Bernoulli(0.2)
        bernoulli_sum = bernoulli_one + bernoulli_two

        self.assertEqual(bernoulli_sum.p, 0.2)
        self.assertEqual(bernoulli_sum.n, 2)


if __name__ == "__main__":
    unittest.main()
