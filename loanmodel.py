import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Load the dataset
df = pd.read_csv('./loan_dataset.csv')

# Drop missing values
df = df.dropna()

# Encode categorical columns
cat_cols = ['employment_status', 'reason_for_loan', 'vehicle_owner', 'realty_ownership']
encoders = {}
for col in cat_cols:
    enc = LabelEncoder()
    df[col] = enc.fit_transform(df[col])
    encoders[col] = enc

# Convert date_of_birth to age
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
df['age'] = 2025 - df['date_of_birth'].dt.year
df = df.drop(columns=['date_of_birth'])

# Split features and target
X = df.drop(columns=['credit_score'])
y = df['credit_score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model Trained")
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Save model and encoders
joblib.dump(model, 'credit_score_model.pkl')
joblib.dump(encoders, 'encoders.pkl')
joblib.dump(list(X.columns), 'feature_columns.pkl')  # Important for prediction ordering
