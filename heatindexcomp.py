
from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heatindex

# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column (only if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Init. my data variable
data = {}
for column in columns:
    data[column] = []

# Read data from file
data = read_data(columns, types=types)

# Compute the heat index
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

# Output comparison of data
print_comparison('heatindex', data['date'], data['time'], data['heatindex'], heatindex)

