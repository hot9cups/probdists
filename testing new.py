from probdists import Exponential

exponential = Exponential()
exponential.read_data_file("./probdists/numbers.csv")

print(exponential.data)
exponential.plot_bar_pdf()
