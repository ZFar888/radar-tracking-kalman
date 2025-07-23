import numpy as np

class Radar:
    def __init__(self,noise_std = 1.0): #the standard deviation of the nosie
        self.noise_std = noise_std

    def get_noisy_position(self, true_position):
        noise = np.random.normal(loc=0, scale = self.noise_std, size = 2)
        noisy_position = true_position + noise
        return noisy_position
