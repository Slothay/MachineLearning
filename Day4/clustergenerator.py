import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Parameters
n_samples = 300  # Number of data points
n_features = 2   # Number of features
n_clusters = 3   # Number of clusters
random_state = 2  # Seed for reproducibility

# Generate synthetic data
X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=random_state)

# Create a DataFrame
data = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
# data['Cluster'] = y

# Save to CSV
data.to_csv('synthetic_data_unanot.csv', index=False)

# Plot the data
plt.scatter(data['Feature1'], data['Feature2'], cmap='viridis')
# plt.scatter(data['Feature1'], data['Feature2'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.title('Synthetic Data for Clustering')
plt.show()