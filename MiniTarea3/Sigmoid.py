from math import exp
import random
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

class Sigmoid:
    def __init__(self,w1,w2,bias):
        self.w1 = w1
        self.w2 = w2
        self.bias = bias

    def sigmoid(self, x1, x2):
        v = x1 * self.w1 + x2 * self.w2 + self.bias
        output = (1.0/(1+exp(v)))
        if (output > 0.4):
            return 0
        return 1

    def funAux(self,x):
        return 2*x + 5

    def training(self,iter):
        C = 0.01
        realValues = []
        predictValues = []
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
            realValues.append(output)
            predict = self.sigmoid(x1, y1)
            predictValues.append(predict)
            if(predict == 0 and output == 1):
                bad += 1
                self.w1 = self.w1 + C * x1
                self.w2 = self.w2 + C * y1
            elif(predict == 1 and output == 0):
                bad += 1
                self.w1 = self.w1 - C * x1
                self.w2 = self.w2 - C * y1
            else:
                good += 1
            goodArray.append(good)
            badArray.append(bad)
        return [goodArray,badArray,realValues,predictValues]
    ### RETORNAR ARRAYS Y CREAR FUNCION TEST QUE GRAFIQUE

    def prediction(self,iter):
        goodArray = []
        badArray = []
        realValues = []
        predictValues = []
        class0x = []
        class0y = []
        class1x = []
        class1y = []
        good = 0
        bad = 0
        for j in range(iter):
            x1 = random.randint(-50,50)
            y1 = random.randint(-50,50)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            realValues.append(output)
            predict = self.sigmoid(x1,y1)
            predictValues.append(predict)
            if(predict == 0):
                class0x.append(x1)
                class0y.append(y1)
            else:
                class1x.append(x1)
                class1y.append(y1)
            if(predict == 0 and output == 1):
                bad += 1
            elif(predict == 1 and output == 0):
                bad += 1
            else:
                good += 1
            goodArray.append(good)
            badArray.append(bad)
            ##print bad,good
        return [goodArray,badArray,realValues,predictValues,class0x,class0y,class1x,class1y]

    def testTraining(self):
        ### Entrenamiento ###
        iter = 2000
        [good,bad,real,pred] = self.training(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            bad[j] = (bad[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.plot(x,good)
        #plt.figure()
        #plt.plot(x,bad)
        plt.ylim([0.0,1.05])
        plt.figure()
        fp, tp, th = roc_curve(real, pred)
        plt.plot(fp, tp)
        plt.show()

    def testPrediction(self):
        ### Entrenamiento ###
        iter = 400
        [good,bad,real,pred,c0x,c0y,c1x,c1y] = self.prediction(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            bad[j] = (bad[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.plot(x,good)
        #plt.figure()
        #plt.plot(x,bad)
        plt.ylim([0.0, 1.05])
        plt.figure()
        plt.plot(c0x, c0y, 'or')
        plt.plot(c1x, c1y, 'ob')
        plt.plot([-50,50], [self.funAux(-50),self.funAux(50)])
        plt.figure()
        fp, tp, th = roc_curve(real, pred)
        plt.plot(fp,tp)
        plt.show()

p = Sigmoid(10,1,-2.5)
p.testTraining()
p.testPrediction()