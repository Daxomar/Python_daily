"""Download the requested pages and save their tabular/content data as JSON.

Dependencies: requests, beautifulsoup4, pandas
"""

import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


OUT = Path("scraped_json")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; data-collection script)"}


def get_soup(url):
	response = requests.get(url, headers=HEADERS, timeout=30)
	response.raise_for_status()
	return BeautifulSoup(response.text, "html.parser")


def write_json(filename, value):
	OUT.mkdir(exist_ok=True)
	(OUT / filename).write_text(
		json.dumps(value, indent=2, ensure_ascii=False, default=str), encoding="utf-8"
	)


def scrape_bu_facts():
	url = "http://www.bu.edu/president/boston-university-facts-stats/"
	soup = get_soup(url)
	tables = []
	for table in soup.find_all("table"):
		rows = []
		for row in table.find_all("tr"):
			cells = [cell.get_text(" ", strip=True) for cell in row.find_all(["th", "td"])]
			if cells:
				rows.append(cells)
		if rows:
			tables.append(rows)
	write_json("bu_facts_stats.json", {"url": url, "tables": tables})


def scrape_uci_datasets():
	url = "https://archive.ics.uci.edu/ml/datasets.php"
	soup = get_soup(url)
	datasets = []
	for table in soup.find_all("table"):
		rows = []
		for row in table.find_all("tr"):
			cells = [
				cell.get_text(" ", strip=True)
				for cell in row.find_all(["th", "td"])
			]
			if len(cells) >= 3:
				rows.append(cells)
		if len(rows) < 2:
			continue
		headers = rows[0]
		for cells in rows[1:]:
			datasets.append({
				(headers[i] if i < len(headers) and headers[i] else f"column_{i + 1}"): value
				for i, value in enumerate(cells)
			})
	write_json("uci_datasets.json", {"url": url, "datasets": datasets})


def scrape_us_presidents():
	url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
	soup = get_soup(url)
	presidents = []
	for table in soup.select("table.wikitable"):
		# Only retain the historical president tables, not unrelated side tables.
		headers = [
			re.sub(r"\[\d+\]", "", cell.get_text(" ", strip=True))
			for cell in table.find_all("th")[:12]
		]
		if not any("President" in header or "Term" in header for header in headers):
			continue
		for row in table.find_all("tr"):
			cells = [re.sub(r"\[\d+\]", "", c.get_text(" ", strip=True))
					 for c in row.find_all(["th", "td"])]
			if not cells or cells == headers:
				continue
			record = {
				(headers[i] if i < len(headers) and headers[i] else f"column_{i + 1}"): value
				for i, value in enumerate(cells)
			}
			if record:
				presidents.append(record)
	write_json("us_presidents.json", {"url": url, "presidents": presidents})


if __name__ == "__main__":
	scrape_bu_facts()
	scrape_uci_datasets()
	scrape_us_presidents()
	print(f"Saved JSON files to {OUT.resolve()}")
