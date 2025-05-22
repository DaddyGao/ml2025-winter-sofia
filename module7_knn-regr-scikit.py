import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def knn_regression_with_variance():
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

		X_train = np.empty(N)
		y_train = np.empty(N)

		print(f"Enter {N} data points (x and y): ")
		for i in range(N):
			x = float(input(f"Enter x for point {i + 1}: "))
			y = float(input(f"Enter y for point {i + 1}: "))
			X_train[i] = x
			y_train[i] = y

		variance_of_labels = np.var(y_train)
		print(f"\nVariance of labels in the training dataset: {variance_of_labels:.4f}")

		x_query = float(input("Enter X value for prediction: "))
		x_reshaped = np.array([[x_query]])

		knn_regressor = KNeighborsRegressor(n_neighbors=k)
		knn_regressor.fit(X_train, y_train)
		y_pred = knn_regressor.predict(x_reshaped)

		print(f"Predicted Y value: {y_pred[0]:.4f}")
	except ValueError:
		print("Invalid input. Please enter numeric values")

if __name__ == "__main__":
	knn_regression_with_variance()