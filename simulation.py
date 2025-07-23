import numpy as np

class MovingObject:
    def __init__(self, x=0.0, y=0.0, vx=1.0, vy=0.5):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        return self.get_position()


    def get_position(self):
        return np.array([self.x, self.y])




