
# Init. my data variable
data = {'date':[], 'time':[], 'tempout':[]}  # dictionary w lists

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:  # closes file automatically

   # read the first 3 lines (header)
   for _ in range(3):
       datafile.readline()

   # read and parse the rest of the file
   for line in datafile:
       split_line = line.split()  # () splits whitespace
       data['date'].append(split_line[0])
       data['time'].append(split_line[1])
       data['tempout'].append(float(split_line[2]))

