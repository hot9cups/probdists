from pathlib import Path
import pandas as pd
import traceback


class Distribution:
    """ Generic distribution class for calculating and
        visualizing a probability distribution.
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) extracted from the data file
        pdf (float) representing the Probability density function
        cdf (float) representing the Cumulative distribution function
    """

    def __init__(self, mu=0, sigma=1):

        self.mean = mu
        self.stdev = sigma
        self.data = []
        self.pdf = None
        self.cdf = None

    def read_data_file(self, file_name, separator='\\n', header=None):
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
        The numbers are stored in the data attribute.
        Args:
                file_name (string): name of a file to read from
                separator (character): custom separator to use if required
                header (int or by default None): to specify if excel file
                contains header.
        Returns:
                None
        """

        file_name_map = {
            'demo_gaussian_data': 'numbers.txt',
            'demo_binomial_data': 'numbers_binomial.txt',
            'demo_exponential_data': 'numbers_exponential.txt',
            'demo_gamma_data': 'numbers_gamma.txt',
            'demo_uniform_data': 'numbers_uniform.txt',
            'demo_bernoulli_data': 'numbers_bernoulli.txt',
            'demo_triangular_data': 'numbers_triangular.txt'
        }
        if file_name in file_name_map:
            dirname = Path(__file__).parent.parent.absolute()
            file_name = str(
                Path(dirname, 'probdists/' + file_name_map[file_name]))

        # Finding the file extension and selecting separator for csv file
        extension = file_name.split('.')[-1]
        if extension == 'csv':
            separator = ','

        excel_formats = {'xls', 'xlsx', 'xlsm', 'xlsb',
                         'odf', 'ods', 'odt'}

        if extension in excel_formats:
            df = pd.read_excel(file_name, header=header)
            data_list = []
            for i in df.iterrows():
                try:
                    data_list.append(float(df.iat[i[0], 0]))
                except:  # pylint: disable=W0702
                    traceback.print_exc()
                    print('Could not convert', df.iat[i[0], 0], ' to int.')
        else:
            with open(file_name) as file:
                data_list = []

                # Reading whole file content as string
                line = file.readline()

                while line:
                    # Stripping white spaces from start and end of string
                    line = line.strip()

                    # If text is space or newline seperated
                    if separator == '\\n' or separator == ' ':
                        # Splitting text with space seperaor
                        line = line.split()
                    else:
                        # Splitting text based on custom separator
                        line = line.split(separator)
                    for number in line:
                        try:
                            data_list.append(float(number))
                        except:  # pylint: disable=W0702
                            traceback.print_exc()
                            print('Could not convert', number, ' to int.')
                    line = file.readline()

        # No need to explicitly close file when using with statement.
        self.data = data_list
