### Alumna: Alexandra Ibarra

# x1: valor entrada 1
# w1: peso entrada 1
# x2: valor entrada 2
# w2: peso entrada 2
# bias: bias del perceptron
## Se encarga de representar un perceptron
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

    ## Se encarga de simular la compuerta logica NAND
    def NAND(self, x1, x2):
        self.w1 = -2
        self.w2 = -2
        self.bias = 3
        return self.perceptron(x1, x2)

    ## Se encarga de simular la compuerta logica AND
    def AND(self, x1, x2):
        self.w1 = 1
        self.w2 = 1
        self.bias = -1.5
        return self.perceptron(x1, x2)

    ## Se encarga de simular la compuerta logica OR
    def OR(self, x1, x2):
        self.w1 = 1
        self.w2 = 1
        self.bias = -0.5
        return self.perceptron(x1, x2)

    ## Se encarga de realizar el calculo de suma de dos bits
    ## retorna el valor de la suma (p1) y el carry de la suma (p2) en un array
    def Summing_numbers(self, x1, x2):
        v1 = self.NAND(x1, x2)
        o1 = self.NAND(x1, v1)
        o2 = self.NAND(v1, x2)
        p1 = self.NAND(o1, o2)
        p2 = self.NAND(v1, v1)
        return [p1, p2]

    ## TEST PARA NAND
    def TestNAND(self):
        assert self.NAND(0, 0) == 1
        assert self.NAND(0, 1) == 1
        assert self.NAND(1, 0) == 1
        assert self.NAND(1, 1) == 0

    ## TEST PARA AND
    def TestAND(self):
        assert self.AND(0, 0) == 0
        assert self.AND(0, 1) == 0
        assert self.AND(1, 0) == 0
        assert self.AND(1, 1) == 1

    ## TEST PARA OR
    def TestOR(self):
        assert self.OR(0, 0) == 0
        assert self.OR(0, 1) == 1
        assert self.OR(1, 0) == 1
        assert self.OR(1, 1) == 1

    ## TEST PARA SUMMING_NUMBERS
    def TestSumming(self):
        assert self.Summing_numbers(0, 0) == [0, 0]
        assert self.Summing_numbers(0, 1) == [1, 0]
        assert self.Summing_numbers(1, 0) == [1, 0]
        assert self.Summing_numbers(1, 1) == [0, 1]