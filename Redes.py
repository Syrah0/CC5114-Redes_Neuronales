### Alumna: Alexandra Ibarra

# x1: valor entrada 1
# w1: peso entrada 1
# x2: valor entrada 2
# w2: peso entrada 2
# bias: bias del perceptron
## Se encarga de inicialiar un perceptron y
## realizar el calculo respectivo
def perceptron(x1,x2,w1,w2,bias):
    v = x1*w1 + x2*w2
    if(v+bias <= 0):
        return 0
    return 1

# x1: valor entrada 1
# x2: valor entrada 2
## Se encarga de realizar el calculo logico NAND
def NAND(x1,x2):
    return perceptron(x1,x2,-2,-2,3)

# x1: valor entrada 1
# x2: valor entrada 2
## Se encarga de simular la compuerta logica AND
def AND(x1,x2):
    return perceptron(x1,x2,1,1,-1.5)

# x1: valor entrada 1
# x2: valor entrada 2
## Se encarga de simular la compuerta logica OR
def OR(x1,x2):
    return perceptron(x1,x2,1,1,-0.5)

# x1: valor entrada 1
# x2: valor entrada 2
## Se encarga de realizar el calculo de suma de dos bits
## retorna el valor de la suma (p1) y el carry de la suma (p2) en un array
def Summing_numbers(x1,x2):
    v1 = NAND(x1,x2)
    o1 = NAND(x1,v1)
    o2 = NAND(v1,x2)
    p1 = NAND(o1,o2)
    p2 = NAND(v1,v1)
    return [p1,p2]

# test AND, OR, NAND
# for it in [(0,0),(0,1),(1,0),(1,1)]:
#    print(it[0],"-",it[1],"-->",OR(it[0],it[1]))

## TEST NAND
assert NAND(0,0)== 1
assert NAND(0,1)== 1
assert NAND(1,0)== 1
assert NAND(1,1)== 0

## TEST AND
assert AND(0,0)== 0
assert AND(0,1)== 0
assert AND(1,0)== 0
assert AND(1,1)== 1

## TEST OR
assert OR(0,0)== 0
assert OR(0,1)== 1
assert OR(1,0)== 1
assert OR(1,1)== 1

# test para summing numbers
#for it in [(0,0),(0,1),(1,0),(1,1)]:
#    print(it[0],"-",it[1],"-->",Summing_numbers(it[0],it[1]))

## TEST SUMMING_NUMBERS
assert Summing_numbers(0,0)==[0,0]
assert Summing_numbers(0,1)==[1,0]
assert Summing_numbers(1,0)==[1,0]
assert Summing_numbers(1,1)==[0,1]
