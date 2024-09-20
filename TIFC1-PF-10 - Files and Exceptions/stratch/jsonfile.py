import json

# Example data to be written to a JSON file
data = {
    "name": "Frankie",
    "age": 4,               # this is dictonary
    "fur": "shaded red"
}

# Write data to a JSON file using json.dump()
#filename = "data.json"
filename = "IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/stratch/data.json"
with open(filename, "w") as json_file:
    json.dump(data, json_file)      # using dump method 
print("Data successfully written to:", filename)

# Reading data from JSON file using json.load()
#with open(filename, "r") as json_file:
with open(filename, "r") as json_file:
    loaded_data = json.load(json_file)
print("Data loaded from:", filename, "-")
print(loaded_data)