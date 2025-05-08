class NumberList:
	def __init__(self):
		self.numbers = []

	def insert(self, number):
		self.numbers.append(number)

	def search(self, target):
		try:
			return self.numbers.index(target) + 1
		except ValueError:
			return -1