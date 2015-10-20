# highway
# rain
# visibility = 0
import csv

wanted = open("FinalData.csv")
reader = csv.reader(wanted)
with open("noDuplicateWeather.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    for row in reader:
        if(row[0] != "CAD CDW ID"): #getting rid of header
            date = row[2].split()[0]
            time = row[2].split()[1]
            #print(time)
            hour = int(time.split(":")[0])
            minutes = int(time.split(":")[1])
            if (minutes >= 30):
                hour = hour + 1
            if (hour == 24):
                hour = 0
            finalTime = hour
            print(finalTime)
            row[2] = date + " " + str(finalTime)
            writer.writerow(row)
            print("pass")
        else:
            writer.writerow(row)
