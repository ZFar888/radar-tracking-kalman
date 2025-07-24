# radar-tracking-kalman

A real-time Python simulation of a 2D object tracked using noisy radar measurements and a Kalman Filter for state estimation. This project demonstrates how noisy sensor data can be filtered to accurately track an object’s true motion using basic estimation techniques and linear algebra.

## Features

- Real-time simulation of a 2D moving object with constant velocity
- Simulated radar sensor with configurable Gaussian noise
- Kalman Filter for smoothing and estimating position and velocity
- Visual representation using Pygame:
  - **Red dot** – True object position
  - **Blue dot** – Noisy radar measurement
  - **Green dot** – Kalman Filter estimate

## Tech Stack

- **Python 3.x** – Primary programming language
- **NumPy** – Matrix operations and linear algebra
- **Pygame** – Real-time 2D graphics rendering
- **Matplotlib** *(optional)* – Offline data plotting/debugging
- **Modular Codebase**:
  - `simulation.py` – Defines object motion
  - `radar.py` – Simulates noisy radar input
  - `kalman.py` – 2D Kalman Filter logic

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ZFar888/radar-tracking-kalman.git
   cd radar-tracking-kalman


## Usage

To start the simulation, run:
```bash
python Main.py