# highway
# rain
# visibility = 0
import csv

wanted = open("WeatherTotal.csv")
reader = csv.reader(wanted)
with open("ChangedTimeWeather.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    for row in reader:
        if(row[0] != "Date"): #getting rid of header
            date = row[0]
            time = row[1]
            temp = time.split(":")[1]
            hour = int(time.split(":")[0])

            noon = temp[2:4]
            if (noon == "AM"):
                hour = hour + 12
            
            minutes = int(temp[0:2])
            #print(minutes)
            if (minutes >= 30):
                hour = hour + 1
            if (hour == 24):
                hour = 0
            if (hour == 25):
                hour = 1
            finalTime = hour
            #print(finalTime)
            row = [date + " " + str(finalTime), row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                   row[9], row[10], row[11], row[12]] 
            writer.writerow(row)
            #print(date + " " + str(finalTime))
            #print("pass")
        else:
            writer.writerow(row)
