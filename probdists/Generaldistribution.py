from pathlib import Path
from abc import abstractmethod
from typing import List, Tuple
import traceback
import pandas as pd


class Distribution:
    """ Generic distribution class for calculating and
        visualizing a probability distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) extracted from the data file
        pdf (float) representing the Probability density function
    """

    @abstractmethod
    def calculate_mean(self, round_to: int = 2) -> float:
        pass

    @abstractmethod
    def calculate_stdev(self, round_to: int = 2) -> float:
        pass

    @abstractmethod
    def cdf(self, x: float) -> float:
        pass

    @abstractmethod
    def plot_histogram(self) -> None:
        pass

    @abstractmethod
    def calculate_pdf(self, round_to: int) -> float:
        pass

    @abstractmethod
    def plot_histogram_pdf(self, n_spaces: int) -> Tuple[List[float], List[float]]:
        pass

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []
        self.pdf = None

    def read_data_file(self, file_path: str, separator="\\n", header=None):

        """Function to read in data from a txt file, csv file
        and excel formats (xls, xlsx, xlsm, xlsb, odf, ods and odt)

        The txt file should have one number (float) per line or
        numbers should be separator seperated.

        No need for separator argument with csv file, it will
        by default be ',' so csv files should have , seperated
        numbers

        For excel file formats. There should only be one column
        containing numbers, and if 0th row is header then header
        argument should be 0. The numbers are taken from next row
        mentioned in header parameter.
        Args:
            separator (character): custom separator to use if required
            header (int or by default None): to specify if header is there in
            excel file.
        Returns:
                None
        """

        # Finding the file extension and selecting separator for csv file
        extension = file_path.split(".")[-1]
        if extension == "csv":
            separator = ","

        excel_formats = {"xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"}

        if extension in excel_formats:
            df = pd.read_excel(file_path, header=header)
            for i in df.iterrows():
                try:
                    self.data.append(float(df.iat[i[0], 0]))
                except Exception as err:
                    print(f"Error: Could not convert {df.iat[i[0], 0]} to int.")
                    print(str(err))
            return

        with open(file_path, "r") as file:
            for line in file.readlines():
                line = line.strip().split(separator)
                for number in line:
                    try:
                        self.data.append(float(number))
                    except Exception as err:
                        print(f"Error: Could not convert {number} to int.")
                        print(str(err))
