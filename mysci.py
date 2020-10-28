
# Init. my data variable
data = []  # empty list

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:  # closes file automatically

   # read the first 3 lines (header)
   for _ in range(3):
       datafile.readline()

   # read and parse the rest of the file
   for line in datafile:
       datum = line.split()  # () splits whitespace
       data.append(datum)

