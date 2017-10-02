import csv
with open("data.csv") as f:
    records = csv.DictReader(f)
    data = list(records)
