import csv
from matplotlib import pyplot
from datetime import datetime

fileName = "death_valley_2014.csv"
with open(fileName) as file:
    reader = csv.reader(file)
    headers = next(reader)
    
    highs, dates, lows = [], [], []
    for row in reader:
        print(row)
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
        
diagram = pyplot.figure(figsize=(10, 5), dpi=128)

pyplot.plot(dates, highs, c='red')
pyplot.plot(dates, lows, c='blue')

pyplot.fill_between(dates, highs, lows, facecolor="blue", alpha=.2)

diagram.autofmt_xdate()
pyplot.title("Daily Highs and Lows in 2014", fontsize=20)
pyplot.xlabel("Date", fontsize=12)
pyplot.ylabel("Temperature (F)", fontsize=12)
pyplot.tick_params(axis="both", which='major', labelsize=12)

pyplot.show()






