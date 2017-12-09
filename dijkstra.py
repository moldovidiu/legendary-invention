import csv

# Read from csv file to dictionary
def read_file(filename, dictname):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
           #First column is the key, the rest is the value
           dictname[row[0]] = row[1:]

edges = {}
read_file('SC0x.csv', edges)
