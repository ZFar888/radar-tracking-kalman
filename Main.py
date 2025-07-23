import numpy as np
import matplotlib.pyplot as plt
from simulation import MovingObject
from radar import Radar
from kalmen import KalmanFilter2D

# Set up simulation
dt = 0.2
obj = MovingObject()
radar = Radar(noise_std=2.0)
kf = KalmanFilter2D()

# Live plot setup
plt.ion()
fig, ax = plt.subplots()

for _ in range(1000):
    true_pos = obj.update(dt)
    radar_pos = radar.get_noisy_position(true_pos)

    # Kalman filter steps
    kf.predict()
    kf.update(radar_pos)
    estimate = kf.get_position()

    # Plotting
    ax.clear()

    # True position - blue
    ax.scatter(true_pos[0], true_pos[1], color="blue", label="True Position", s=50)

    # Noisy radar - red
    ax.scatter(radar_pos[0], radar_pos[1], color="red", label="Radar Reading", s=30)

    # Kalman estimate - green
    ax.scatter(estimate[0], estimate[1], color="green", label="Kalman Estimate", s=40)

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 30)
    ax.set_title("Live Radar Tracking with Kalman Filter")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.legend()
    ax.grid(True)

    plt.pause(dt)

plt.ioff()
plt.show()
