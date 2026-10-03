numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number <= 0]
print(negative_and_zero)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [number for sublist in list_of_lists for number in sublist]
print(flattened)

powers = [(number, 1, number, number**2, number**3, number**4, number**5)
		  for number in range(11)]
print(powers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [[country.upper(), country[:3].upper(), city.upper()]
				for country_group in countries
				for country, city in country_group]
print(country_list)

country_dicts = [{'country': country.upper(), 'city': city.upper()}
				 for country_group in countries
				 for country, city in country_group]
print(country_dicts)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
		 [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f'{first} {last}'
					  for name_group in names
					  for first, last in name_group]
print(concatenated_names)
