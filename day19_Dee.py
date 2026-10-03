from pathlib import Path
import json
import re
from collections import Counter


def count_lines_and_words(filepath):
	"""Return the number of lines and whitespace-separated words in a file."""
	text = Path(filepath).read_text(encoding="utf-8")
	return len(text.splitlines()), len(text.split())

files = [
	"obama_speech.txt",
	"michelle_obama_speech.txt",
	"donald_speech.txt",
	"melina_trump_speech.txt",
]

for filename in files:
	path = Path("data") / filename
	lines, words = count_lines_and_words(path)
	print(f"{filename}: {lines} lines, {words} words")


def most_populated_countries(filename, count):
	"""Return the most populated countries from a JSON data file."""
	with open(filename, encoding="utf-8") as file:
		countries = json.load(file)

	return [
		{"country": country["name"], "population": country["population"]}
		for country in sorted(
			countries, key=lambda country: country["population"], reverse=True
		)[:count]
	]


print(most_populated_countries(filename="./data/countries_data.json", count=10))


def most_spoken_languages(filename, count):
	"""Return the most spoken languages and the number of countries using them."""
	with open(filename, encoding="utf-8") as file:
		countries = json.load(file)

	language_counts = {}
	for country in countries:
		for language in country["languages"]:
			language_counts[language] = language_counts.get(language, 0) + 1

	return sorted(
		((number, language) for language, number in language_counts.items()),
		reverse=True,
	)[:count]

print(most_spoken_languages(filename="./data/countries_data.json", count=10))


def extract_incoming_email_addresses(filename):
	"""Return all email addresses found in incoming messages."""
	text = Path(filename).read_text(encoding="utf-8")
	return re.findall(
		r"(?im)^from:\s*(?:[^<\n]*<)?([\w.+-]+@[\w.-]+\.[A-Za-z]{2,})",
		text,
	)


def find_most_common_words(source, count):
	"""Return the most common words in a text string or file."""
	if not isinstance(count, int) or count <= 0:
		raise ValueError("count must be a positive integer")

	path = Path(source)
	text = path.read_text(encoding="utf-8") if path.is_file() else source
	words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text)
	return Counter(words).most_common(count)


def _read_text(source):
	"""Read a file or return a text string unchanged."""
	path = Path(source) if isinstance(source, (str, Path)) else None
	return path.read_text(encoding="utf-8") if path and path.is_file() else str(source)


def clean_text(text):
	"""Convert text to lowercase word tokens."""
	return re.findall(r"[a-z]+(?:'[a-z]+)?", _read_text(text).lower())


def remove_support_words(words, stop_words=None):
	"""Remove common stop words from word tokens."""
	if stop_words is None:
		stop_words = set()
		stop_words_file = Path("data/stop_words.py")
		if stop_words_file.is_file():
			namespace = {}
			exec(stop_words_file.read_text(encoding="utf-8"), {}, namespace)
			stop_words = set(namespace.get("stop_words", []))
	return [word for word in words if word not in stop_words]


def check_text_similarity(first, second, stop_words=None):
	"""Return cosine similarity for two files or text strings."""
	first_counts = Counter(remove_support_words(clean_text(first), stop_words))
	second_counts = Counter(remove_support_words(clean_text(second), stop_words))
	all_words = set(first_counts) | set(second_counts)
	if not all_words:
		return 0.0
	dot_product = sum(first_counts[word] * second_counts[word] for word in all_words)
	first_length = sum(value * value for value in first_counts.values()) ** 0.5
	second_length = sum(value * value for value in second_counts.values()) ** 0.5
	return dot_product / (first_length * second_length)


print(extract_incoming_email_addresses("./data/email_exchange_big.txt"))
print(find_most_common_words("./data/sample.txt", 10))
print(find_most_common_words("./data/sample.txt", 5))

for speech in files:
	print(f"{speech}: {find_most_common_words(Path('data') / speech, 10)}")

print(
	"Michelle/Melania similarity:",
	check_text_similarity(
		Path("data/michelle_obama_speech.txt"),
		Path("data/melina_trump_speech.txt"),
	),
)


def count_hacker_news_keywords(filename):
	"""Count lines containing Python, JavaScript, and Java (excluding JavaScript)."""
	lines = Path(filename).read_text(encoding="utf-8").splitlines()
	python_count = sum("python" in line.lower() for line in lines)
	javascript_count = sum("javascript" in line.lower() for line in lines)
	java_count = sum(
		"java" in line.lower() and "javascript" not in line.lower()
		for line in lines
	)
	return python_count, javascript_count, java_count


python_count, javascript_count, java_count = count_hacker_news_keywords(
	"data/hacker_news.csv"
)
print(f"Python: {python_count}")
print(f"JavaScript: {javascript_count}")
print(f"Java (not JavaScript): {java_count}")

