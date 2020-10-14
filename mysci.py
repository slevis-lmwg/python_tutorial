# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:  # closes file automatically
    data = datafile.read()

