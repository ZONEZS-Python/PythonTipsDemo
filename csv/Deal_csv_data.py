import csv

file = open('name.csv', 'r')
reader = csv.reader(file)

# print(reader)

for row in reader:
    print(row)