from math import exp
import random
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

### Alumna: Alexandra Ibarra

# x1: valor entrada 1
# w1: peso entrada 1
# x2: valor entrada 2
# w2: peso entrada 2
# bias: bias del sigmoid neuron
# thre: limite de comparacion para realizar decision de clases
# Se encarga de representar un sigmoid neuron

class Sigmoid:

    ## Se encarga de inicializar un sigmoid neuron
    def __init__(self,weight,bias):
        self.w = weight
        self.bias = bias
        self.error = 0
        self.delta = 0
        self.output = 0
        self.inp = []

    ## Se encarga de realizar el calculo del sigmoid neuron
    def sigmoid(self, inputs):
        v = 0
        for i in range(len(inputs)):
            v += inputs[i]*self.w[i]
        v += self.bias
        output = (1.0/(1+exp(v))) # ver si es -v o v
        self.output = output
        self.inp = inputs
        return output

    ## Funcion auxiliar encargada para calculo de la clase de los elementos
    def funAux(self, inputs):
        v = 0
        for i in range(len(inputs)):
            v += 2*inputs[i] - 3
        out = (1.0/v)**2
        return out

    def setWeight(self,rate):
        for i in range(len(self.w)):
            self.w[i] += rate*self.delta*self.inp[i]

    def setBias(self,rate):
        self.bias += rate*self.delta

    def setError(self):
        out = self.output
        real_out = self.funAux(self.inp)
        self.error = real_out - out

    def setErrorHidden(self, next, numWeight):
        error = 0.0
        for i in range(len(next)):
            error += (next[i].w[numWeight] * next[i].delta)
        self.error = error

    def setDelta(self):
        error = self.error
        out = self.output
        self.delta = error * out * (1.0 - out)