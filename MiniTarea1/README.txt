El link directo al repositorio que contiene la tarea es:

https://github.com/Syrah0/CC5114-Redes_Neuronales/tree/master/MiniTarea1

IMPORTANTE!!!!

Esta carpeta contiene 2 archivos, ambos escritos en lenguaje Python 3.6.1:

Redes.py -> Es el primer archivo creado, este solo implementa las funciones pedidas.

Redes2.py ->  Es el segundo archivo creado, este implementa una clase perceptron (siguiendo la indicación final del profesor) la cual contiene las funciones pedidas.

MODO DE EJECUCIÓN Y COMPILACIÓN

En primer lugar se deben descargar los archivos del repositorio ya sea clonando el repositorio de github con el comando:

git clone https://github.com/Syrah0/CC5114-Redes_Neuronales.git

o de manera manual copiando los archivos de github a un archivo propio (copy and paste).


Las siguientes instrucciones se darán considerando que se utiliza el IDLE de Python (shell):

1.- Teniendo los archivos se debe abrir el IDLE de python (o consola de python).

2.- Luego se debe ir a la opción "File" y poner "Open..." (o simplemente utilizar Ctrl+O)

3.- Buscar el archivo a querer ejecutar (Redes.py o Redes2.py) y hacer click sobre el para abrir. 

4.- Una vez abierto el archivo seleccionado hacer click en la opción "Run" y poner "Run Module" (o simplemente utilizar F5) para ejecutar el código y así correr los test (esto último será válido solo para Redes.py).

Es importante señalar que este paso se debe realizar para que el Shell de Python identifique la dirección donde se encuentra el archivo .py a ejecutar (Redes.py o Redes2.py). 

IMPORTANTE: EL PASO 5 DEPENDE DEL ARCHIVO EJECUTADO EN EL PASO 4. SI SE EJECUTÓ Redes.py ENTONCES LEER LAS INSTRUCCIONES PARA DICHO ARCHIVO (5.a), EN CASO CONTRARIO LEER LAS INSTRUCCIONES PARA Redes2.py (5.b). 

TRAS HABER PROBADO UNO DE LOS ARCHIVOS Y, SI SE DESEA EJECUTAR EL OTRO, SE DEBEN REPETIR LOS PASOS DESDE EL 2 ABRIENDO EL ARCHIVO CONTRARIO (esto se realiza en caso de que los archivos se hayan guardado en carpetas diferentes, si están en la misma carpeta no es necesario y se pueden realizar las instruccioness 5.a y 5.b de forma simultanea).

5.- Luego ir al IDLE de Python. 

a) Para probar el archivo 'Redes.py' poner lo siguiente:

from Redes import *

Eso permitirá importar todas las funciones del archivo, en este caso para probar las funciones basta con poner el nombre de la función con sus respectivos parámetros por ejemplo, para ejecutar la calculadora de dos bits colocar:

Summing_numbers(0,0)

En caso de querer sumar 0 con 0. Esto retornará un array [0,0]. Para ejecutar la función NAND realizar lo siguiente:

NAND(0,0)

b) Para probar el archivo 'Redes2.py' se deberá realizar lo siguiente, poner:

from Redes2 import *

Esto permitirá importar todas las funciones de la clase Perceptron, luego crear un objeto perceptron de la siguiente manera:

neurona = Perceptron(1,1,2)

Esto creará un perceptron que cuyo bias es 2 y los pesos son w1 = 1 y w2 = 1. Luego, para ejecutar las funciones se deberá realizar lo siguiente, por ejemplo, para ejecutar la calculadora de dos bits colocar:

neurona.Summing_numbers(0,0)

En caso de querer sumar 0 con 0. Esto retornará un array [0,0]. Para ejecutar la función NAND realizar lo siguiente:

neurona.NAND(0,0)

Para ejecutar el resto de las funciones se sigue la misma mecánica.



NOTA!!!!
CADA ARCHIVO TIENE SUS ASSERT O TEST, EN EL CASO DE Redes.py LOS ASSERT SE ENCUENTRAN AL FINAL DEL ARCHIVO POR LO QUE PARA EJECUTARLOS BASTA CON REALIZAR F5 TAL COMO DICE EL PASO 4.

EN CASO DEL ARCHIVO Redes2.py LOS ASSERT SON PARTE DE FUNCIONES DE TEST POR LO QUE PARA EJECUTARLOS REALIZAR LO SIGUIENTE:

###### TEST NAND ######

neurona.TestNAND()


###### TEST AND ######

neurona.TestAND()


###### TEST OR ######

neurona.TestOR()


###### TEST SUMMING ######

neurona.TestSumming()


LOS TEST REALIZADOS SON EXACTAMENTE LOS MISMOS EN AMBOS ARCHIVOS. SI TRAS SU EJECUCIÓN NO APARECE NINGÚN ERROR QUIERE DECIR QUE LOS TEST PASARON CORRECTAMENTE.