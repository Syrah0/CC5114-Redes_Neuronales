from math import exp
import random
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from MiniTarea4.Sigmoid import *

### Alumna: Alexandra Ibarra

# x1: valor entrada 1
# w1: peso entrada 1
# x2: valor entrada 2
# w2: peso entrada 2
# bias: bias del sigmoid neuron
# thre: limite de comparacion para realizar decision de clases
# Se encarga de representar un sigmoid neuron

class Network:

    def __init__(self,hidden,outputs,inputs,neurons):
        self.hidden = hidden # cantidad de capas ocultas
        self.out = outputs # cantidad de output
        self.inputs = inputs # array con los valores de los inputs
        self.neuron = neurons # cantidad de neuronas en cada capa
        self.layers = []

    def feeding(self):
        ## creo la red -> capas ocultas
        for i in range(self.hidden):
            if i == 0:
                w = len(self.inputs)
            else:
                w = self.neuron[i-1]

            weigth = []
            for j in range(self.neuron[i]):
                for k in range(w):
                    weigth.append(1)
                p = Sigmoid(weigth,2) # arreglar!!!!!!!!!!!!!!!!!!!
                self.layers.append(p)

        ## creo capa output
        weigth = []
        for i in range(self.out):
            for k in range(self.neuron[self.hidden-1]):
                weigth.append(1)
            p = Sigmoid(weigth,2) # arreglar!!!!!!!!!!!!!!!!!
            self.layers.append(p)

        pos = 0
        for i in range(self.hidden+1):
            inp = []
            if i == 0: # primera capa
                inp = self.inputs
            else: # resto de capas ocultas
                for j in range(self.neuron[i-1]):
                    inp.append(self.layers[pos-(self.neuron[i-1])+j].output)

            if i == self.hidden: # ultima capa
                length = self.out
            else:
                length = self.neuron[i]

            for j in range(length):
                self.layers[pos+j].sigmoid(inp)

            if i != self.hidden:
                pos += self.neuron[i]

    #def backpropagation(self):

