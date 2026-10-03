emptup = ()

brotup = ('John', 'Doe', 'Damian', 'Smith')
print(brotup)
sistup = ('Alice', 'Johnson')
print(sistup)
sibtup = brotup + sistup
print(sibtup)
print("The total number of siblings is: ", len(sibtup))
family_tup = sibtup + ('Adam', 'Eve')
print(family_tup)
print("Siblings:", family_tup[0:4])
print("Parents:", family_tup[4:6])
fruits = ('apple', 'banana', 'cherry', 'date')
print(fruits)
vegetables = ('asparagus', 'broccoli', 'carrot', 'daikon')
print(vegetables)
animal_products = ('milk', 'cheese', 'yogurt', 'butter')
print(animal_products)
foos_stuff_tp = fruits + vegetables + animal_products
print(foos_stuff_tp)
foods_list = list(foos_stuff_tp)
print(foods_list)
print("The middle item is:", foods_list[len(foods_list) // 2])
print("The first three items are:", foods_list[:3])
print("The last three items are:", foods_list[-3:])
del foos_stuff_tp
print("The foods tuple has been deleted.")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country.")
else:
    print("Estonia is not a Nordic country.")
if 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country.")
else:
    print("Iceland is not a Nordic country.")
