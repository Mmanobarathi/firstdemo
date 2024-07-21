import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv("Forest_fire.csv")

# Extract features (X) and target (y)
X = data.iloc[:, 1:-1].values  # Features (all rows, columns 1 through second-to-last)
y = data.iloc[:, -1].values    # Target (all rows, last column)

# Convert target y to integer type
y = y.astype('int')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialize and train the logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Save the trained model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(log_reg, f)

print("Model saved successfully as model.pkl")

