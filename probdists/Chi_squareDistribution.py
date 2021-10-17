import pandas as pd
# from .Generaldistribution import Distribution


class Chi_squareDistribution():
    """Chi_squareDistribution Chi-square distribution class
    is for caluclating chi-square value.
    """

    def __init__(self, filename=None, data=None):
        self.filename = filename
        self.data = data

    def read_data_file(self, filename):
        """Read data file will read data from csv file.
        in which there will be observed and expected values.

        """
        self.filename = filename
        self.data = pd.read_csv(filename)

    def chi_square(self):
        """   Chi_square  method will extract the observed and expected values columns from the data file(.csv) and return
        the vlaue of chi-square.
        """

        observed = self.data["observed"].values.tolist()
        expected = self.data["expected"].values.tolist()

        chi = 0
        for i, el in enumerate(observed):
            chi = chi+(((el-expected[i])**2)/expected[i])
        print(chi)
        return chi
