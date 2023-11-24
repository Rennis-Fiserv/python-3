import csv
import os

def find_total_visits():
    total = 0

    for x in range(1,4):
        file_name = f'week-{x}.csv'
        file_path = os.path.join('files/', file_name)
    
        with open(file_path) as file:
            next(file)
            rows = csv.reader(file, delimiter=',')
            for row in rows:
                total+= sum(map(int,row[1:]))
    
    return total



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()