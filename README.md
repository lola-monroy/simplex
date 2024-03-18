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
Se presentan dos opciones para calcular la solución básica factible inicial (SBF) utilizando la fase I del símplex:

1. Integrar la fase I en el código, formulando y resolviendo automáticamente el problema de fase I a partir de los parámetros originales, y luego continuar con la fase II si se encuentra una SBF.
2. Implementar solo la fase II del símplex y ejecutarla dos veces: una vez con los parámetros correspondientes al problema de fase I y una SBF inicial trivial, y otra vez con los parámetros originales y la SBF encontrada por la fase I.

Se requiere implementar la regla de Bland para la selección de variables de entrada y salida en caso de empate.

