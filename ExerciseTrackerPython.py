#This is going to be an excersize tracker written in Python

print("This is Tom's exercise tracker")
print("Hoping to add a little more every day and at the end of the week get a total distance walked")


#miles_walked = input("How many miles did you walk today? ")
#with open(r"c:\temp\mileTracker.txt", 'a') as file:
#    file.write(miles_walked + '\n')

import csv
from datetime import date

miles_walked = input("How many miles did you walk today bub? ")
today = date.today().strftime('%Y/%m/%d')
with open(r'c:\temp\mileTracker.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(['Date', 'Miles Walked'])
    writer.writerow([today, miles_walked])

#import csv

with open(r'c:\temp\mileTracker.csv', 'r') as file:
    reader = csv.DictReader(file)
    total_miles = 0
    for row in reader:
        total_miles += float(row['Miles Walked'])
    print(f'Total miles walked: **{total_miles:.2f}**')

