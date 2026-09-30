from collections import Counter
import os
import re

from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ title }}</title>
</head>
<body>
  <nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
	<a href="/post">Text Analyzer</a>
  </nav>
  {% block content %}{% endblock %}
</body>
</html>
"""

home_template = template.replace(
	"{% block content %}{% endblock %}",
	"<h1>{{ name }}</h1><ul>{% for tech in techs %}<li>{{ tech }}</li>{% endfor %}</ul>",
)

about_template = template.replace(
	"{% block content %}{% endblock %}",
	"<h1>{{ name }}</h1>",
)

post_template = template.replace(
	"{% block content %}{% endblock %}",
	"""
	<h1>Text Analyzer</h1>
	<p>Enter text to analyze its word count, character count, and most frequent words.</p>
	<form method="post">
	  <textarea name="content" rows="20" cols="70" autofocus aria-label="Text to analyze">{{ content }}</textarea>
	  <button type="submit">Process Text</button>
	</form>
	{% if result %}
	<p>Words: {{ result.words }}</p>
	<p>Characters: {{ result.characters }}</p>
	<h2>Most frequent words</h2>
	<ul>{% for word, count in result.frequent %}<li>{{ word }}: {{ count }}</li>{% endfor %}</ul>
	{% endif %}
	""",
)


@app.route("/")
def home():
	return render_template_string(
		home_template,
		title="Home",
		name="30 Days Of Python Programming",
		techs=["HTML", "CSS", "Flask", "Python"],
	)


@app.route("/about")
def about():
	return render_template_string(
		about_template,
		title="About",
		name="30 Days Of Python Programming",
	)


@app.route("/post", methods=["GET", "POST"])
def post():
	content = request.form.get("content", "")
	words = re.findall(r"[\w']+", content.lower())
	result = None
	if request.method == "POST":
		result = {
			"words": len(words),
			"characters": len(content),
			"frequent": Counter(words).most_common(10),
		}
	return render_template_string(
		post_template,
		title="Text Analyzer",
		content=content,
		result=result,
	)


if __name__ == "__main__":
	app.run(
		debug=True,
		host="0.0.0.0",
		port=int(os.environ.get("PORT", 5000)),
	)
