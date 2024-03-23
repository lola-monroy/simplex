# Simplex
En esta práctica se desarrolla el algoritmo de un **simplex primal**, tal y como se ha visto en clase, usando python. 
Trabajaremos para resolver un total de 8 problemas entre los dos miembros del grupo (de los conjuntos de datos 13 y 24). Los problemas a resolver, siempre serán lineales, pero pueden ser factibles, infactibles, no acotados o degenerados. 

#### Uso de biblioteca NumPy
La biblioteca NumPy facilita el procesamiento numérico en el ámbito de matrices y vectores, por lo que nos será extremadamente útil al computar multiplicaciones entre estos . Esta biblioteca proporciona los 'arrays', que permiten almacenar y manipular grandes conjuntos de datos numéricos. 

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

Este, que lleva el nomre de **_calcula_**, tiene el propósito de coordinar la resolución del problema utilizando el método Simplex y devolver el resultado final. Lleva a cabo dos fases:

1. **Fase 1**: introduce variables artificiales si es necesario para encontrar una solución inicial factible. Esto se hará cuando el problema inicial no tenga una solución factible. En esta fase, se creará una nueva función objetivo y un conjunto de restricciones con variables artificiales, y se resorverá utilizando el método Simplex (definido posteriormente).

2. **Fase 2**: resuelve el problema original utilizando el método Simplex. Una vez que se haya encontrado una solución factible en la fase 1, esta solución se utilizará como punto de partida para resolver el problema original. En esta fase, se utilizará el método Simplex para optimizar la función objetivo sujeta a las restricciones del problema original.

El tercer método, és el del **_Simplex_**, que realiza iteraciones con el propósito de encontrar una solución óptima. Lo hace mejorando la solución actual en cada iteracion hasta alcanzar la solución óptima o determinar que el problema no está acotado. El orden en el que realiza las acciones y actualizaciones es el siguiente: 

1. Se ordenan las variables no básicas (no_base).
2. Se calculan matrices B, An, y B_inv basadas en las matrices originales A, b, y c, respectivamente.
3. Se calculan las variables básicas (x_b) resolviendo el sistema de ecuaciones lineales B * x_b = b utilizando la matriz inversa B_inv.
4. Se calcula el vector r, que representa el costo reducido de las variables no básicas.
e. Se calcula el valor de la función objetivo z.
f. Si todos los costos reducidos son mayores o iguales a cero, se ha encontrado una solución óptima y se devuelve el valor de z y las variables básicas.
g. Si hay algún costo reducido negativo, se elige una variable no básica para entrar en la base (indice_variable_entra) basándose en el criterio de mínimo costo reducido negativo.
h. Se calcula la dirección factible (d_b) en la que se puede mover la solución para mejorar la función objetivo.
i. Si todas las direcciones son no positivas, el problema no está acotado y se devuelve un mensaje indicando esto.
j. Se selecciona una variable básica para salir de la base (variable_sale) basándose en el criterio de mínima razón. Se intercambian las variables básicas y no básicas correspondientes.

Se repite el proceso hasta que se encuentra una solución óptima o se determina que el problema no está acotado.

Podemos decir que, resumidamente, _calcula_ coordina las fases del algoritmo para resolver el problema, mientras que el método _SIMPLEX_ implementa el propio algoritmo Simplex.

#### Formato de las actualizaciones
Las sigüientes líneas de código forman parte del bucle iterativo para encontrar la solución óptima del problema de programación lineal.

1. B = A[:, self.base]: operación para seleccionar las columnas de la matriz A correspondientes a las variables **básicas** ('self.base' es ser una lista de índices que representan las variables básicas). Se están seleccionando todas las filas de la matriz A, pero solo las columnas cuyos índices están en la lista 'self.base'.
2. An = A[:, self.no_base]: selecciona las columnas de la matriz A correspondientes a las variables **no básicas** ('self.no_base' es una lista de índices que representan las variables no básicas). 

3. B_inv = np.linalg.inv(B): calcula la inversa de la matriz B. (B representa la matriz de coeficientes de las variables básicas).

4. x_b = x_b_old + theta * d_b: se está actualizando el vector de variables básicas 'x_b' multiplicando un paso ('theta') por la dirección ('d_b') en la que se va a mover.

5. c_b = c[self.base]: selecciona coeficientes de la función objetivo correspondientes a las variables básicas.
6. c_n = c[self.no_base]: selecciona los coeficientes de la función objetivo correspondientes a las variables no básicas.

7. z = z_old + theta * rq: se está actualizando el valor de la función objetivo 'z' multiplicando un paso ('theta') por el vector de reducción de costos ('rq').


