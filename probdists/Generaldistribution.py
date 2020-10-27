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
        """
            Initialize the generic distribution object.

            Recommended that you instantiate one of its children.
            mu (float): the mean of the distribution
            sigma (float): the standard deviation of the distribution
            data (list of float): the data itself
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name, sep='\n'):
        """Function to read in data from a txt file.
        The numbers are stored in the data attribute.

        Args:
                file_name (string): name of a file to read from
                sep (string): seperator specifying how to split
                              the text read from file_name.
                Default to newline character ('\n')
        NOTE:   Refrain from using '.' as a seperator
                (Especially if you work with floating-points).
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

        with open(file_name) as file:
            # read the data as a single string
            txt = file.read()
            # split into a list seperated by sep
            tokens = txt.split(sep)
            # sanitize the input of empty literals
            tokens = [x for x in tokens if x != '']
            data_list = []
            # add to data_list
            try:
                data_list = [float(x) for x in tokens]
            except ValueError:
                print('[-] Encountered bad token to convert to int')

        self.data = data_list
