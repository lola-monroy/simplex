# Función para leer el archivo y extraer las matrices
import numpy as np

def leer_archivo(nombre_archivo):
    c = []
    A = []
    b = []

    with open(nombre_archivo, 'r') as file:
        for line in file:
            if 'c=' in line:
                while True:
                    line = next(file)
                    if line=='\n':
                        break

                    for x in line.split():
                        c.append(int(x))

            elif 'A=' in line:
                while True:
                    line = next(file)
                    A.append([int(x) for x in line.split()])
                    if line=='\n':
                        A.pop()
                        break

            elif 'b=' in line:
                line = next(file)
                for x in line.split():
                    b.append(int(x))                    
    # Convertir las listas a arrays numpy
    c = np.array(c)
    A = np.array(A)
    b = np.array(b)
    
    return c, A, b
