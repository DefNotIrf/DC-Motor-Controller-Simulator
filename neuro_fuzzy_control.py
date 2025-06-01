import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def run_neuro_fuzzy(load_disturbance=0.0):
    data = pd.read_csv("dc_motor_data.csv")
    reference_speed = 1.0
    actual_speed = data['Normalized Speed'].values - load_disturbance
    actual_speed = np.clip(actual_speed, 0, None)

    error = reference_speed - actual_speed
    delta_error = np.append([0], np.diff(error))

    X = np.column_stack((error, delta_error))
    y = actual_speed

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = MLPRegressor(hidden_layer_sizes=(10,), activation='tanh', max_iter=1000, random_state=42)
    model.fit(X_scaled, y)
    y_pred = model.predict(X_scaled)
    mse = mean_squared_error(y, y_pred)

    return y, y_pred, mse
