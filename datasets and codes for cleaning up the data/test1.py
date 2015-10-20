import csv

read = open("Car Accidents - Car Accidents.csv")
reader = csv.reader(read)
with open("New Car Accidents.csv", "w", newline = "") as csvfile:
    #9.419354838709678
    #24.258064516129032
    hourSubtract = 9
    minuteSubtract = 49
    writer = csv.writer(csvfile)
    for row in reader:
        if(row[0] != "CAD CDW ID"):
            date = row[2].split()[0].split("/")
            clearanceTime = row[2].split()[1]
            clearanceTimeSet = clearanceTime.split(":") #hours and minutes for clearance

            finalMinute = int(clearanceTimeSet[1])- minuteSubtract
            #print(finalMinute)
            temp = int(clearanceTimeSet[0])
            if(finalMinute < 0):
                finalMinute = finalMinute + 60
                temp = temp - 1
            if(finalMinute < 10):
                finalMinute = "0" + str(finalMinute)
            finalHour = int(clearanceTimeSet[0]) - hourSubtract
            #print(finalHour)

            if(finalHour < 0):
                finalHour = finalHour + 24

                
                date[1] = int(date[1]) - 1
            if(int(date[1]) == 0):
                if(int(date[0]) == 1):
                   date[1] = 31
                   date[0] = 12
                   date[2] = int(date[2])-1
                elif(int(date[0]) == 2):
                    date[1] = 31
                    date[0] = 1
                elif(int(date[0]) == 3):
                    date[1] = 28
                    date[0] = 2
                elif(int(date[0]) == 4):
                    date[1] = 31
                    date[0] = 3
                elif(int(date[0]) == 5):
                    date[1] = 30
                    date[0] = 4
                elif(int(date[0]) == 6):
                    date[1] = 31
                    date[0] = 5
                elif(int(date[0]) == 7):
                    date[1] = 30
                    date[0] = 6
                elif(int(date[0]) == 8):
                    date[1] = 31
                    date[0] = 7
                elif(int(date[0]) == 9):
                    date[1] = 31
                    date[0] = 8
                elif(int(date[0]) == 10):
                    date[1] = 30
                    date[0] = 9
                elif(int(date[0]) == 11):
                    date[1] = 31
                    date[0] = 10
                elif(int(date[0]) == 12):
                    date[1] = 30
                    date[0] = 11
            correctTime = str(date[0]) + "/" + str(date[1]) + "/" + str(date[2]) + " " + str(finalHour) + ":" + str(finalMinute)
            row[2] = correctTime
            print(row)
            writer.writerow(row)
            #subtract the time from the hours and minutes and then check if statement
            
        else:
            writer.writerow(row)
