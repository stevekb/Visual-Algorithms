# neural net class which just contains data and can calculate option with inputs
import numpy as np


class NN:

    def __init__(self, inputs, hidden, outputs):
        self.inputweights = 2 * np.random.random((inputs, hidden[0])) - 1
        self.hiddenweights = 2 * np.random.random((hidden[0], hidden[0], hidden[1])) - 1
        self.outputweights = 2 * np.random.random((hidden[0], outputs)) - 1
        self.hiddenbias = 2 * np.random.random((hidden[0], hidden[1])) - 1
        self.outputbi

    def getinputw(self):
        return self.inputweights

    def gethiddenw(self):
        return self.hiddenweights

    def getoutputw(self):
        return self.outputweights

    def randomize(self):
        self.inputweights = 2 * np.random.random(self.inputweights.shape) - 1
        self.hiddenweights = 2 * np.random.random(self.hiddenweights.shape) - 1
        self.outputweights = 2 * np.random.random(self.outputweights.shape) - 1
