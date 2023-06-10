class Hebrews:
	def __init__(self, n):
		self.n = n

	def who_is_joseph(self, k):
		print(f"In a circle of {self.n} people, killing number {k}")
		
		h = list(range(self.n))
		i = 1

		while len(h) > 1:
			i = (i + k - 1) % len(h)
			del h[i]

		return f"Joseph is the Hebrew in position {h[0]}"
