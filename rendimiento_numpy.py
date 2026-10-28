
import time
import numpy as np

# Profe, aquí importé NumPy para trabajar con arrays.

# Profe, aquí creé un array con 1 millón de números.
numeros = np.arange(1000000)

# Profe, aquí guardé el tiempo inicial.
inicio = time.perf_counter()

# Profe, aquí multipliqué todos los elementos por 2.
resultado = numeros * 2

# Profe, aquí guardé el tiempo final.
fin = time.perf_counter()

# Profe, aquí calculé el tiempo de ejecución.
tiempo = fin - inicio

print("Tiempo con NumPy:", tiempo, "segundos")
print("Primeros 5 resultados:", resultado[:5])
