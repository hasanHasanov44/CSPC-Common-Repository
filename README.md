# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
## PW1 Lab B - Data, Plotting, and Automation
- **Data Observation:** The dataset demonstrates exponential radioactive decay over time.
- **Comparison:** The observed experimental data closely matches the theoretical analytical decay curve.
- **Automation:** The Snakemake pipeline automates figure generation, rebuilding `figure.png` only when source data or scripts change.

## PW2 Lab A - Motion from Tracking Data

- **Mean Acceleration:** -9.81 m/s²
- **Noise Observation:** Differentiation compares adjacent noisy measurements, which greatly amplifies high-frequency noise (as seen in the wildly oscillating acceleration plot). In contrast, integration sums up values, which causes random noise to cancel out and suppresses it.
- **Integration Back Result:** Reconstructing position by integrating the noisy acceleration restored the original smooth trajectory within about 1 meter of accuracy.

### Bonus: 2D Tracked Trajectory
- Calculated the 2D path (x vs y) and speed sqrt(vx^2 + vy^2) over time using `np.gradient` on each coordinate.
- Saved the output visualization as `trajectory.png`.

# PW2 Lab B - Chemical Computing Report

## Part 2B Observations
- **Gradient Descent & SLSQP:** Both methods converge to a local minimum depending on the starting point $x_0$.
- **Newton's Method:** Solves $g'(x) = 0$, finding stationary points. From $x_0 = 0$, it finds a local **maximum** ($d^2g < 0$). From $x_0 = 2$, it finds a local **minimum** ($d^2g > 0$).
- **Starting Point Effect:** The choice of $x_0$ dictates which local extremum or stationary point the algorithm reaches.

## Key Numerical Results
- **Titration Equivalence Point:** 50.0 mL
- **Fitted Rate Constant (Kinetics k):** 0.2618
- **Equilibrium Extent (x):** 0.6638
- **Equilibrium Amounts:** H2 = 0.3362 mol, I2 = 0.3362 mol, HI = 1.3277 mols