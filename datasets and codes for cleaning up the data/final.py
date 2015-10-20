import csv

first = open("ChangedTimeCA.csv")
reader1 = csv.reader(first)



with open("time_visibility_rain_highway", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hour", "Highway", "Visibility", "Rain"])
    for row1 in reader1:
        #print("pass")
        second = open("noDuplicateWeather.csv")
        reader2 = csv.reader(second)
        for row2 in reader2:
            if (row1[2].strip() == row2[0].strip()):
                hour = row1[2].split()[1]
                if (row2[10] == "N/A"):
                    rain = 0
                else:
                    rain = 1
                temp = [hour, row1[3], row2[6], rain]
                writer.writerow(temp)
    print("done")
