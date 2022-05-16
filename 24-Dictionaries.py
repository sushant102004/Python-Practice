# Dictionaries is datatype that store data in key value pair.
carDetails = {
    'name': 'BMW',
    'model': 'Z4',
    'year': 2018
}

# print(carDetails)
# print(carDetails['name'])

# Dictionaries are changeable so we can change, add or delete data after it is created.
# Dictionaries can't have duplicate key values. If there is duplicate key then the data will be overwritten.

dictOne = {
    'name': 'Sushant',
    'stream': 'B. Tech',
    'name': 'John'
}
# print(dictOne)

# Dictionaries can have diffrent data types also.
studentDetail = {
    'name': 'Sushant',
    'rollNo': 11212531,
    'isRegistered': True,
    'favSubjects': ['Python', 'Internet of Things']
}
# print(dictTwo)

# Dictionaries access methods
studentDetail['name']
x = studentDetail.get('rollNo')
y = studentDetail.keys()
z = studentDetail.values()
a = studentDetail.items()

# Conditional Statements
# if 'name' in dictTwo:
#     print('Name exists in dictTwo')

# Changing Dictionary Items
dictThree = {
    'name': 'John',
    'profession': 'UI Designer'
}
dictThree['name'] == 'Rock'
dictThree.update({'name': 'Ben'})

# Add Items
dictThree['salary'] = '$10000'
dictThree.update({'salary': '$15000'})

# Remove Elements
# dictThree.pop('salary')
# dictThree.popitem() # This will remove last element
# del dictThree['name']

# for x in studentDetail:
#     print(x)

# for i in studentDetail:
#     print(studentDetail[i])

# for x, y in studentDetail.items():
#     print(x, y)

# Nested Loop
family = {
    'mother': {
        'name': 'Lisa',
        'dob': 1990
    },
    'father': {
        'name': 'Bryan',
        'dob': 1989
    },
    'childOne': {
        'name': 'Robin',
        'dob': 2013
    }
}
