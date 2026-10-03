names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

for index, country in enumerate(names):
	if country == 'Estonia':
		es = country
	if country == 'Russia':
		ru = country

nordic_countries = [*names[:5], es, ru]
nordic_countries.pop()
nordic_countries.pop()

print(nordic_countries)

