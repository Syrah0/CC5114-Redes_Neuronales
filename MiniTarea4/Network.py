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

            for j in range(self.neuron[i]):
                weigth = []
                for k in range(w):
                    weigth.append(1)
                p = Sigmoid(weigth,2) # arreglar!!!!!!!!!!!!!!!!!!!
                self.layers.append(p)

        ## en este punto -> len(layers) = sum(self.neuron) => i_out = sum(self.neuron)
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

    def backpropagation(self):
        # error y delta output capa
        pos_out = 0
        for i in range(self.hidden):
            pos_out += self.neuron[i]

        for i in range(pos_out,self.out + pos_out):
            self.layers[i].setError()
            self.layers[i].setDelta()

        # error y delta otras capas
        for i in range(self.hidden):
            numNeuron = self.neuron[self.hidden - i - 1]
            nextLayer = []

            pos = 0
            for j in range(self.hidden - i - 1):
                pos += self.neuron[j]

            if i == 0:
                endNextLayer = self.out
            else:
                endNextLayer = self.neuron[self.hidden - i]

            for j in range(pos + numNeuron, pos + numNeuron + endNextLayer):
                nextLayer.append(self.layers[j])

            for j in range(pos, pos + numNeuron):
                self.layers[j].setErrorHidden(nextLayer, j - pos)
                self.layers[j].setDelta()

    def updateWeightAndBias(self, rate):
        for i in range(len(self.layers)):
            self.layers[i].setWeight(rate)
            self.layers[i].setBias(rate)

    def neuralNetwoks(self,rate):
        self.feeding()
        self.backpropagation()
        self.updateWeightAndBias(rate)

