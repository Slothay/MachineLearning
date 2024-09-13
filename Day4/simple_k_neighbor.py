import numpy as np

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [self.euclidean_distance(x, x_train) for x_train in self.X_train]

        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]

        # Extract the labels of the k nearest neighbor training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Return the most common class label
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common

# Example usage:
if __name__ == "__main__":
    # Sample data
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([0, 0, 1, 1])
    
    # Initialize and fit the KNN classifier
    knn = KNNClassifier(k=2)
    knn.fit(X_train, y_train)
    
    # Predict a new data point
    X_new = np.array([2.5, 3.5])
    y_pred = knn.predict([X_new])
    
    print("Predicted class:", y_pred[0])
