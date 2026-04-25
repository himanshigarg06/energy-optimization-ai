import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv('final_dataset.csv')

# Features (inputs)
X = df[['Peak Demand (MW)', 'Coal Requirement', 'Solar Potential (MW)', 'Wind Potential (MW)']]

# Target (what we predict)
y = df['Energy Deficit (MW)']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)

print("✅ Model trained successfully!")
print("Sample Predictions:", predictions[:5])
print("Actual Values:", y_test.values[:5])
print("MAE (Error):", mae)