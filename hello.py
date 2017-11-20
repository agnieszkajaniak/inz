import csv
import pandas as pd


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

filtered_data = pd.DataFrame(filtered_data)
filtered_data['value'] = pd.to_numeric(filtered_data['value'], errors='coerce')
print(filtered_data.groupby(['asylum', 'origin', 'year'])['value'].sum())

filtered_data = filtered_data.to_dict('records').values()

print(filtered_data[0])