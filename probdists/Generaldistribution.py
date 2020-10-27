from pathlib import Path


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
        """Function to read in data from a txt file.
        The txt file should have one number (float) per line.
        The numbers are stored in the data attribute.

        Args:
                file_name (string): name of a file to read from

        Returns:
                None

        """

        if file_name == 'demo_gaussian_data':
            dirname = Path(__file__).parent.parent.absolute()
            file_name = Path(dirname, 'numbers.txt')

        elif file_name == 'demo_binomial_data':
            dirname = Path(__file__).parent.parent.absolute()
            file_name = Path(dirname, 'numbers_binomial.txt')

        elif file_name == 'demo_exponential_data':
            dirname = Path(__file__).parent.parent.absolute()
            file_name = Path(dirname, 'numbers_exponential.txt')

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
