
import time
import numpy as np

# Profe, aquí definí la cantidad de datos.
cantidad = 1000000

# Profe, aquí creé ambas estructuras.
lista = list(range(cantidad))
array = np.arange(cantidad)

tiempos_lista = []
tiempos_array = []

# Profe, aquí repetí las pruebas 5 veces.
for i in range(5):

    # Medimos el tiempo de la lista.
    inicio = time.perf_counter()
    resultado_lista = [n * 2 for n in lista]
    fin = time.perf_counter()

    tiempos_lista.append(fin - inicio)

    # Medimos el tiempo del array.
    inicio = time.perf_counter()
    resultado_array = array * 2
    fin = time.perf_counter()

    tiempos_array.append(fin - inicio)

# Profe, aquí calculé los promedios.
promedio_lista = sum(tiempos_lista) / 5
promedio_array = sum(tiempos_array) / 5

# Verificamos que los resultados sean iguales.
iguales = np.array_equal(resultado_lista, resultado_array)

print("Tiempo promedio lista:", promedio_lista)
print("Tiempo promedio NumPy:", promedio_array)
print("Resultados iguales:", iguales)

if promedio_array < promedio_lista:
    print("NumPy fue más rápido")
elif promedio_lista < promedio_array:
    print("La lista fue más rápida")
else:
    print("Ambas tardaron lo mismo")
