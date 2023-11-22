import json



#Create the data dictionary

data= {

    'name': 'John Doe',
    'age': 25,
    'city': 'Seattle, WA',
    'interests': ['football', 'running', 'videogames'],
    'is_student': False
}


# Writing data to a json file
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent=4)

print('Data written to data.json')


# Reading data from a JSON file 
with open('data.json', 'r') as json_file:

    loaded_data = json.load(json_file)

print("Data loaded from data.json")
print(loaded_data)



# Select key and an integer modifications
loaded_data['age'] = 28
loaded_data["interests"].append('travel')


# Complete modifacation to the data.json file using with statement
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')