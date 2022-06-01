from pandas import read_csv
from matplotlib import pyplot
import matplotlib.pyplot as plt
from google.colab import files
import io


data = files.upload()

series = read_csv(r"/content/teslavar.csv", header=0,
index_col=0, squeeze=True)

plt.figure (figsize=(12,7))
plt.title('Tesla Motors')
plt.ylabel('Variações em %', fontsize=16)
series.plot()
pyplot.show()