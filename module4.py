N = int(input("Please enter a positive integer N: "))

if N <= 0:
	print("N must be a positive integer. Exiting.")
	exit()

numbers = []
for i in range(N):
	n = int(input(f"Enter number {i + 1}: "))
	numbers.append(n)

X = int(input("Please enter an integer: "))

if X in numbers:
	index = numbers.index(X) + 1
	print(index)
else:
	print("-1")