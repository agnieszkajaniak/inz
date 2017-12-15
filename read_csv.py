import pandas as pd
import json

data = pd.read_csv("data.csv")
data[["value"]] = data[["value"]].apply(pd.to_numeric, errors='coerce')
data.fillna(0, inplace=True)

country_names = pd.read_csv("country_names_mapping.csv")
filtered_data = data[data["asylum"].isin(country_names["name"]) & data["origin"].isin(country_names["name"])]


d = country_names[["name", "iso"]]
dictionary = d.set_index('name').to_dict()["iso"]

filtered_data["asylum"].replace(dictionary, inplace=True)
filtered_data["origin"].replace(dictionary, inplace=True)
filtered_data["value"] = filtered_data["value"].astype(int)

filtered_data_by_year = filtered_data.groupby(["asylum", "origin", "year"]).sum()
data_array = filtered_data_by_year.reset_index().as_matrix()


data_array = list(map(
    lambda x: {"asylum": x[0],"origin": x[1], "year": x[2], "value": x[3]},
    data_array
))

data_array = list(filter(lambda x: x["value"] > 0, data_array))

with open('result.json', 'w') as fp:
    json.dump(data_array, fp)


