import numpy as np
from sklearn.metrics import precision_score, recall_score

def calculate_precision_recall():
	try:
		N = int(input("Enter the number of data points (N): "))
		if N <= 0:
			print("N must be a positive integer.")
			return

		X_ground_truths = np.empty(N)
		Y_predictions = np.empty(N)

		print(f"Enter {N} data points (ground truth, prediction): ")
		for i in range(N):
			while True:
				x = int(input(f"Enter ground truth (0 or 1) for point {i + 1}: "))
				if x in [0, 1]:
					break
				else:
					print("Ground truth must be 0 or 1. Please try again.")

			while True:
				y = int(input(f"Enter prediction (0 or 1) for point {i + 1}: "))
				if y in [0, 1]:
					break
				else:
					print("Prediction must be 0 or 1. Please try again.")
			
			X_ground_truths[i] = x
			Y_predictions[i] = y

		print("\n--- Results ---")
		print(f"Ground Truths: {X_ground_truths}")
		print(f"Predictions:   {Y_predictions}")

		precision = precision_score(X_ground_truths, Y_predictions, pos_label=1, zero_division="warn")
		recall = recall_score(X_ground_truths, Y_predictions, pos_label=1, zero_division="warn")

		print(f"\nPrecision: {precision:.4f}")
		print(f"Recall:    {recall:.4f}")
	except ValueError:
		print("Invalid input. Please enter numeric values")


if __name__ == "__main__":
    calculate_precision_recall()
