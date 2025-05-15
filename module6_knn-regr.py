import numpy as np

class KNNRegressior:
	def __init__(self, k):
		self.k = k
		self.x_train = None
		self.y_train = None

	def fit(self, x, y):
		self.x_train = np.array(x)
		self.y_train = np.array(y)

	def predict(self, x_query):
		distances = np.abs(self.x_train - x_query)
		nearest_indices = np.argsort(distances)[:self.k]
		return np.mean(self.y_train[nearest_indices])

def main():
	try:
		N = int(input("Enter the number of data points (N): "))
		if N <= 0:
			print("N must be a positive integer.")
			return

		k = int(input("Enter the value of k: "))
		if k <= 0:
			print("k must be a positive integer.")
			return
		if k > N:
			print("k cannot be larger than N.")
			return

		x_points = []
		y_points = []

		print(f"Enter {N} data points (x and y): ")
		for i in range(N):
			x = float(input(f"Enter x for point {i + 1}: "))
			y = float(input(f"Enter y for point {i + 1}: "))
			x_points.append(x)
			y_points.append(y)

		x_query = float(input("Enter X value for prediction: "))

		model = KNNRegressior(k)
		model.fit(np.array(x_points), np.array(y_points))
		y_pred = model.predict(x_query)

		print(f"Predicted Y value: {y_pred:.4f}")
	except ValueError:
		print("Invalid input. Please enter numeric values")

if __name__ == "__main__":
	main()