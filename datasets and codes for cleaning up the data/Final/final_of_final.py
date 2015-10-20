import csv

wanted = open("time_visibility_rain_highway.csv")
reader = csv.reader(wanted)

# name it clearly
with open("highway1_rain0_visibility1-5.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    for row in reader:
        if(row[0] == "Hour"):
            writer.writerow(row)
        else:
            # highway
            if(row[1] == "1"):
                # rain
                if(row[3] == "0"):
                    if(row[2].strip() == "0.1mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "0.2mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "0.5mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "0.8mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "1.0mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "1.2mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "1.5mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "1.8mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "2.0mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "2.5mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "3.0mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "4.0mi"):
                        writer.writerow(row)
                    if(row[2].strip() == "5.0mi"):
                        writer.writerow(row)
                        

