# Simplex
En esta práctica se desarrolla el algoritmo de un **simplex** en python. 

#### Resumen del enunciado de la práctica

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

