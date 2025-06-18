import numpy as np
import control as ctrl
import pandas as pd

# DC Motor Parameters
R, L, J, b, Kt, Ke = 1.0, 0.5, 0.01, 0.1, 0.01, 0.01

def motor_transfer_function():
    num = [Kt]
    den = [J*L, (J*R + L*b), (R*b + Kt*Ke)]
    return ctrl.TransferFunction(num, den)

def simulate_motor_step(load_disturbance=0.0, T=2, N=1000):
    # For load disturbance, model as torque disturbance affecting output speed
    system = motor_transfer_function()
    time = np.linspace(0, T, N)
    t, response = ctrl.step_response(system, T=time)

    # Simulate load disturbance by reducing output speed by disturbance factor
    disturbed_response = response - load_disturbance * np.ones_like(response)
    disturbed_response = np.clip(disturbed_response, 0, None)  

    return t, disturbed_response

def save_normalized_data():
    t, response = simulate_motor_step()
    norm = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    normalized_speed = norm(response)
    df = pd.DataFrame({'Time': t, 'Speed': response, 'Normalized Speed': normalized_speed})
    df.to_csv('dc_motor_data.csv', index=False)

if __name__ == "__main__":
    save_normalized_data()
