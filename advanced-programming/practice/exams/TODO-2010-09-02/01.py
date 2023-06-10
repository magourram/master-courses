KEYS = {
	'a': 2,
	'b': 2,
	'c': 2,
	'd': 3,
	'e': 3,
	'f': 3,
	'g': 4,
	'h': 4,
	'i': 4,
	'j': 5,
	'k': 5,
	'l': 5,
	'm': 6,
	'n': 6,
	'o': 6,
	'p': 7,
	'q': 7,
	'r': 7,
	's': 7,
	't': 8,
	'u': 8,
	'v': 8,
	'w': 9,
	'x': 9,
	'y': 9,
	'z': 9
}

def translate(w):
	return "".join(str(KEYS[c]) for c in w)

def translate_text(text, translated, dictionary):
	if text == []:
		return ""

	w, *rest = text

	candidates = [i for i, v in enumerate(translated) if w == v]
	highest = dictionary[max(candidates, key=lambda i: dictionary[i][1])][0]
	
	return highest + " " + translate_text(rest, translated, dictionary)

if __name__ == "__main__":

	dictionary = [(line.split(" ")[0], float(line.split(" ")[1])) \
		for line in open("dict-frequency.txt").read().strip().split("\n")]
	translated = [translate(w[0]) for w in dictionary]

	texts = open("t9's texts.txt").read().strip().split("\n")

	for text in texts:
		r = translate_text(text.split(), translated, dictionary)
		print(r)