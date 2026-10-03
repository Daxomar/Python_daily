# ---------------- Dog dictionary ----------------

dog = {}
dog["name"] = "Buddy"
dog["color"] = "brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 5
print("The length of the dog dictionary is: " + str(len(dog)))


# ---------------- Student dictionary ----------------

student = {
    'first_name': 'KDee',
    'last_name': 'Miller',
    'gender': 'Female',
    'age': 25,
    'marital_status': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Finland',
    'city': 'Helsinki',
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Length of the student dictionary
print("The length of the student dictionary is: " + str(len(student)))

# Value of skills + data type check
print("The value of the skills key is: " + str(student['skills']))
print("The data type of the skills key is: " + str(type(student['skills'])))

# Modify skills - add one or two
student['skills'].append('HTML')
student['skills'].append('CSS')
print("The updated value of the skills key is: " + str(student['skills']))

# Keys as a list
print("The dictionary of student keys are: " + str(list(student.keys())))

# Values as a list
print("The dictionary of student values are: " + str(list(student.values())))

# Dictionary to list of tuples via items()
items = student.items()
print("The dictionary of student items are: " + str(list(items)))

# Delete one item
del student['age']
print("The updated dictionary of student keys are: " + str(list(student.keys())))

# Delete the entire dictionary
del student
# student no longer exists at this point - referencing it now would raise a NameError