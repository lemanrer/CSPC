# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW1/Lab A/.
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