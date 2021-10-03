from probdists import Binomial

binomial = Binomial()
binomial.read_data_file("./probdists/numbers.csv")

print(binomial.data)
binomial.plot_bar_pdf()
