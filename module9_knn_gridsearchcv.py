import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def get_user_input(num_pairs, set_name):
    print(f"\nEnter {num_pairs} (x, y) pairs for the {set_name} set:")
    pairs = np.zeros((num_pairs, 2), dtype=float)
    for i in range(num_pairs):
        while True:
            try:
                x = float(input(f"Enter x value for pair {i + 1}: "))
                y = int(input(f"Enter y value for pair {i + 1} (non-negative integer): "))
                if y < 0:
                    raise ValueError
                pairs[i, 0] = x
                pairs[i, 1] = y
                break
            except ValueError:
                print("Invalid input. X should be a real number and Y a non-negative integer. Please try again.")
    return pairs

def main():
    while True:
        try:
            N = int(input("Enter the number of training pairs (N, positive integer): "))
            if N <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. N should be a positive integer. Please try again.")
    
    train_data = get_user_input(N, "training")
    X_train = train_data[:, 0].reshape(-1, 1)
    y_train = train_data[:, 1].astype(int)
    print(f"Train set input features: {X_train}")
    print(f"Train set class labels: {y_train}")

    while True:
        try:
            M = int(input("\nEnter the number of test pairs (M, positive integer): "))
            if M <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. M should be a positive integer. Please try again.")

    test_data = get_user_input(M, "test")
    X_test = test_data[:, 0].reshape(-1, 1)
    y_test = test_data[:, 1].astype(int)
    print(f"Test set input features: {X_test}")
    print(f"Test set class labels: {y_test}")

    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1, 11))}
    grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, scoring='accuracy', cv=2)
    print("\nPerforming hyperparameter search using GridSearchCV...")

    grid_search.fit(X_train, y_train)

    best_k = grid_search.best_params_['n_neighbors']
    best_cv_score = grid_search.best_score_

    print(f"\nBest k found by GridSearchCV (based on cross-validation): {best_k}")
    print(f"Corresponding Cross-Validation Accuracy: {best_cv_score:.4f}")

    best_knn_model = grid_search.best_estimator_
    y_pred_test = best_knn_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred_test)

    print(f"\nTest Accuracy with the best k ({best_k}): {test_accuracy:.4f}")

if __name__ == "__main__":
    main()