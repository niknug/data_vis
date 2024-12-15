import csv

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

plt.title("Daily High Temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
