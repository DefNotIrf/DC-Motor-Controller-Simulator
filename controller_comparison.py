import numpy as np
import pandas as pd
import control as ctrl
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from deap import base, creator, tools, algorithms


# PID
def run_pid(Kp=100, Ki=200, Kd=10, load_disturbance=0.0):
    R, L, J, b, Kt, Ke = 1.0, 0.5, 0.01, 0.1, 0.01, 0.01
    num = [Kt]
    den = [J * L, (J * R + L * b), (R * b + Kt * Ke)]
    plant = ctrl.TransferFunction(num, den)
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    system = ctrl.feedback(pid * plant, 1)
    t = np.linspace(0, 2, 1000)
    _, response = ctrl.step_response(system, T=t)
    response = np.clip(response - load_disturbance, 0, None)
    return t, response


# GA-PID
def pid_response(Kp, Ki, Kd):
    return run_pid(Kp, Ki, Kd)

def fitness(ind):
    _, y = pid_response(*ind)
    mse = np.mean((y - 1.0) ** 2)
    return (mse,)

def get_best_gains():
    if not hasattr(creator, "FitnessMin"):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", np.random.uniform, 0, 500)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 3)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", fitness)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=50, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=20)
    hof = tools.HallOfFame(1)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.3, ngen=20, halloffame=hof, verbose=False)
    return hof[0][0], hof[0][1], hof[0][2]


# Neuro Fuzzy
def run_neuro_fuzzy(load_disturbance=0.0):
    data = pd.read_csv("dc_motor_data.csv")  # Must exist in your folder
    actual_speed = data['Normalized Speed'].values - load_disturbance
    actual_speed = np.clip(actual_speed, 0, None)

    reference = 1.0
    error = reference - actual_speed
    delta_error = np.append([0], np.diff(error))

    X = np.column_stack((error, delta_error))
    y = actual_speed

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = MLPRegressor(hidden_layer_sizes=(10,), activation='tanh', max_iter=1000, random_state=42)
    model.fit(X_scaled, y)
    y_pred = model.predict(X_scaled)

    return y, y_pred


# Combine Outputs
def generate_output_table():
    t_pid, out_pid = run_pid()

    Kp_ga, Ki_ga, Kd_ga = get_best_gains()
    _, out_ga = run_pid(Kp_ga, Ki_ga, Kd_ga)

    actual_nf, _ = run_neuro_fuzzy()

    df = pd.DataFrame({
        "Time (s)": t_pid,
        "Setpoint": np.ones_like(t_pid),
        "PID Output": out_pid,
        "GA-Tuned PID Output": out_ga,
        "Neuro-Fuzzy Output": actual_nf[:len(t_pid)]  # match length
    })

    df.to_csv("controller_outputs.csv", index=False)
    print("Output saved to 'controller_outputs.csv'")
    return df

if __name__ == "__main__":
    df_outputs = generate_output_table()
    print(df_outputs.head(10))  # Show first 10 rows
