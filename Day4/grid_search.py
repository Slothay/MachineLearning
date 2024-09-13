from sklearn.svm import SVR
import numpy as np

#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn-model-selection-gridsearchcv
from sklearn.model_selection import GridSearchCV

X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y = np.array([2, 4, 6, 8])

# defining parameter range 
param_grid = {'C': [0.1, 1, 10],  
              'gamma': [0.1, 0.01, 0.001], 
              'kernel': ['linear','rbf']}  
# Parameters: https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#rbf-svm-parameters

# verbose 1-3 can give printed info during fit
grid = GridSearchCV(SVR(), param_grid, cv=2, verbose=3) 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cvint%2C%20cross%2Dvalidation%20generator%20or%20an%20iterable%2C%20default%3DNone

# fitting the model for grid search 
grid.fit(X, y) 

print("Best parameters: ", grid.best_params_)
print("Best Score", grid.best_score_)
print("Best_estimator", grid.best_estimator_)

print(grid.predict([[6,3]]))






