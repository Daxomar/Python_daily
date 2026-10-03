def add_two_numbers(a, b):
	return a + b

def areaCircle(r):
	return 22/7 * r*r

def add_all_nums(*nums):
	if not all(isinstance(num, (int, float, complex)) and not isinstance(num, bool) for num in nums):
		raise TypeError("All arguments must be numbers.")
	return sum(nums)


def convert_celsius_to_fahrenheit(celsius):
	return (celsius * 9 / 5) + 32


def check_season(month):
	months = {
		"autumn": {"september", "october", "november"},
		"winter": {"december", "january", "february"},
		"spring": {"march", "april", "may"},
		"summer": {"june", "july", "august"},
	}

	if isinstance(month, int) and not isinstance(month, bool):
		if month < 1 or month > 12:
			raise ValueError("Month must be between 1 and 12.")
		return ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
				"Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter")[month - 1]

	month_name = str(month).strip().lower()
	for season, season_months in months.items():
		if month_name in season_months:
			return season.capitalize()
	raise ValueError("Invalid month.")


def calculate_slope(x1, y1, x2, y2):
	if x2 == x1:
		raise ValueError("A vertical line has an undefined slope.")
	return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
	if a == 0:
		if b == 0:
			return () if c != 0 else "all real numbers"
		return (-c / b,)

	discriminant = b ** 2 - 4 * a * c
	if discriminant < 0:
		return ()
	if discriminant == 0:
		return (-b / (2 * a),)
	root = discriminant ** 0.5
	return ((-b + root) / (2 * a), (-b - root) / (2 * a))


def print_list(items):
	for item in items:
		print(item)


def reverse_list(array):
	reversed_array = []
	for index in range(len(array) - 1, -1, -1):
		reversed_array.append(array[index])
	return reversed_array


def capitalize_list_items(items):
	return [str(item).capitalize() for item in items]


def add_item(items, item):
	return items + [item]


def remove_item(items, item):
	result = list(items)
	result.remove(item)
	return result


def sum_of_numbers(number):
	return sum(range(1, number + 1))


def sum_of_odds(number):
	return sum(value for value in range(1, number + 1) if value % 2)


def sum_of_even(number):
	return sum(value for value in range(1, number + 1) if value % 2 == 0)


def evens_and_odds(number):
	if not isinstance(number, int) or isinstance(number, bool) or number < 0:
		raise ValueError("number must be a positive integer")
	return {
		"odds": sum(1 for value in range(number + 1) if value % 2),
		"evens": sum(1 for value in range(number + 1) if value % 2 == 0),
	}


def factorial(number):
	if not isinstance(number, int) or isinstance(number, bool) or number < 0:
		raise ValueError("number must be a whole number")
	result = 1
	for value in range(2, number + 1):
		result *= value
	return result


def is_empty(value):
	return len(value) == 0


def calculate_mean(values):
	return sum(values) / len(values)


def calculate_median(values):
	ordered = sorted(values)
	middle = len(ordered) // 2
	if len(ordered) % 2:
		return ordered[middle]
	return (ordered[middle - 1] + ordered[middle]) / 2


def calculate_mode(values):
	counts = {value: values.count(value) for value in values}
	maximum = max(counts.values())
	return [value for value, count in counts.items() if count == maximum]


def calculate_range(values):
	return max(values) - min(values)


def calculate_variance(values):
	mean = calculate_mean(values)
	return sum((value - mean) ** 2 for value in values) / len(values)


def calculate_std(values):
	return calculate_variance(values) ** 0.5


def greet(name="Guest"):
	print(f"Hello, {name}!")


def show_args(**kwargs):
	print("Received: " + ", ".join(f"{name}: {value}" for name, value in kwargs.items()))


def is_prime(number):
	if not isinstance(number, int) or number < 2:
		return False
	return all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))


def all_unique(items):
	return len(items) == len(set(items))


def same_data_type(items):
	return not items or all(type(item) is type(items[0]) for item in items)


def is_valid_variable(name):
	return isinstance(name, str) and name.isidentifier() and not __import__("keyword").iskeyword(name)

