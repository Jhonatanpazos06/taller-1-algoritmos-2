
import time

# Profe, aquí importé time para medir el tiempo de ejecución.

# Profe, aquí creé una lista con 1 millón de números.
numeros = list(range(1000000))

# Profe, aquí guardé el tiempo antes de iniciar la operación.
inicio = time.perf_counter()

# Profe, aquí multipliqué cada número por 2.
resultado = [numero * 2 for numero in numeros]

# Profe, aquí guardé el tiempo al finalizar.
fin = time.perf_counter()

# Profe, aquí calculé cuánto tardó la operación.
tiempo = fin - inicio

print("Tiempo con listas:", tiempo, "segundos")
print("Primeros 5 resultados:", resultado[:5])
