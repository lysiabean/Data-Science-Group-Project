import re
import requests
import csv
from bs4 import BeautifulSoup


with open("Weather2015.csv", "w", newline = "") as csvfile:

    writer = csv.writer(csvfile) 
    writer.writerow(["Date", "Time(PST)", "Temp.", "Windchill", "Dew Point", "Humidity", "Pressure", "Visibility", "Wind Dir", "Wind Speed",
                     "Gust Speed", "Precip", "Events", "Conditions"])
    year = 2015
    for b in range(12):
        if (b + 1 == 2):
            days = 28
        elif (b + 1 == 1):
            days = 31
        elif (b + 1 == 3):
            days = 31
        elif (b + 1 == 5):
            days = 31
        elif (b + 1 == 7):
            days = 31
        elif (b + 1 == 8):
            days = 31
        elif (b + 1 == 10):
            days = 31
        elif (b + 1 == 12):
            days = 31
        else:
            days = 30
        for a in range(days):
            link = "http://english.wunderground.com/history/airport/KBFI/" + str(year) + "/"+str(b+1)+ "/" + str(a+1) + "/DailyHistory.html"
            r = requests.get(link)
            soup = BeautifulSoup(r.content)

            test = len(soup.find_all("th"))

            if (test == 20):
                n = 0
                yes = True
                while(yes == True):
                    try:
                        table = soup.find_all("tr", "no-metars")
                        temp = table[n].text.split()
                        if (temp[4] == "-"):
                            temp.insert(5, "")
                        if (temp[14] == "Calm"):
                            temp.insert(15, "")
                        if (temp[16] == "-"):
                            temp.insert(17, "")
                        if (temp[18] == "N/A"):
                            temp.insert(19, "")
                        if (temp[20] != "Rain"):
                            temp.insert(20, "-")
                        if (len(temp) == 23):
                            temp1 = [str(year) + "/"+str(b+1)+ "/" + str(a+1), temp[0]+temp[1], temp[2]+temp[3], temp[4]+temp[5], temp[6]+temp[7], temp[8], temp[9]+temp[10], temp[11]+temp[12],
                                 temp[13], temp[14]+temp[15], temp[16]+temp[17], temp[18]+temp[19], temp[20], temp[21]+temp[22]]
                        else:
                            temp1 = [str(year) + "/"+str(b+1)+ "/" + str(a+1), temp[0]+temp[1], temp[2]+temp[3], temp[4]+temp[5], temp[6]+temp[7], temp[8], temp[9]+temp[10], temp[11]+temp[12],
                                 temp[13], temp[14]+temp[15], temp[16]+temp[17], temp[18]+temp[19], temp[20], temp[21]]
                    except IndexError:
                        temp1 = []
                    print(temp1)
                    writer.writerow(temp1)
                    n = n + 1
                    try:
                        table[n]
                    except IndexError:
                        yes = False
                        
            else:
                n = 0
                yes = True
                while(yes == True):
                    try:
                        table = soup.find_all("tr", "no-metars")
                        temp = table[n].text.split()
                        if (temp[12] == "Calm"):
                            temp.insert(13, "")
                        if (temp[14] == "-"):
                            temp.insert(15, "")
                        if (temp[16] == "N/A"):
                            temp.insert(17, "")
                        if (temp[18] != "Rain"):
                            temp.insert(18, "-")
                        if (len(temp) == 21):
                            temp2 = [str(year) + "/"+str(b+1)+ "/" + str(a+1), temp[0]+temp[1], temp[2]+temp[3], "-", temp[4]+temp[5], temp[6], temp[7]+temp[8], temp[9]+temp[10],
                                 temp[11], temp[12]+temp[13], temp[14]+temp[15], temp[16]+temp[17], temp[18], temp[19]+temp[20]]
                        else:
                            temp2 = [str(year) + "/"+str(b+1)+ "/" + str(a+1), temp[0]+temp[1], temp[2]+temp[3], "-", temp[4]+temp[5], temp[6], temp[7]+temp[8], temp[9]+temp[10],
                                 temp[11], temp[12]+temp[13], temp[14]+temp[15], temp[16]+temp[17], temp[18], temp[19]]
                    except IndexError:
                        temp2 = []
                    print(temp2)
                    writer.writerow(temp2)
                    n = n + 1
                    try:
                        table[n]
                    except IndexError:
                        yes = False

            


