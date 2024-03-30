''' LECTOR DE ARCHIVO + BÁSICO: input individual y editado '''
from clase_simplex import SIMPLEX
from funcion_lectura import leer_archivo
# # Llamar a la función para leer el archivo
nombre_archivo = input("Por favor, ingresa el nombre del fichero en el que se encuentra el problema: ")
nombre_archivo+='.txt'
c, A, b = leer_archivo(nombre_archivo)

# Mostrar las matrices
print(" La matriz c es:",end=' ')
print(c)
print("\n La matriz A es:",end=' ')
print(A)
print("\n El vector b es:",end=' ')
print(b)

simplex = SIMPLEX(c, A, b)
result = simplex.calcula()
