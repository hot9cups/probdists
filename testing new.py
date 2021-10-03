from probdists import Gaussian

gaussian = Gaussian()
gaussian.read_data_file("./probdists/numbers.txt")

print(gaussian.data)
gaussian.plot_histogram_pdf()
