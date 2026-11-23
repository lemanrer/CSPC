"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]
# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
equivalence_index = np.argmax(slope)
equivalence_volume = V[equivalence_index]
print("Equivalence point volume =", equivalence_volume)
print("Maximum slope =", slope[equivalence_index])
# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(V, pH, marker="o", label="Titration curve")
axes[0].axvline(
    equivalence_volume,
    color="red",
    linestyle="--",
    label="Equivalence point"
)
axes[0].set_xlabel("Volume of base added")
axes[0].set_ylabel("pH")
axes[0].set_title("pH vs Volume")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(V, slope, marker="o", label="Slope")
axes[1].axvline(
    equivalence_volume,
    color="red",
    linestyle="--",
    label="Equivalence point"
)
axes[1].scatter(
    equivalence_volume,
    slope[equivalence_index],
    color="red",
    zorder=3
)
axes[1].set_xlabel("Volume of base added")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Slope vs Volume")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig("titration.png", dpi=300, bbox_inches="tight")
plt.show()