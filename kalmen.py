import numpy as np

class KalmanFilter2D:
    def __init__(self):
        self.x = np.zeros((4,1))

        self.dt = 0.2


        self.F = np.array([
            [1,0,self.dt,0],
            [0,1,0,self.dt],
            [0,0,1,0],
            [0,0,0,1]
        ])

        self.H = np.array([
            [1,0,0,0],
            [0,1,0,0]
        ])


        self.R = np.eye(2) * 4.0


        self.P = np.eye(4) * 1000.0


        self.Q = np.eye(4) * 0.1


    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q


    def update(self, z):
        z = z.reshape((2,1))
        y = z - self.H @ self.x
        S = self.H @self.P @self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y
        self.P = (np.eye(4) - K @ self.H) @ self.P

    def get_position(self):
        return self.x[0:2].flatten()