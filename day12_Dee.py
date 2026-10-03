import secrets


def list_of_hexa_colors(number):
	return [f"#{secrets.token_hex(3)}" for _ in range(number)]


def list_of_rgb_colors(number):
	return [
		f"rgb({secrets.randbelow(256)}, {secrets.randbelow(256)}, {secrets.randbelow(256)})"
		for _ in range(number)
	]


def generate_colors(color_type, number):
	if color_type == "hexa":
		return list_of_hexa_colors(number)
	if color_type == "rgb":
		return list_of_rgb_colors(number)
	raise ValueError("color_type must be 'hexa' or 'rgb'")

def shuffle_list(items):
	shuffled = items.copy()
	secrets.SystemRandom().shuffle(shuffled)
	return shuffled


def seven_random_numbers():
	return secrets.SystemRandom().sample(range(10), 7)


