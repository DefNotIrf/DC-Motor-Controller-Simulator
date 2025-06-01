DC Motor Controller Simulator

This project implements and compares various control strategies for a DC motor system, including classical PID, Fuzzy Logic, and Neuro-Fuzzy controllers. It provides a graphical user interface (GUI) to simulate and analyse the controllers’ performance under different load disturbances. Additionally, it includes a Genetic Algorithm (GA) to automatically tune PID controller gains.

---

Project Objectives

- Simulate a DC motor system using different control approaches  
- Compare controller performance based on metrics such as Mean Squared Error (MSE), rise time, overshoot, and settling time  
- Provide an interactive GUI for easy experimentation and visualisation  
- Implement a GA-based PID tuning method to optimise controller parameters  
- Use real motor response data to train fuzzy and neuro-fuzzy models  

---

Features

Controller Type     | Description
--------------------|------------------------------------------------------------
PID Controller      | Classical proportional–integral–derivative control
Fuzzy Logic         | Rule-based inference with linguistic variables and membership functions
Neuro-Fuzzy         | Hybrid model combining fuzzy logic with machine learning (MLP regressor)
GA Tuning           | Genetic Algorithm optimisation of PID gains

---

File Overview

Filename                | Description
------------------------|---------------------------------------------------------
motor_model.py          | Simulates the DC motor and generates the data file dc_motor_data.csv
pid_control.py          | PID controller simulation code
fuzzy_control.py        | Fuzzy logic controller implementation
neuro_fuzzy_control.py  | Neuro-fuzzy controller using MLPRegressor for learning
ga_pid_tuning.py        | Genetic Algorithm to tune PID controller gains
performance_metrics.py  | Calculates key performance metrics such as MSE, overshoot, rise time, settling time
gui_simulation.py       | Main GUI application for running simulations and displaying results
dc_motor_data.csv       | Recorded motor speed response data

---

Getting Started

Prerequisites

Make sure you have Python 3.x installed. Install the required Python packages using pip:

pip install numpy matplotlib control pandas scikit-learn scikit-fuzzy deap

Running the GUI

Launch the GUI simulation by running:

python gui_simulation.py

---

Usage

- Select the desired controller type (PID, Fuzzy Logic, or Neuro-Fuzzy)
- Adjust PID parameters or disturbance load as needed
- Click Run Simulation to see the motor speed response and performance metrics
- Optionally, use GA Tune PID Gains to automatically find optimal PID parameters

---

Performance Evaluation

The simulator calculates and displays the following metrics to evaluate controller performance:

- Mean Squared Error (MSE) between the motor speed and the setpoint
- Overshoot — how much the response exceeds the setpoint
- Rise Time — time taken for the response to reach 90% of the setpoint
- Settling Time — time taken for the response to stay within a tolerance band around the setpoint

---

Contributors

Developed by Group 6: Irfan, Ikhwan, Isma & Akmal as part of the Computational Intelligence (MCTA 3371) Mini Project.
