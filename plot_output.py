import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("controller_outputs.csv")

# Plotoutputs
plt.figure(figsize=(10, 6))
plt.plot(df["Time (s)"], df["Setpoint"], 'k--', label="Setpoint")
plt.plot(df["Time (s)"], df["PID Output"], label="PID Output")
plt.plot(df["Time (s)"], df["GA-Tuned PID Output"], label="GA-Tuned PID Output")
plt.plot(df["Time (s)"], df["Neuro-Fuzzy Output"], label="Neuro-Fuzzy Output")

# Plot style
plt.title("Controller Output Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Speed (rad/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
