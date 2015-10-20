import csv
wanted = open("time_visibility_rain_highway.csv")
reader = csv.reader(wanted)


mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
          , 0, 0, 0, 0, 0, 0, 0, 0]
for row in reader:
    if (row[0] != "Hour"):
        temp = int(row[0])
        mylist[temp] = mylist[temp] + 1
print(mylist)
# [1354, 2028, 2690, 3502, 2882, 3182, 3434, 4064, 4158, 4009, 4698, 4523, 2318, 2024, 1639, 1366, 1228, 894, 835, 952, 447, 385, 442, 782]
