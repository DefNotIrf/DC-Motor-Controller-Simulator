# DC Motor Controller Simulator

This project implements and compares various control strategies for a DC motor system, including classical PID, Fuzzy Logic, and Neuro-Fuzzy controllers. It provides a graphical user interface (GUI) to simulate and analyse the controllers’ performance under different load disturbances. Additionally, it includes a Genetic Algorithm (GA) to automatically tune PID controller gains.

---

## Project Objectives

- Simulate a DC motor system using different control approaches  
- Compare controller performance based on metrics such as Mean Squared Error (MSE), rise time, overshoot, and settling time  
- Provide an interactive GUI for easy experimentation and visualisation  
- Implement a GA-based PID tuning method to optimise controller parameters  
- Use real motor response data to train fuzzy and neuro-fuzzy models
- Extracted and saved original model output vs input data for performance comparison
- Plotted all controller responses (PID, GA-PID, Neuro-Fuzzy) for visual analysis

---

## Features

Controller Type     | Description
--------------------|------------------------------------------------------------
PID Controller      | Classical proportional–integral–derivative control
Fuzzy Logic         | Rule-based inference with linguistic variables and membership functions
Neuro-Fuzzy         | Hybrid model combining fuzzy logic with machine learning (MLP regressor)
GA Tuning for PID   | Genetic Algorithm optimisation of PID gains

---

## File Overview

Filename                | Description
------------------------|---------------------------------------------------------
motor_model.py          | Simulates the DC motor and generates the data file dc_motor_data.csv
controller_comparison.py| Run all controller and produce outputs data controller_outputs.csv
pid_control.py          | PID controller simulation code
fuzzy_control.py        | Fuzzy logic controller implementation
neuro_fuzzy_control.py  | Neuro-fuzzy controller using MLPRegressor for learning
ga_pid_tuning.py        | Genetic Algorithm to tune PID controller gains
performance_metrics.py  | Calculates key performance metrics such as MSE, overshoot, rise time, settling time
gui_simulation.py       | Main GUI application for running simulations and displaying results
plot_output.py          | Optional script to visualise outputs from controller_outputs.csv
dc_motor_data.csv       | Recorded motor speed response data (run 'motor_model.py' to get this file)
controller_outputs.csv  | Stores step response output of all controllers (PID, GA-PID, Neuro-Fuzzy)

---

## Getting Started!

### Prerequisites:
Make sure you have Python 3.x installed. Install the required Python packages using pip:
``` 
pip install numpy matplotlib control pandas scikit-learn scikit-fuzzy deap
```

### Produce DC Motor Data:
You must run 'motor_model.py' first to obtain the .csv file before launching the GUI simulation

### Produce Controller Outputs:
You must run 'controller_comparison.py'  to obtain the .csv file before plotting the outputs

### Running the GUI:
Launch the GUI simulation by running:
```
python gui_simulation.py
```

#### Visualising the Outputs:
Plot the response of the controller  by running:
```
python plot_output.py
```
---

## Usage

- Select the desired controller type (PID, Fuzzy Logic, or Neuro-Fuzzy)
- Adjust PID parameters or disturbance load as needed
- Click Run Simulation to see the motor speed response and performance metrics
- Optionally, use GA Tune PID Gains to automatically find optimal PID parameters
- Use the exported 'controller_outputs.csv' for documenting and comparing controller responses
- Run 'plot_outputs.py' to visualise all controller outputs against the setpoint

---

## Performance Evaluation

The simulator calculates and displays the following metrics to evaluate controller performance:

- Mean Squared Error (MSE) between the motor speed and the setpoint
- Overshoot — how much the response exceeds the setpoint
- Rise Time — time taken for the response to reach 90% of the setpoint
- Settling Time — time taken for the response to stay within a tolerance band around the setpoint

Outside of the simulator, we can also plot the respective outputs against the setpoint, which the default are step response

---

## Contributors

Developed by Group 6: Irfan, Ikhwan, Isma & Akmal as part of the Computational Intelligence (MCTA 3371) Mini Project, Semester 2 24/25. 
