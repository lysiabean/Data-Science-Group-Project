import csv

wanted = open("ChangedTimeWeather.csv")
reader = csv.reader(wanted)

with open("noDuplicateWeather.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    temp = ""
    for row in reader:
        if (temp != row[0]):
            writer.writerow(row)
        temp = row[0]
        
