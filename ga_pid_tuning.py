import numpy as np
import control as ctrl
from deap import base, creator, tools, algorithms

# GA uses DEAP library (pip install deap)
# Fitness: minimize MSE between step response and reference speed

R, L, J, b, Kt, Ke = 1.0, 0.5, 0.01, 0.1, 0.01, 0.01

def pid_response(Kp, Ki, Kd):
    num = [Kt]
    den = [J*L, (J*R + L*b), (R*b + Kt*Ke)]
    plant = ctrl.TransferFunction(num, den)
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    system = ctrl.feedback(pid * plant, 1)
    time = np.linspace(0, 2, 1000)
    t, response = ctrl.step_response(system, T=time)
    return t, response

def fitness(individual):
    Kp, Ki, Kd = individual
    _, response = pid_response(Kp, Ki, Kd)
    ref = 1.0
    mse = np.mean((response - ref) ** 2)
    return (mse,)

def run_ga():
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
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
    best = hof[0]
    print(f"Best PID gains found: Kp={best[0]:.2f}, Ki={best[1]:.2f}, Kd={best[2]:.2f}")
    return best
