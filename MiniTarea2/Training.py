import random
import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve

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

    ## Funcion auxiliar encargada para calculo de la clase de los elementos
    def funAux(self,x):
        return 2*x + 5

    ## Funcion encargada del proceso de entrenamiento del perceptron
    ## Esta recibe como parametro la cantidad de iteraciones que se desean realizar para entrenar
    def training(self,iter):
        C = 0.01
       # realValues = [] # contiene los valores o clases reales de los puntos
       # predictValues = [] # contiene las clases predichas por el perceptron
        goodArray = [] # contiene la cantidad de elementos buenas tras cada iteracion
        good = 0 # cantidad de clases correctamente acertadas
        for j in range(iter):
            x1 = random.randint(-50,50)
            y1 = random.randint(-50,50)
            if(self.funAux(x1)>y1):
                output = 0
            else:
                output = 1
            #realValues.append(output)
            predict = self.perceptron(x1, y1)
            #predictValues.append(predict)
            if(predict == 0 and output == 1):
                self.w1 = self.w1 + C * x1
                self.w2 = self.w2 + C * y1
            elif(predict == 1 and output == 0):
                self.w1 = self.w1 - C * x1
                self.w2 = self.w2 - C * y1
            else:
                good += 1
            goodArray.append(good)
            #print(self.w1, self.w2)
        return goodArray

    ## Funcion encargada de predecir las clases de diferentes elementos usando un perceptron ya entrenado
    def prediction(self,iter):
        #realValues = []  # contiene los valores o clases reales de los puntos
        #predictValues = []  # contiene las clases predichas por el perceptron
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
            #realValues.append(output)
            predict = self.perceptron(x1,y1)
            #predictValues.append(predict)
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

    # Funcion encargada de testear el entrenamiento del perceptron
    # grafica el rendimiento del entrenamiento
    def testTraining(self):
        ### Entrenamiento ###
        iter = 1000
        good = self.training(iter)
        x = []
        for j in range(iter):
            good[j] = (good[j]*1.0) / (j + 1)
            x.append(j)
        plt.figure()
        plt.title("Rendimiento del entrenamiento")
        plt.ylabel("Cantidad de puntos correctamente clasificados")
        plt.xlabel("N° iteraciones")
        plt.plot(x,good)
        plt.ylim([0.0,1.05])
        plt.show()

    # Funcion encargada de testear el rendimiento del perceptron ya entrenado
    # grafica el rendimiento del perceptron con un nuevo conjunto (prueba)
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
        #plt.figure()
        #plt.title("Curva de ROC del rendimiento del perceptron en testing")
        #fp, tp, th = roc_curve(real, pred)
        #plt.plot(fp,tp)
        plt.show()

#### TESTING #####

# crea perceptron para proceso de testeo
p = Perceptron(-2.5,1.5,-0.5)
#p = Perceptron(10,1,-2.5)
p.testTraining()
p.testPrediction()