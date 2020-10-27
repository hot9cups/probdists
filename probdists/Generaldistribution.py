from pathlib import Path
import pandas as pd

class Distribution:
    """ Generic distribution class for calculating and
        visualizing a probability distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) extracted from the data file
    """

    def __init__(self, mu=0, sigma=1):

        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """Function to read in data from a txt file, csv file
        and excel formats (xls, xlsx, xlsm, xlsb, odf, ods and odt)

        The txt file should have one number (float) per line or
        numbers should be seperator seperated.

        No need for seperator argument with csv file, it will
        by default be ',' so csv files shoul have , seperated
        numbers

        For excel file formats. There should only be one column
        containing numbers, and if 0th row is header then header
        argument should be 0. The numbers are taken from next row
        mentioned in header parameter.

        The numbers are stored in the data attribute.

        Args:
                file_name (string): name of a file to read from
                seperator (character): custom seperator to use if required
                header (int or by default None): to specify if header is there in
                excel file.
        Returns:
                None
        """
        if file_name == 'demo_gaussian_data':
            dirname = Path(__file__).parent.absolute()
            file_name = Path(dirname, 'numbers.txt')

        elif file_name == 'demo_binomial_data':
            dirname = Path(__file__).parent.absolute()
            file_name = Path(dirname, 'numbers_binomial.txt')

        elif file_name == 'demo_exponential_data':
            dirname = Path(__file__).parent.absolute()
            file_name = Path(dirname, 'numbers_exponential.txt')

        # Finding the file extension and selecting seperator for csv file
        extension = file_name.split('.')[-1]
        if extension == 'csv':
            seperator = ','

        excel_formats = {'xls', 'xlsx', 'xlsm', 'xlsb',
                         'odf', 'ods', 'odt'}

        if extension in excel_formats:
            df = pd.read_excel(file_name, header=header)
            data_list = []
            for i, row in df.iterrows():
                try:
                    data_list.append(int(float(df.iat[i, 0])))
                except:
                    print('Could not convert', df.iat[i, 0], ' to int.')
        else:
            with open(file_name) as file:
                data_list = []

                # Reading whole file content as string
                line = file.readline()

                while line:
                    # Stripping white spaces from start and end of string
                    line = line.strip()

                    # If text is space or newline seperated
                    if seperator == '\\n' or seperator == ' ':
                        # Splitting text with space seperaor
                        line = line.split()
                    else:
                        # Splitting text based on custom seperator
                        line = line.split(seperator)
                    for number in line:
                        try:
                            data_list.append(int(float(number)))
                        except:
                            print('Could not convert', number, ' to int.')
                    line = file.readline()

        # No need to explicitly close file when using with statement.
        self.data = data_list
