El link directo al repositorio que contiene la tarea es:

https://github.com/Syrah0/CC5114-Redes_Neuronales/tree/master/MiniTarea2


IMPORTANTE!!!!

Esta carpeta contiene 1 archivo escrito en lenguaje Python 3.5.3
Además es posible observar una carpeta de resultados donde se encuentran algunas imágenes con los resultados obtenidos tras variar el valor de C.

Es IMPORTANTE señalar que para ejecutar el código se necesita de la librería:  Matplotlib 
Esta permite graficar y visualizar los diferentes gráficos realizados.

MODO DE EJECUCIÓN Y COMPILACIÓN

En primer lugar se deben descargar los archivos del repositorio ya sea clonando el repositorio de github con el comando:

git clone https://github.com/Syrah0/CC5114-Redes_Neuronales.git

o de manera manual copiando los archivos de github a un archivo propio (copy and paste).


Las siguientes instrucciones se darán considerando que se utiliza PyCharm dado que este facilita la instalación de la librería deseada

1.- Teniendo los archivos se debe abrir PyCharm.

2.- Luego se debe ir a la opción "File" y poner "Open...".

3.- Buscar la carpeta o archivo que se desea ejecutar (es recomendable seleccionar la carpeta que contiene el archivo y hacer click en "OK", en caso contrario seleccionar el archivo Training.py y luego "OK")

4.- Una vez abierto el archivo seleccionado hacer click derecho sobre el nombre del archivo (o en el archivo como tal) y seleccionar "Run 'Training.py'".

Es importante señalar que en caso que no se haya configurado un interprete para el lenguaje se deberá configurar uno, para eso se debe ir a File -> Settings y seleccionar el "Project Interpreter". NOTAR QUE EL INTERPRETE DEBE TENER INSTALADA LA LIBRERIA MATPLOTLIB (sino ir al signo + e instalarla) 

Tras lo anterior aparecerán los gráficos tras el entrenamiento del perceptrón.


NOTA!!!!!!!!!

Tambien es posible realizar lo mismo a través de la consola de python (Python Console). Esto será recomendable en caso que se deseen ejecutar las funciones por separado. 
Para esto se debe ir, en PyCharm, a Python Console.
Luego poner:

from <Nombre/Carpeta/Archivo>.Training import *

Por ejemplo, si Training.py está de Tarea entonces poner: from Tarea.Training import *

IMPORTANTE!!!! EL NOMBRE DE LA CARPETA SE PONE SI Y SOLO SI DICHA CARPETA ESTÁ CONTENIDA DENTRO DE LA CARPETA DEL PROYECTO. EN EL EJEMPLO ANTERIOR ES EQUIVALENTE A DECIR QUE:

Proyect
 |--> Tarea
	|--> Training.py

EN CASO CONTRARIO ES SOLO from Training import *

Tras lo anterior se ejecutará automaticamente el proceso de prueba escrito en el código y la generación de los gráficos. En caso de probar las otras funciones basta con colocar:

p.perceptron(x1,x2)

En dicho caso se usará el perceptrón entrenado. Si se desea usar otro perceptron entonces usar:

p2 = Perceptron(w1,w2,bias)
p2.perceptron(x1,x2)

por ejemplo.