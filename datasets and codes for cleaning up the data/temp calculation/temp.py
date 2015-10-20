import csv
import math
wanted = open("noDuplicateWeather.csv")
reader = csv.reader(wanted)

mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for row in reader:
    temp = row[6][:-2]
    if (temp == "mi"):
        print("fuck")
    elif (math.floor(float(temp)) < 10.5 and math.floor(float(temp)) >= 9.5):
        #print("pass")
        if (row[11] != "Rain"):
            mylist[int(row[0].split()[1])] = mylist[int(row[0].split()[1])] + 1
        
print(mylist)
