import math
import pandas as pd


#data = pd.read_csv('Kumpula-June-2016-w-metadata.txt', sep=',', header=None)
data = pd.read_csv("data\Kumpula-June-2016-w-metadata (1).cvs",  sep=',',  skiprows=8)

temp_data = data[["TEMP","MIN","MAX"]].plot()



print(temp_data)

