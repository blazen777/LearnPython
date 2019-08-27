import csv

streets = {}

with open('ostanovka.csv', 'r', encoding='cp1251')as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        if row['Street'] in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1

streets = sorted(streets.items(), key=lambda item: item[1], reverse=True)

with open('num_ostanov.csv', 'w', encoding='utf-8') as fw:
    writer = csv.writer(fw)
    writer.writerow(['Name', 'Count'])
   
    for street in streets:
        writer.writerow(street)
