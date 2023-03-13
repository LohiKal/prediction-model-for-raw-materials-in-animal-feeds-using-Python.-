import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv("animal_feeds_ph.csv")

# Split data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Define features and target
features = ["raw_material_1", "raw_material_2", "raw_material_3"]
target = "crude_protein"

# Create model
model = LinearRegression()

# Train model on training data
model.fit(train_data[features], train_data[target])

# Make predictions on testing data
predictions = model.predict(test_data[features])

# Evaluate model performance
mse = mean_squared_error(test_data[target], predictions)
rmse = np.sqrt(mse)
print("Root mean squared error:", rmse)
