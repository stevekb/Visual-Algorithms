# neural net class which just contains data and can calculate option with inputs
import numpy as np


class NeuralNet:

    def __init__(self, shape):
        self.shape = shape
        self.w_shapes = list(zip(shape[1:], shape[:-1]))
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in self.w_shapes]
        self.bias = [np.zeros((s, 1)) for s in shape[1:]]

    def getweights(self):
        return self.weights

    def getshape(self):
        return self.shape

    def getbias(self):
        return self.bias

    def randomize(self):
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in self.w_shapes]
        self.bias = [np.zeros((s, 1)) for s in self.shape[1:]]

    def predict(self, a):
        if len(a) != self.shape[0]:
            raise Exception('predict input not correct size')
        a = np.transpose([a])
        for w, b in zip(self.weights, self.bias):
            a = self.activationReLU(np.matmul(w, a) + b)
        return a


    @staticmethod
    def activation(x):
        return 1/(1 + np.exp(-x))


    @staticmethod
    def activationReLU(x):
        return np.maximum(x, np.zeros(x.shape))
