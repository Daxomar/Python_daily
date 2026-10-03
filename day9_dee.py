
# 1. Age check with missing-years feedback
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")


# 2. Compare my_age and your_age, with singular/plural handling
my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    word = "year" if diff == 1 else "years"
    print(f"You are {diff} {word} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    word = "year" if diff == 1 else "years"
    print(f"I am {diff} {word} older than you.")
else:
    print("We are the same age.")


# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# ---------------- Level 2 ----------------

# 1. Grades
score = int(input("Enter Your Score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# 2. Season from month
month = input("Enter the month: ")
if month in ("September", "October", "November"):
    print("The season is Autumn")
elif month in ("December", "January", "February"):
    print("The season is Winter")
elif month in ("March", "April", "May"):
    print("The season is Spring")
elif month in ("June", "July", "August"):
    print("The season is Summer")
else:
    print("Not a valid month")


# 3. Fruit list - print modified list
fruits = ['banana', 'orange', 'mango', 'lemon']
unkfruit = input("Enter a fruit: ")
if unkfruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(unkfruit)
    print(fruits)


# ---------------- Level 3 ----------------

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Middle skill (only if 'skills' key exists)
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("The middle skill is:", skills[middle_index])

# 2. Check for Python skill specifically
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")

# 3. Developer title - check the skill set as a whole.
#    Order matters: check the more specific/larger combos first,
#    since this person actually qualifies for more than one.
skills = person['skills']
if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
else:
    print('unknown title')

# 4. Married + country check
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in {person['country']}.")