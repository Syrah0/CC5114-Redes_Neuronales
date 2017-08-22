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

    ## Se encarga de realizar el calculo del sigmoid neuron
    def sigmoid(self, inputs):
        v = 0
        for i in range(len(inputs)):
            v += inputs[i]*self.w[i]
        v += self.bias
        output = (1.0/(1+exp(v))) # ver si es -v o v
        self.output = output
        return output

    ## Funcion auxiliar encargada para calculo de la clase de los elementos
    def funAux(self,x):
        return 2*x + 5

    ## Funcion encargada del proceso de entrenamiento del sigmoid neuron
    ## Esta recibe como parametro la cantidad de iteraciones que se desean realizar para entrenar
    def setWeight(self,rate,inputs):
        for i in range(len(self.w)):
            self.w[i] += rate*self.delta*inputs[i]

    def setBias(self,rate):
        self.bias += rate*self.delta