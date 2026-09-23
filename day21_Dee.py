class Statistics:
	def __init__(self, values):
		if not values:
			raise ValueError("values must not be empty")
		self.values = list(values)

	def count(self):
		return len(self.values)

	def sum(self):
		return sum(self.values)

	def min(self):
		return min(self.values)

	def max(self):
		return max(self.values)

	def range(self):
		return self.max() - self.min()

	def mean(self):
		return self.sum() / self.count()

	def median(self):
		values = sorted(self.values)
		middle = self.count() // 2
		if self.count() % 2:
			return values[middle]
		return (values[middle - 1] + values[middle]) / 2

	def _frequencies(self):
		frequencies = {}
		for value in self.values:
			frequencies[value] = frequencies.get(value, 0) + 1
		return frequencies

	def mode(self):
		frequencies = self._frequencies()
		value = max(frequencies, key=lambda item: (frequencies[item], -item))
		return value, frequencies[value]

	def var(self):
		average = self.mean()
		return sum((value - average) ** 2 for value in self.values) / (self.count() - 1)

	def std(self):
		return self.var() ** 0.5

	def percentile(self, percent):
		if not 0 <= percent <= 100:
			raise ValueError("percent must be between 0 and 100")
		values = sorted(self.values)
		position = (len(values) - 1) * percent / 100
		lower = int(position)
		upper = min(lower + 1, len(values) - 1)
		return values[lower] + (values[upper] - values[lower]) * (position - lower)

	def freq_dist(self):
		frequencies = self._frequencies()
		return [
			(round(count * 100 / self.count(), 1), value)
			for value, count in sorted(
				frequencies.items(), key=lambda item: (-item[1], -item[0])
			)
		]

	def describe(self):
		return "\n".join([
			f"Count: {self.count()}",
			f"Sum:  {self.sum()}",
			f"Min:  {self.min()}",
			f"Max:  {self.max()}",
			f"Range:  {self.range()}",
			f"Mean:  {round(self.mean())}",
			f"Median:  {self.median()}",
			f"Mode:  {self.mode()}",
			f"Variance:  {round(self.var(), 1)}",
			f"Standard Deviation:  {round(self.std(), 1)}",
			f"Frequency Distribution: {self.freq_dist()}",
		])


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
		33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())


class PersonAccount:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.incomes = set()
		self.expenses = set()

	def total_income(self):
		return sum(amount for amount, _ in self.incomes)

	def total_expense(self):
		return sum(amount for amount, _ in self.expenses)

	def account_info(self):
		return (
			f"Name: {self.firstname} {self.lastname}\n"
			f"Total income: {self.total_income()}\n"
			f"Total expense: {self.total_expense()}\n"
			f"Account balance: {self.account_balance()}"
		)

	def add_income(self, amount, description):
		self.incomes.add((amount, description))

	def add_expense(self, amount, description):
		self.expenses.add((amount, description))

	def account_balance(self):
		return self.total_income() - self.total_expense()

