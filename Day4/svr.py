from sklearn.svm import SVR

import numpy as np

X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y = np.array([2, 4, 6, 8])

# Create a Support Vector Machine for regression
model = SVR(kernel='linear')

# Fit the model
model.fit(X, y)


y_pred = model.predict([[5,5]])

print(y_pred)
