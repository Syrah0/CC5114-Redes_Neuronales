El link directo al repositorio que contiene la tarea es:

https://github.com/Syrah0/CC5114-Redes_Neuronales/tree/master/MiniTarea2


IMPORTANTE!!!!

Esta carpeta contiene 1 archivo escrito en lenguaje Python 3.5.3
Adem�s es posible observar una carpeta de resultados donde se encuentran algunas im�genes con los resultados obtenidos tras variar el valor de C.

Es IMPORTANTE se�alar que para ejecutar el c�digo se necesita de la librer�a:  Matplotlib 
Esta permite graficar y visualizar los diferentes gr�ficos realizados.

MODO DE EJECUCI�N Y COMPILACI�N

En primer lugar se deben descargar los archivos del repositorio ya sea clonando el repositorio de github con el comando:

git clone https://github.com/Syrah0/CC5114-Redes_Neuronales.git

o de manera manual copiando los archivos de github a un archivo propio (copy and paste).


Las siguientes instrucciones se dar�n considerando que se utiliza PyCharm dado que este facilita la instalaci�n de la librer�a deseada

1.- Teniendo los archivos se debe abrir PyCharm.

2.- Luego se debe ir a la opci�n "File" y poner "Open...".

3.- Buscar la carpeta o archivo que se desea ejecutar (es recomendable seleccionar la carpeta que contiene el archivo y hacer click en "OK", en caso contrario seleccionar el archivo Training.py y luego "OK")

4.- Una vez abierto el archivo seleccionado hacer click derecho sobre el nombre del archivo (o en el archivo como tal) y seleccionar "Run 'Training.py'".

Es importante se�alar que en caso que no se haya configurado un interprete para el lenguaje se deber� configurar uno, para eso se debe ir a File -> Settings y seleccionar el "Project Interpreter". NOTAR QUE EL INTERPRETE DEBE TENER INSTALADA LA LIBRERIA MATPLOTLIB (sino ir al signo + e instalarla) 

Tras lo anterior aparecer�n los gr�ficos tras el entrenamiento del perceptr�n.


NOTA!!!!!!!!!

Tambien es posible realizar lo mismo a trav�s de la consola de python (Python Console). Esto ser� recomendable en caso que se deseen ejecutar las funciones por separado. 
Para esto se debe ir, en PyCharm, a Python Console.
Luego poner:

from <Nombre/Carpeta/Archivo>.Training import *

Por ejemplo, si Training.py est� de Tarea entonces poner: from Tarea.Training import *

IMPORTANTE!!!! EL NOMBRE DE LA CARPETA SE PONE SI Y SOLO SI DICHA CARPETA EST� CONTENIDA DENTRO DE LA CARPETA DEL PROYECTO. EN EL EJEMPLO ANTERIOR ES EQUIVALENTE A DECIR QUE:

Proyect
 |--> Tarea
	|--> Training.py

EN CASO CONTRARIO ES SOLO from Training import *

Tras lo anterior se ejecutar� automaticamente el proceso de prueba escrito en el c�digo y la generaci�n de los gr�ficos. En caso de probar las otras funciones basta con colocar:

p.perceptron(x1,x2)

En dicho caso se usar� el perceptr�n entrenado. Si se desea usar otro perceptron entonces usar:

p2 = Perceptron(w1,w2,bias)
p2.perceptron(x1,x2)

por ejemplo.