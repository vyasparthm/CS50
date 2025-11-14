import csv

with open('names.csv','r') as file:
    for line in file:
        # row = line.rstrip().split(',')
        # print(f'{row[0]} belongs to {row[1]} universe!')
        row,universe = line.rstrip().split(',')
        print(f'{row}  belongs to {universe}')
        
            