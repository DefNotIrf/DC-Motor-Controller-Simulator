import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd

def run_fuzzy(load_disturbance=0.0):
    # Define fuzzy variables
    error = ctrl.Antecedent(np.arange(-1, 1.01, 0.01), 'error')
    delta_error = ctrl.Antecedent(np.arange(-1, 1.01, 0.01), 'delta_error')
    output = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'output')

    # Membership functions
    error['neg'] = fuzz.trimf(error.universe, [-1, -1, 0])
    error['zero'] = fuzz.trimf(error.universe, [-0.1, 0, 0.1])
    error['pos'] = fuzz.trimf(error.universe, [0, 1, 1])

    delta_error['neg'] = fuzz.trimf(delta_error.universe, [-1, -1, 0])
    delta_error['zero'] = fuzz.trimf(delta_error.universe, [-0.1, 0, 0.1])
    delta_error['pos'] = fuzz.trimf(delta_error.universe, [0, 1, 1])

    output['low'] = fuzz.trimf(output.universe, [0, 0, 0.5])
    output['medium'] = fuzz.trimf(output.universe, [0, 0.5, 1])
    output['high'] = fuzz.trimf(output.universe, [0.5, 1, 1])

    # Rules
    rules = [
        ctrl.Rule(error['pos'] & delta_error['pos'], output['high']),
        ctrl.Rule(error['pos'] & delta_error['zero'], output['high']),
        ctrl.Rule(error['pos'] & delta_error['neg'], output['medium']),
        ctrl.Rule(error['zero'] & delta_error['pos'], output['medium']),
        ctrl.Rule(error['zero'] & delta_error['zero'], output['medium']),
        ctrl.Rule(error['zero'] & delta_error['neg'], output['low']),
        ctrl.Rule(error['neg'] & delta_error['pos'], output['low']),
        ctrl.Rule(error['neg'] & delta_error['zero'], output['low']),
        ctrl.Rule(error['neg'] & delta_error['neg'], output['low']),
    ]

    control_system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(control_system)

    # Load motor data
    data = pd.read_csv("dc_motor_data.csv")
    ref_speed = 1.0
    actual_speed = data['Normalized Speed'].values - load_disturbance
    actual_speed = np.clip(actual_speed, 0, None)

    # Calculate error and delta error
    error_values = ref_speed - actual_speed
    delta_error_values = np.append([0], np.diff(error_values))

    output_values = []
    for e, de in zip(error_values, delta_error_values):
        sim.input['error'] = e
        sim.input['delta_error'] = de
        sim.compute()
        output_values.append(sim.output['output'])

    time = np.linspace(0, 2, len(output_values))

    return time, np.array(output_values)
