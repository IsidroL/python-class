import json



#Create the data dictionary

data= {

    'name': 'John Doe',
    'age':30,
    'city': 'New York,NY',
    'interests': ['golf','running','videogames'],
    'is_student': False
}


# Writing data to a json file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data written to data.json.')


# Reading data from a JSON file 
with open('data.json', 'r') as json_file:

    loaded_data = json.load