from module5_mod import NumberList

def main():
	while True:
		try:
			N = int(input("Enter a positive integer N: "))
			if (N <= 0):
				raise ValueError
			break
		except ValueError:
			print("Please enter a valid positive integer.")

	number_list = NumberList()

	for i in range(N):
		while True:
			try:
				num = int(input(f"Enter number {i + 1}: "))
				number_list.insert(num)
				break
			except ValueError:
				print("Please enter a valid integer.")

	while True:
		try:
			X = int(input("Enter the number X to search for: "))
			break
		except ValueError:
			print("Please enter a valid integer.")

	position = number_list.search(X)
	print(position)


if __name__ == "__main__":
	main()