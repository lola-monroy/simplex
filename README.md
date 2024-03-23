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
5. *z 
6. *vb

Para leerlo, creamos una función que se encarga de leer los 3 primeros elementos y los transforma en un 'array' de numpy para facilitar la posterior manipulación de estos.  

#### Desarrollo del simplex
Para calcular la solución básica factible inicial (SBF) tenemos dos opicones:

1. Integrar la fase I en el código y luego continuar con la fase II si se encuentra una SBF.
2. Implementar solo la fase II del símplex y ejecutarla dos veces: una vez con los parámetros correspondientes al problema de fase I y una SBF inicial trivial, y otra vez con los parámetros originales y la SBF encontrada por la fase I.

Se requiere implementar la regla de Bland para la selección de variables de entrada y salida en caso de empate.

#### Formato de las actualizaciones
Las sigüientes líneas de código forman parte del bucle iterativo para encontrar la solución óptima del problema de programación lineal.

1. B = A[:, self.base]: operación para seleccionar las columnas de la matriz A correspondientes a las variables **básicas** ('self.base' es ser una lista de índices que representan las variables básicas). Se están seleccionando todas las filas de la matriz A, pero solo las columnas cuyos índices están en la lista 'self.base'.
2. An = A[:, self.no_base]: selecciona las columnas de la matriz A correspondientes a las variables **no básicas** ('self.no_base' es una lista de índices que representan las variables no básicas). 

3. B_inv = np.linalg.inv(B): calcula la inversa de la matriz B. (B representa la matriz de coeficientes de las variables básicas).

4. x_b = x_b_old + theta * d_b: se está actualizando el vector de variables básicas 'x_b' multiplicando un paso ('theta') por la dirección ('d_b') en la que se va a mover.

5. c_b = c[self.base]: selecciona coeficientes de la función objetivo correspondientes a las variables básicas.
6. c_n = c[self.no_base]: selecciona los coeficientes de la función objetivo correspondientes a las variables no básicas.

7. z = z_old + theta * rq: se está actualizando el valor de la función objetivo 'z' multiplicando un paso ('theta') por el vector de reducción de costos ('rq').


