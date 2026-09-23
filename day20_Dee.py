import re
from collections import Counter
from statistics import mean, median, stdev
import pandas as pd
import requests
from bs4 import BeautifulSoup


CAT_API = "https://api.thecatapi.com/v1/breeds"
COUNTRIES_API = "https://restcountries.com/v2/all"
UCI_URL = "https://archive.ics.uci.edu/ml/datasets.php"


def numbers(value):
	"""Return numbers from strings such as '3 - 5' or '12 - 15 years'."""
	return [float(x) for x in re.findall(r"\d+(?:\.\d+)?", str(value))]


def summary(values):
	values = [float(x) for x in values]
	return {
		"min": min(values),
		"max": max(values),
		"mean": mean(values),
		"median": median(values),
		"standard_deviation": stdev(values) if len(values) > 1 else 0,
	}


def cat_analysis():
	cats = requests.get(CAT_API, timeout=30).json()
	# Breed ranges are represented by their midpoint for numerical summaries.
	weights = [mean(numbers(c["weight"]["metric"])) for c in cats if numbers(c["weight"]["metric"])]
	lifespans = [mean(numbers(c["life_span"])) for c in cats if numbers(c["life_span"])]
	country_breed = Counter(
		(c.get("origin", "Unknown"), c.get("name", "Unknown")) for c in cats
	)
	print("CAT WEIGHT (kg):", summary(weights))
	print("CAT LIFESPAN (years):", summary(lifespans))
	print("COUNTRY/BREED FREQUENCY TABLE:")
	print(pd.DataFrame(country_breed.items(), columns=["country_breed", "frequency"]))


def countries_analysis():
	response = requests.get(COUNTRIES_API, timeout=30)
	response.raise_for_status()
	countries = response.json()
	largest = sorted(countries, key=lambda c: c.get("area") or 0, reverse=True)[:10]
	language_counts = Counter(
		language.get("name")
		for country in countries
		for language in country.get("languages", [])
		if language.get("name")
	)
	print("10 LARGEST COUNTRIES:")
	print(pd.DataFrame([{"country": c["name"], "area_km2": c.get("area")} for c in largest]))
	print("10 MOST SPOKEN LANGUAGES:")
	print(pd.DataFrame(language_counts.most_common(10), columns=["language", "countries"]))
	print("TOTAL DISTINCT LANGUAGES:", len(language_counts))


def uci_analysis():
	response = requests.get(UCI_URL, timeout=30)
	response.raise_for_status()
	soup = BeautifulSoup(response.text, "html.parser")
	rows = []
	for row in soup.select("tr"):
		cells = [cell.get_text(" ", strip=True) for cell in row.select("td, th")]
		if cells:
			rows.append(cells)
	print("UCI DATASET PAGE: {} rows found".format(len(rows)))
	for row in rows[:10]:
		print(" | ".join(row))


if __name__ == "__main__":
	cat_analysis()
	countries_analysis()
	uci_analysis()
