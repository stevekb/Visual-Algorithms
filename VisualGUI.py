import numpy as np
import random as rand


class VisualGUI:

    array = np.zeros(20)

    def __init__(self):

        for i in range(len(self.array)):
            self.array[i] = rand.randint(0, 32)

    def get_array(self):
        return self.array
