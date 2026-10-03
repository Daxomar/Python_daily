import re

def clean_text(text):
	cleaned = re.sub(r"[^A-Za-z\s]", "", text)
	return re.sub(r"\s+", " ", cleaned).strip()

def most_frequent_words(text):
	frequencies = {}
	for word in text.split():
		frequencies[word] = frequencies.get(word, 0) + 1
	return sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:3]

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))

paragraph = (
	"I love teaching. If you do not love teaching what else can you love. "
	"I love Python if you do not love something which can give you all the "
	"capabilities to develop an application what else can you love."
)
words = re.findall(r"[A-Za-z]+", paragraph)
frequencies = {}
for word in words:
	frequencies[word] = frequencies.get(word, 0) + 1
most_common = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
print(most_common)
print(f"Most frequent word: {most_common[0]}")

points_text = "-12, -4, -3, -1, 0, 4, 8"
points = sorted(map(int, re.findall(r"-?\d+", points_text)))
distance = points[-1] - points[0]
print(f"Distance between furthest particles: {distance}")

def is_valid_variable(name):
	return bool(re.fullmatch(r"[A-Za-z_]\w*", name))
print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))

