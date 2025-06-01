# DC-Motor-Controller-Simulator
This project demonstrates the design and comparison of intelligent controllers for a DC motor system. It integrates Fuzzy Logic, Neuro-Fuzzy models, and PID control to simulate and optimise motor speed under load disturbances. It also features a full GUI interface for experimentation and performance analysis.

---

## 📌 Objectives

- Simulate a DC motor system using classical and intelligent control strategies
- Evaluate controller performance (MSE, tracking behaviour)
- Provide GUI-based simulation tools
- Apply Genetic Algorithm (GA) to auto-tune PID gains
- Use real step response data for fuzzy/neuro models

---

## 🧠 Computational Intelligence Features

| Technique          | Description |
|--------------------|-------------|
| **Fuzzy Logic**    | Rule-based inference using linguistic variables and membership functions |
| **Neuro-Fuzzy**    | Combines fuzzy logic input structure with machine learning (MLP regressor) |
| **GA-PID Tuning**  | Genetic Algorithm optimisation of PID gains using DEAP |
| **PID Controller** | Classical control technique for reference tracking |

---

## 🗂 File Descriptions

| File | Description |
|------|-------------|
| `motor_model.py` | Simulates DC motor model and exports `dc_motor_data.csv` |
| `pid_control.py` | Manual PID controller simulation |
| `fuzzy_control.py` | Fuzzy logic controller with rule base |
| `neuro_fuzzy_controller.py` | Neuro-Fuzzy model using MLPRegressor |
| `ga_pid_tuning.py` | Genetic Algorithm optimiser for PID tuning |
| `performance_metrics.py` | Evaluates performance metrics (MSE, etc.) |
| `gui_simulation.py` | GUI application for running simulations |
| `dc_motor_data.csv` | Motor response data used for learning/simulation (Run 'motor_model.py' to get this .csv file) |
| `README.md` | Project instructions and overview |

---

## ✅ Requirements

Install all dependencies with:

```bash
pip install numpy matplotlib control pandas scikit-learn scikit-fuzzy deap

Developed by Group 6 (Irfan, Ikhwan, Isma & Akmal) part of a Computational Intelligence (MCTA 3371) Mini Project. Demonstrates how hybrid computational intelligence techniques can improve classical control methods through learning, adaptability, and evolution.
