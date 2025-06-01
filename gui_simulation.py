import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import motor_model
import pid_control
import neuro_fuzzy_control
import fuzzy_control
import performance_metrics
import ga_pid_tuning

class MotorControlApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DC Motor Controller Simulator")

        # Variables
        self.controller_var = tk.StringVar(value="PID")
        self.load_disturbance_var = tk.DoubleVar(value=0.0)

        # PID params
        self.Kp_var = tk.DoubleVar(value=100)
        self.Ki_var = tk.DoubleVar(value=200)
        self.Kd_var = tk.DoubleVar(value=10)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10)

        ttk.Label(frame, text="Select Controller").grid(row=0, column=0)
        controller_menu = ttk.Combobox(frame, textvariable=self.controller_var,
                                       values=["PID", "Neuro-Fuzzy", "Fuzzy Logic"])
        controller_menu.grid(row=0, column=1)

        ttk.Label(frame, text="Kp").grid(row=1, column=0)
        ttk.Entry(frame, textvariable=self.Kp_var).grid(row=1, column=1)
        ttk.Label(frame, text="Ki").grid(row=2, column=0)
        ttk.Entry(frame, textvariable=self.Ki_var).grid(row=2, column=1)
        ttk.Label(frame, text="Kd").grid(row=3, column=0)
        ttk.Entry(frame, textvariable=self.Kd_var).grid(row=3, column=1)

        ttk.Label(frame, text="Load Disturbance").grid(row=4, column=0)
        ttk.Entry(frame, textvariable=self.load_disturbance_var).grid(row=4, column=1)

        ttk.Button(frame, text="Run Simulation", command=self.run_simulation).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="GA Tune PID Gains", command=self.run_ga_tune).grid(row=6, column=0, columnspan=2, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

        self.metrics_text = tk.Text(self, height=7, width=70)
        self.metrics_text.pack()

    def run_simulation(self):
        controller = self.controller_var.get()
        ld = self.load_disturbance_var.get()

        self.ax.clear()
        mse = None

        try:
            if controller == "PID":
                t, response = pid_control.run_pid(self.Kp_var.get(), self.Ki_var.get(), self.Kd_var.get(), ld)
                mse = ((response - 1.0) ** 2).mean()
                overshoot, rise_time, settling_time = performance_metrics.calculate_performance_metrics(t, response)
                self.ax.plot(t, response, label="PID Output")

            elif controller == "Neuro-Fuzzy":
                actual, predicted, mse = neuro_fuzzy_control.run_neuro_fuzzy(ld)
                t = range(len(actual))
                overshoot, rise_time, settling_time = performance_metrics.calculate_performance_metrics(t, actual)
                self.ax.plot(t, actual, label="Actual Speed")
                self.ax.plot(t, predicted, '--', label="Neuro-Fuzzy Output")

            elif controller == "Fuzzy Logic":
                t, response = fuzzy_control.run_fuzzy(ld)
                mse = ((response - 1.0) ** 2).mean()
                overshoot, rise_time, settling_time = performance_metrics.calculate_performance_metrics(t, response)
                self.ax.plot(t, response, label="Fuzzy Logic Output")

            else:
                messagebox.showerror("Error", "Unknown controller selected!")
                return

            self.ax.set_title(f"{controller} Controller Response")
            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Speed (rad/s)")
            self.ax.legend()
            self.ax.grid(True)
            self.canvas.draw()

            # Show performance metrics safely
            self.metrics_text.delete(1.0, tk.END)
            self.metrics_text.insert(tk.END, f"MSE: {mse:.6f}\n")
            self.metrics_text.insert(tk.END, f"Overshoot: {overshoot:.2f}%\n")

            if rise_time == -1:
                rise_time_str = "N/A"
            else:
                rise_time_str = f"{rise_time:.4f} s"

            self.metrics_text.insert(tk.END, f"Rise Time: {rise_time_str}\n")
            self.metrics_text.insert(tk.END, f"Settling Time: {settling_time:.4f} s\n")

        except Exception as e:
            messagebox.showerror("Simulation Error", str(e))

    def run_ga_tune(self):
        try:
            best_params = ga_pid_tuning.run_ga()
            self.Kp_var.set(best_params[0])
            self.Ki_var.set(best_params[1])
            self.Kd_var.set(best_params[2])
            messagebox.showinfo("GA Tuning", f"Best PID gains found:\nKp={best_params[0]:.2f}, Ki={best_params[1]:.2f}, Kd={best_params[2]:.2f}")
        except Exception as e:
            messagebox.showerror("GA Tuning Error", str(e))


if __name__ == "__main__":
    app = MotorControlApp()
    app.mainloop()
