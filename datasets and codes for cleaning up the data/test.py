import csv

wanted = open("Car Accidents - Car Accidents.csv")
reader = csv.reader(wanted)
count = 0
totalHours = 0
totalMinutes = 0
for row in reader:
    if(row[0] != "CAD CDW ID"): #getting rid of header
        if(row[9] != ""):
            count = count + 1
            clearanceTime = row[2].split()[1]
            clearanceTimeSet = clearanceTime.split(":") #hours and minutes for clearance
            occurenceTimeSet = row[9].split(":") #hours and minutes for occurence
            #print(clearanceTimeSet) 

            hourDifference = (int(clearanceTimeSet[0])-int(occurenceTimeSet[0]))
            minuteDifference = (int(clearanceTimeSet[1])-int(occurenceTimeSet[1]))
            if(minuteDifference < 0):
                minuteDifference = minuteDifference + 60
                hourDifference - 1
            if(hourDifference < 0):
                hourDifference = hourDifference + 24
            #print("hours = " + str(hourDifference) + ", minutes = " + str(minuteDifference))
            totalHours = totalHours + hourDifference
            totalMinutes = totalMinutes + minuteDifference

averageHours = totalHours/count
averageMinutes = totalMinutes/count
print(averageHours)
print(averageMinutes)
    
