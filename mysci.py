
# Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2}

# Data types for each column (only if non-string)
types = {'tempout': float}

# Init. my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:  # closes file automatically

    # read the first 3 lines (header)
    for _ in range(3):
        datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()  # () splits whitespace
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

