import pickle
import numpy as np

# Load trained model and scaler
with open(r"D:\Machine_L_Projects\Job placement\job_placment\placement\job_placement_model.pkl", "rb") as file:
    data = pickle.load(file)

model = data["model"]
scaler = data["scaler"]

# Function to predict job placement
def predict_job(features):
    input_feature = np.array(features).reshape(1, -1)  # Convert to NumPy array
    input_feature_scaled = scaler.transform(input_feature)  # Scale the features
    prediction = model.predict(input_feature_scaled)  # Predict


    if prediction[0] == 1:
        return "Placed"
    else:
        return "Not Placed"

