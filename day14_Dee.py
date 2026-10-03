from collections import Counter
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Define callbacks before using them with map, filter, or reduce.
def to_upper(value):
	return value.upper()


def square(value):
	return value * value


def add(left, right):
	return left + right


def has_land(country):
	return "land" in country.lower()


for country in countries:
	print(country)
for name in names:
	print(name)
for number in numbers:
	print(number)

# Level 2
uppercase_countries = list(map(to_upper, countries))
square_numbers = list(map(square, numbers))
uppercase_names = list(map(to_upper, names))
land_countries = list(filter(has_land, countries))
six_character_countries = list(filter(lambda country: len(country) == 6, countries))
at_least_six_countries = list(filter(lambda country: len(country) >= 6, countries))
e_countries = list(filter(lambda country: country.startswith("E"), countries))

# Chain map, filter, and reduce.
chained = reduce(
	lambda result, item: f"{result}, {item}" if result else item,
	filter(lambda item: "A" in item, map(to_upper, countries)),
	"",
)


def get_string_lists(items):
	return list(filter(lambda item: isinstance(item, str), items))


sum_numbers = reduce(add, numbers, 0)
country_sentence = reduce(
	lambda result, country: f"{result}, {country}", countries[1:], countries[0]
) + " are north European countries"


def categorize_countries(items, pattern):
	return list(filter(lambda country: pattern.lower() in country.lower(), items))


def country_starting_letter_counts(items):
	return dict(Counter(country[0].upper() for country in items))


def get_first_ten_countries(items):
	return items[:10]


def get_last_ten_countries(items):
	return items[-10:]


# Level 3: records have the shape used by countries-data.py.
def sort_countries_by(records, field):
	return sorted(records, key=lambda record: record[field])


def ten_most_spoken_languages(records):
	counts = Counter(
		language for record in records for language in record.get("languages", [])
	)
	return counts.most_common(10)


def ten_most_populated_countries(records):
	return sorted(records, key=lambda record: record["population"], reverse=True)[:10]


# Closure and decorator examples.
def make_multiplier(factor):
	def multiply(value):
		return value * factor
	return multiply


def announce(function):
	def wrapper(*args, **kwargs):
		print(f"Calling {function.__name__}")
		return function(*args, **kwargs)
	return wrapper


@announce
def greet(name):
	return f"Hello, {name}!"
