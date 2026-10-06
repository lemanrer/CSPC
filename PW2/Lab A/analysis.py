"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)
print("t is: ", t)
print("y is: ", y)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print("Here I am")

print("Mean acceleration:", np.mean(a))
print("Is it close to -9.81?", np.isclose(np.mean(a), -9.81, atol=0.5)) #atol is absolute tolerance
print("Acceleration is noisy:", np.std(a)) #standard deviation

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.pngx
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

# Position
axes[0].plot(t, y, label="Measured position")
axes[0].plot(t, y_recovered, "--", label="Recovered position")
axes[0].set_ylabel("Position y")
axes[0].set_title("Position vs Time")
axes[0].legend()
axes[0].grid()

# Velocity
axes[1].plot(t, v, label="Calculated velocity")
axes[1].plot(t, v_recovered, "--", label="Recovered velocity")
axes[1].set_ylabel("Velocity v")
axes[1].set_title("Velocity vs Time")
axes[1].legend()
axes[1].grid()

# Acceleration
axes[2].plot(t, a, label="Calculated acceleration")
axes[2].axhline(-9.81, linestyle="--", label="True acceleration = -9.81")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration a")
axes[2].set_title("Acceleration vs Time")
axes[2].legend()
axes[2].grid()

plt.tight_layout()

# Save figure
plt.savefig("motion.png")

plt.show()