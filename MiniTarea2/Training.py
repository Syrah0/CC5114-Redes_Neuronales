import random
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

### Alumna: Alexandra Ibarra

# x1: valor entrada 1
# w1: peso entrada 1
# x2: valor entrada 2
# w2: peso entrada 2
# bias: bias del perceptron
# Se encarga de representar un perceptron


class Perceptron:

    ## Se encarga de inicializar un perceptron
    def __init__(self,w1,w2,bias):
        self.w1 = w1
        self.w2 = w2
        self.bias = bias

    ## Se encarga de realizar el calculo del perceptron
    def perceptron(self, x1, x2):
        v = x1 * self.w1 + x2 * self.w2
        if (v + self.bias <= 0):
            return 0
        return 1

    def funAux(self,x):
        return 2*x + 5

    def training(self,iter):
        C = 0.01
        goodArray = []
        badArray = []
        good = 0
        bad = 0
        for j in range(iter):
            x1 = random.randint(-30,30)
            y1 = random.randint(-30,30)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            predict = self.perceptron(x1,y1)
            if(predict == 0 and output == 1):
                bad += 1
                self.w1 = self.w1 - C * x1
                self.w2 = self.w2 - C * y1
            elif(predict == 1 and output == 0):
                bad += 1
                self.w1 = self.w1 + C * x1
                self.w2 = self.w2 + C * y1
            else:
                good += 1
            goodArray.append(good)
            badArray.append(bad)
        return [goodArray,badArray]
    ### RETORNAR ARRAYS Y CREAR FUNCION TEST QUE GRAFIQUE

    def prediction(self,iter):
        goodArray = []
        badArray = []
        good = 0
        bad = 0
        for j in range(iter):
            x1 = random.randint(-30,30)
            y1 = random.randint(-30,30)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            predict = self.perceptron(x1,y1)
            if(predict == 0 and output == 1):
                bad += 1
            elif(predict == 1 and output == 0):
                bad += 1
            else:
                good += 1
            goodArray.append(good)
            badArray.append(bad)
            print bad,good
        return [goodArray,badArray]

    def testTraining(self):
        ### Entrenamiento ###
        iter = 2000
        [good,bad] = self.training(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            bad[j] = (bad[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.plot(x,good)
        #plt.figure()
        #plt.plot(x,bad)
        plt.show()

    def testPrediction(self):
        ### Entrenamiento ###
        iter = 2000/4
        [good,bad] = self.prediction(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            bad[j] = (bad[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.plot(x,good)
        #plt.figure()
        #plt.plot(x,bad)
        plt.show()

p = Perceptron(1.5,0.2,-0.5)
p.testTraining()
p.testPrediction()

