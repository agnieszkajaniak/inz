import csv
with open('data.csv') as f:
    records = csv.DictReader(f)
    data = list(records)

unique_countries = set()
for row in data:
    unique_countries.add(row['asylum'])
    unique_countries.add(row['origin'])

with open('countries_i_want.csv') as f:
    records = csv.reader(f)
    countries_i_want = list(map(lambda x: x[0], records))

filtered_data = list(filter(
    lambda x: x['asylum'] in countries_i_want and x['origin'] in countries_i_want, data))
