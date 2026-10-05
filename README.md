# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW1/Lab A/Lab B.
## Setup
Create the environment for a given lab:
```bash
conda env create -f PW1/Lab\ A/environment.yml
conda activate cspc
```
---
## PW1 - Lab A: Reproducible Foundations

## **What I built:**
- Implemented a radioactive decay simulation using both a pure-Python loop and a vectorised NumPy implementation.
- Added pytest tests to check the initial value, reject negative decay rates, and verify that the simulation approximately follows the expected exponential decay law.
## **Speed comparison (loop vs NumPy):**
- pure python : 2.7334 s
- numpy : 0.0003 s
- speed-up: numpy is 9442.96 times faster
## **Tests:** 
All passing? : Yes
## **Conclusion:**
- I implemented and tested a radioactive decay simulation using Python and NumPy.
- The tests verify both input validation and the physical behaviour of the simulation.
- The performance comparison shows that the vectorised NumPy implementation is much faster than looping over individual atoms for large simulations.
- I pushed my CSPC repository online, connected my local CSPC repository to the GitHub repository.

---
## PW1 - Lab B: Data, Plotting, and Automation

## **What I built:**
- Plotted the observed radioactive decay data from `decay_observed.csv` alongside the analytical decay law ($N_0 e^{-\lambda t}$) using a $1 \times 2$ subplot with shared axes[cite: 1].
- Created a Snakemake workflow (`Snakefile`) to automate the generation of `figure.png` from the input dataset and script.

## **Data observation & comparison:**
- **Observed data:** Shows a radioactive decay process where particle counts decrease over time.
- **Comparison:** The observed scatter points match the smooth theoretical analytical curve closely on the same scale.

## **Snakemake pipeline:**
- The pipeline automates figure building and uses file timestamps to only rerun the script when input files or scripts change.
- Re-running when nothing changed reports `Nothing to be done`.

## **Conclusion:**
- I read observation data and successfully verified that the empirical data follows the analytical decay law ($N(t) = N_0 e^{-\lambda t}$).
- I automated the plotting process using Snakemake, ensuring reproducible and dependency-aware data visualisation.
- I updated the repository structure, verified the pipeline execution, and committed all required files to GitHub.
---
## PW2 - Lab A: Motion from Tracking Data

## **What I built:**
- Loaded time and position data from `freefall.csv`.
- Calculated velocity and acceleration using `np.gradient()`.
- Calculated the mean acceleration and compared it with the theoretical value of `-9.81 m/s²`.
- Integrated acceleration to recover velocity using `cumulative_trapezoid()`.
- Created a figure with position, velocity, and acceleration plotted against time.

## **Data observation & comparison:**
- The calculated acceleration is close to the theoretical gravitational acceleration of -9.81 m/s².
- However, the acceleration data is not perfectly constant. It shows some fluctuations because the velocity and acceleration are calculated numerically from the measured position data. Taking derivatives can make small measurement errors more noticeable.
- The recovered velocity and position can also be compared with the original measured data. The recovered values follow the general behavior of the original motion, showing that numerical differentiation and integration can be used to analyze the free-fall data.
- The acceleration plot also includes a horizontal line at -9.81 m/s², which makes it easier to visually compare the calculated acceleration with the theoretical value.

## **Conclusion:**
- I learned how numerical methods can be used to analyze experimental motion data.
- By taking numerical derivatives, I obtained velocity and acceleration from position data. Then, by numerical integration, I recovered velocity and position from acceleration.