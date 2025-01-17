import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os

# Load the data with relative path
data_path = os.path.join('data', 'iter.csv')  # Adjusted to reflect a relative path for CI/CD
data = pd.read_csv(data_path)

# Clean the 'Salary' column by removing commas and converting it to a numeric type
data['Salary'] = data['Salary'].replace({',': ''}, regex=True).astype(float)

# Split features and target
X = data[['Age', 'Salary']]
y = data['Purchased']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model initialization
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
