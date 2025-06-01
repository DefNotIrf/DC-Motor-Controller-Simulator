import numpy as np

def calculate_performance_metrics(time, response, setpoint=1.0):
    overshoot = (np.max(response) - setpoint) / setpoint * 100
    
    rise_time = None
    try:
        rise_time = time[next(i for i, v in enumerate(response) if v >= 0.9 * setpoint)]
    except StopIteration:
        rise_time = None

    settling_time = None
    for i in range(len(response) - 1, -1, -1):
        if abs(response[i] - setpoint) > 0.02 * setpoint:
            settling_time = time[i]
            break
    if settling_time is None:
        settling_time = time[-1]

    if rise_time is None:
        rise_time = -1  # flag for missing rise time

    return overshoot, rise_time, settling_time
