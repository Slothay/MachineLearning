from sklearn.datasets import make_classification

# Generate a random classification dataset
X, y = make_classification(n_informative=3, n_samples=200, n_features=10, n_classes=4, random_state=42)

import pandas as pd

df = pd.DataFrame(X,y)
print(df.head)
df.to_csv("classify.csv", index= False)
