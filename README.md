# Simplex
En esta práctica se desarrolla el algoritmo de un **simplex primal**, tal y como se ha visto en clase, usando python. 
Trabajaremos para resolver un total de 8 problemas entre los dos miembros del grupo (de los conjuntos de datos 13 y 24). Los problemas a resolver, siempre serán lineales, pero pueden ser factibles, infactibles, no acotados o degenerados. 

#### Uso de biblioteca NumPy
La biblioteca NumPy facilita el procesamiento numérico en el ámbito de matrices y vectores, por lo que nos será extremadamente útil al computar multiplicaciones entre estos . Esta biblioteca proporciona los 'arrays', que permiten almacenar y manipular grandes conjuntos de datos numéricos. 
#### Ejecución del programa
Para ejecutar el programa diríjase al fichero de nombre fichero_ejecucion y ejecutelo. A continuación se le preguntará por un fichero(problema) que ejecutar: introduzca su nombre(sin el .txt) y el probrema será resuelto y sus resultados se mostrarán por pantalla.
#### Leyendo el archivo de entrada
El archivo de entrada consta de diferentes problemas, agrupados en grupos de 4. Es decir, cada 4 problemas se agrupan en un conjunto de datos. 

Cada uno de estos problemas nos proporciona la sigiente información: 
1. Índice del conjunto de datos y número del problema
2. 'c' = vector
3. 'A' = matriz
4. 'b' = vector
   
Y solo en el primer fichero de cada conjunto de datos, encontramos también:
6. *z = función objetivo
7. *vb = variables básicas

Para leerlo, creamos una función que se encarga de leer los 3 primeros elementos y los transforma en un 'array' de numpy para facilitar la posterior manipulación de estos.  

#### Clase _Simplex_
Hemos desarrollado una clase con 3 métodos (1 de los cuales es el de inicialización), para el desarrollo de nuestra práctica. Después de la inicialización de las 3 variables que leemos del fichero (c, A y b), así como la del tamaño de la matriz 'A', procedemos al segundo método. 

Este, que lleva el nombre de **_calcula_**, tiene el propósito de coordinar la resolución del problema utilizando el método Simplex y devolver el resultado final. Lleva a cabo dos fases:

1. **Fase 1**: introduce variables artificiales si es necesario para encontrar una solución inicial factible. Esto se hará cuando el problema inicial no tenga una solución factible. En esta fase, se creará una nueva función objetivo y un conjunto de restricciones con variables artificiales, y se resorverá utilizando el método Simplex (definido posteriormente). Esta fase está dividida en dos métodos de nombre fase1_1 y fase1_2. Esto es así por motivos de programación para poder implementar de manera eficiente la actualización de la inversa ahorrando condiciones que puedan ralentizar el algoritmo.

2. **Fase 2**: resuelve el problema original utilizando el método Simplex. Una vez que se haya encontrado una solución factible en la fase 1, esta solución se utilizará como punto de partida para resolver el problema original. En esta fase, se utilizará el método Simplex para optimizar la función objetivo sujeta a las restricciones del problema original. Esta fase está dividia en otra pareja de métodos distintos a la pareja de la fase anterior(y por los mismos motivos) de nombres SIMPLEX y SIMPLEX2

Hay un tercer método, el del **_Theta_**, que realiza el cálculo de la Theta(longitud de paso) hayando la menor y también la variable a salir; y un cuarto método, el de **actualizacion_inv** que realiza, como su nombre indica, la actualización de la inversa.
Fase 1 y Fase 2, como hemos visto, se dividen en dos métodos uno que se ejecuta una única vez y otro que se itera hasta hayar la solución pero de manera igual funcionan de la siguiente manera:
1. Se ordenan las variables no básicas (no_base).
2. Se calculan matrices B, An, y B_inv(o se actualiza si estamos en el segundo método de la pareja) basadas en las matrices originales A, b, y c, respectivamente.
3. Se calculan las variables básicas (x_b) resolviendo el sistema de ecuaciones lineales B * x_b = b utilizando la matriz inversa B_inv.
4. Se calcula el vector r, que representa el costo reducido de las variables no básicas.
5. Se calcula el valor de la función objetivo z.
6. Si todos los costos reducidos son mayores o iguales a cero, se ha encontrado una solución óptima y se devuelve el valor de z y las variables básicas.
7. Si hay algún costo reducido negativo, se elige una variable no básica para entrar en la base (indice_variable_entra) basándose en el criterio de mínimo costo reducido negativo.
8. Se calcula la dirección factible (d_b) en la que se puede mover la solución para mejorar la función objetivo.
9. Si todas las direcciones son no positivas, el problema no está acotado y se devuelve un mensaje indicando esto.
10. Se selecciona una variable básica para salir de la base (variable_sale) basándose en el criterio de mínima razón. Se intercambian las variables básicas y no básicas correspondientes.

Se repite el proceso hasta que se encuentra una solución óptima o se determina que el problema no está acotado.

Podemos decir que, resumidamente, _calcula_ coordina las fases del algoritmo para resolver el problema llamando primero a un método de la fase1(que llamará al siguiente método de la fase) y después al primero de los métodos de la segunda fase que llamará a su vez el siguiente método de la pareja.

#### Actualizaciones
Queremos especificar que, mientras actualizamos la inversa debido a que este es un cálculo complejo, largo e inestable, vimos inncecesario realizar los cálculos de actualización de la Xb o la z y simplemente los recalculamos de nuevo.

