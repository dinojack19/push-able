import math
import pandas as pd

row_count = None
column_names = None
column_datatypes = None

temp_mean = None
temp_max_std = None
station_count = None


data = pd.read_csv("data/6153237444115dat.csv", sep=',')

#row_count = data.shape[0]
#column_names = data[-1:0]

#row = data[0:1]
#column_datatypes = row.dtypes 
#print(f"There are {row_count} rows")
#print(f"The columns are: \n{column_names}")
#print(f"The column types are: \n{column_datatypes}")

temp_mean = data["TEMP"].loc[data["TEMP"] != "****"]
temp_mean = temp_mean.astype(int)
temp_mean = temp_mean.mean()

def farenheit(temp_mean):
    temp_mean = (temp_mean *1.8) +32
    print(f"The mean temperature in Fahrenheit is {round(temp_mean,1)}")
    
farenheit(temp_mean)

temp_max_std = data["MAX"].loc[data["MAX"] != "***"]
temp_max_std = temp_max_std.astype(int)
temp_max_std = temp_max_std.std()
print(f"The standard deviation of maximum temperature is {round(temp_max_std, 1)}")

station_count = list(data["USAF"].unique())
print(f"The number of unique stations is {station_count}")

