''' LECTOR DE ARCHIVO + BÁSICO: input individual y editado '''
import numpy as np

nombre_archivo = input("Por favor, ingresa el nombre del fichero en el que se encuentra el problema: ")

# Función para leer el archivo y extraer las matrices
def leer_archivo(nombre_archivo):
    c = []
    A = []
    b = []

    with open(nombre_archivo, 'r') as file:
        for line in file:
            if 'c=' in line:
                while True:
                    line = next(file)
                    c.append([int(x) for x in line.split()])
                    if line=='\n':
                        c.pop()
                        break

            elif 'A=' in line:
                while True:
                    line = next(file)
                    A.append([int(x) for x in line.split()])
                    if line=='\n':
                        A.pop()
                        break

            elif 'b=' in line:
                line = next(file)
                b.append([int(x) for x in line.split()])
                    
    # Convertir las listas a arrays numpy
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)
    
    return c, A, b

# # Llamar a la función para leer el archivo
c, A, b = leer_archivo(nombre_archivo)

# Mostrar las matrices
print(" La matriz c és:")
print(c)
print("\n La matriz A és:")
print(A)
print("\n El vector b és:")
print(b)
