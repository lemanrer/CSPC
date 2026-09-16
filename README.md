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
- Created a Snakemake workflow (`Snakefile`) to automate the generation of `figure.png` from the input dataset and script[cite: 1].

## **Data observation & comparison:**
- **Observed data:** Shows a radioactive decay process where particle counts decrease over time[cite: 1].
- **Comparison:** The observed scatter points match the smooth theoretical analytical curve closely on the same scale[cite: 1].

## **Snakemake pipeline:**
- The pipeline automates figure building and uses file timestamps to only rerun the script when input files or scripts change[cite: 1].
- Re-running when nothing changed reports `Nothing to be done`[cite: 1].

## **Conclusion:**
- I read observation data and successfully verified that the empirical data follows the analytical decay law ($N(t) = N_0 e^{-\lambda t}$)[cite: 1].
- I automated the plotting process using Snakemake, ensuring reproducible and dependency-aware data visualisation[cite: 1].
- I updated the repository structure, verified the pipeline execution, and committed all required files to GitHub[cite: 1].