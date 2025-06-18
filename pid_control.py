import numpy as np
import control as ctrl

def run_pid(Kp=100, Ki=200, Kd=10, load_disturbance=0.0):
    # DC Motor params
    R, L, J, b, Kt, Ke = 1.0, 0.5, 0.01, 0.1, 0.01, 0.01
    num = [Kt]
    den = [J*L, (J*R + L*b), (R*b + Kt*Ke)]
    plant = ctrl.TransferFunction(num, den)

    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    system = ctrl.feedback(pid * plant, 1)

    time = np.linspace(0, 2, 1000)
    t, response = ctrl.step_response(system, T=time)

    # Simulate disturbance effect
    disturbed_response = response - load_disturbance
    disturbed_response = np.clip(disturbed_response, 0, None)

    return t, disturbed_response
