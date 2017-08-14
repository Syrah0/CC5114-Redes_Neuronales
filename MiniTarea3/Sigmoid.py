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
    def __init__(self,w1,w2,bias,thre):
        self.w1 = w1
        self.w2 = w2
        self.bias = bias
        self.thre = thre

    ## Se encarga de realizar el calculo del sigmoid neuron
    def sigmoid(self, x1, x2):
        v = x1 * self.w1 + x2 * self.w2 + self.bias
        output = (1.0/(1+exp(v)))
        if (output >= self.thre):
            return 0
        return 1

    ## Se encarga de simular la compuerta logica NAND
    def NAND(self, x1, x2):
        self.w1 = -2
        self.w2 = -2
        self.bias = 3
        self.thre = 0.5
        return self.sigmoid(x1, x2)

    ## Se encarga de simular la compuerta logica AND
    def AND(self, x1, x2):
        self.w1 = 1
        self.w2 = 1
        self.bias = -1.5
        self.thre = 0.5
        return self.sigmoid(x1, x2)

    ## Se encarga de simular la compuerta logica OR
    def OR(self, x1, x2):
        self.w1 = 1
        self.w2 = 1
        self.bias = -0.5
        self.thre = 0.5
        return self.sigmoid(x1, x2)

    ## Funcion auxiliar encargada para calculo de la clase de los elementos
    def funAux(self,x):
        return 2*x + 5

    ## Funcion encargada del proceso de entrenamiento del sigmoid neuron
    ## Esta recibe como parametro la cantidad de iteraciones que se desean realizar para entrenar
    def training(self,iter):
        C = 0.01
        goodArray = []  # contiene la cantidad de elementos buenas tras cada iteracion
        good = 0  # cantidad de clases correctamente acertadas
        for j in range(iter):
            x1 = random.randint(-30,30)
            y1 = random.randint(-30,30)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            predict = self.sigmoid(x1, y1)
            if(predict == 0 and output == 1):
                self.w1 = self.w1 + C * x1
                self.w2 = self.w2 + C * y1
            elif(predict == 1 and output == 0):
                self.w1 = self.w1 - C * x1
                self.w2 = self.w2 - C * y1
            else:
                good += 1
            goodArray.append(good)
        return goodArray

    ## Funcion encargada de predecir las clases de diferentes elementos usando un sigmoid
    ## neuron ya entrenado
    def prediction(self,iter):
        goodArray = []  # contiene la cantidad de elementos buenas tras cada iteracion
        good = 0  # cantidad de clases correctamente acertadas
        class0x = [] # valor de X perteneciente a la clase 0
        class0y = [] # valor de Y perteneciente a la clase 0
        class1x = [] # valor de X perteneciente a la clase 1
        class1y = [] # valor de Y perteneciente a la clase 1
        for j in range(iter):
            x1 = random.randint(-50,50)
            y1 = random.randint(-50,50)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            predict = self.sigmoid(x1,y1)
            if(predict == 0):
                class0x.append(x1)
                class0y.append(y1)
            else:
                class1x.append(x1)
                class1y.append(y1)
            if((predict == 0 and output == 0) or (predict == 1 and output == 1)):
                good += 1
            goodArray.append(good)
        return [goodArray,class0x,class0y,class1x,class1y]

    # Funcion encargada de testear el entrenamiento del sigmoid neuron
    # grafica el rendimiento del entrenamiento
    def testTraining(self):
        ### Entrenamiento ###
        iter = 1000
        good = self.training(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j] * 1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.title("Rendimiento del entrenamiento")
        plt.ylabel("Cantidad de puntos correctamente clasificados")
        plt.xlabel("N° iteraciones")
        plt.plot(x, good)
        plt.ylim([0.0, 1.05])
        plt.show()

    # Funcion encargada de testear el rendimiento del sigmoid neuron ya entrenado
    # grafica el rendimiento del sigmoid neuron con un nuevo conjunto (prueba)
    # grafica la distribucion de los nuevos puntos en el espacio
    def testPrediction(self):
        ### Testing con conjunto de prueba ###
        iter = 1000
        [good,c0x,c0y,c1x,c1y] = self.prediction(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.title("Rendimiento del entrenamiento fase de testing")
        plt.ylabel("Cantidad de puntos correctamente clasificados")
        plt.xlabel("N° iteraciones")
        plt.plot(x,good,'-')
        plt.ylim([0.0, 1.05])
        plt.figure()
        plt.plot(c0x, c0y, 'or')
        plt.plot(c1x, c1y, 'ob')
        plt.plot([-50,50], [self.funAux(-50),self.funAux(50)])
        plt.show()

###### TESTING #######

# crea sigmoid neuron para proceso de testeo
p = Sigmoid(-2.5, 1.5, -0.5, 0.5)
#p = Sigmoid(10,1,-2.5)
p.testTraining()
p.testPrediction()

## TEST PARA NAND
assert p.NAND(0, 0) == 1
assert p.NAND(0, 1) == 1
assert p.NAND(1, 0) == 1
assert p.NAND(1, 1) == 0

## TEST PARA AND
assert p.AND(0, 0) == 0
assert p.AND(0, 1) == 0
assert p.AND(1, 0) == 0
assert p.AND(1, 1) == 1

## TEST PARA OR
assert p.OR(0, 0) == 0
assert p.OR(0, 1) == 1
assert p.OR(1, 0) == 1
assert p.OR(1, 1) == 1
