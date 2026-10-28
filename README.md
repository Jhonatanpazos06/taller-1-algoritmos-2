# Taller de Laboratorio #1: Listas y Arrays

**Asignatura:** Algoritmos 2  
**Estudiante:** Jhonatan Pazos
**Fecha:** 27/10/2026

## Objetivo

Comparar experimentalmente el rendimiento de listas de Python y arrays de NumPy en operaciones matemáticas con muchos valores, y diseñar una solución para gestionar calificaciones de estudiantes.

## Parte 1. Comparación de rendimiento

### Planteamiento e hipótesis

Se necesita multiplicar por dos un conjunto grande de valores numéricos en el menor tiempo posible. La hipótesis es que NumPy tardará menos, gracias a sus operaciones vectorizadas.

### Metodología

1. Se crearon una lista de Python y un array de NumPy con **1.000.000** de enteros, del 0 al 999.999.
2. En ambas estructuras se multiplicó cada número por dos.
3. Se midió únicamente la operación matemática con `time.perf_counter()`, sin incluir la creación inicial de las estructuras.
4. Cada operación se repitió **5 veces** y se calculó el promedio de sus tiempos.
5. Se comprobó la igualdad de los resultados mediante `np.array_equal()`.

**Archivos:** `rendimiento_listas.py`, `rendimiento_numpy.py` y `comparacion_rendimiento.py`.

### Resultados obtenidos

Estos valores corresponden a la ejecución real compartida por el estudiante:

| Medición | Resultado |
|---|---:|
| Tiempo promedio de lista | 0,1719545 segundos |
| Tiempo promedio de array NumPy | 0,0093616 segundos |
| Relación de tiempos (lista / NumPy) | 18.37 veces |
| ¿Los resultados numéricos coinciden? | `True` |

En esta ejecución, **NumPy fue aproximadamente 18.37 veces más rápido** para la operación evaluada. La medición es específica del equipo, del entorno y de este experimento; no representa una ventaja universal en todos los programas.

### Respuestas argumentadas

**1. ¿Qué diferencias se observan en el tiempo de ejecución y a qué se deben?**  
La lista tardó 0,1719545 segundos en promedio, mientras que NumPy tardó 0,0093616 segundos. NumPy fue más rápido en esta prueba porque ejecuta la multiplicación de manera vectorizada mediante rutinas optimizadas, mientras que la comprensión de lista procesa las operaciones mediante Python.

**2. ¿Cómo influye el almacenamiento en memoria?**  
Una lista de Python almacena referencias a objetos. Un array de NumPy normalmente guarda valores homogéneos en memoria compacta. Esta organización puede mejorar la localidad de memoria y facilitar operaciones numéricas eficientes. **No se midió directamente el uso de memoria en este experimento**, por lo que esta explicación es técnica y no un resultado de consumo de memoria observado.

**3. ¿Qué estructura se elegiría para grandes volúmenes de datos numéricos?**  
Elegiría NumPy cuando la tarea consista principalmente en operaciones matemáticas sobre muchos valores numéricos, porque en esta prueba tuvo un tiempo promedio menor y produjo los mismos resultados. Las listas siguen siendo útiles cuando se necesita flexibilidad para datos heterogéneos o tareas pequeñas.

### Conclusión de la Parte 1

Al multiplicar un millón de enteros por dos, NumPy presentó un tiempo promedio menor que la lista de Python. Ambas estructuras produjeron resultados equivalentes. La prueba respalda el uso de NumPy para esta operación numérica concreta, aunque conviene repetir mediciones en diferentes tamaños de datos y equipos antes de generalizar.

## Parte 2. Gestión de calificaciones

### Problema

Una aplicación académica debe almacenar notas, recorrerlas, calcular resultados, permitir correcciones bajo un criterio definido y presentar información consolidada.

### Estructura elegida y justificación

Se eligió una **lista de Python** porque conserva el orden de ingreso, acepta notas repetidas y permite cambiar un elemento mediante su índice. Para un registro sencillo no es necesario añadir NumPy ni asociar cada nota a una clave de diccionario.

### Reglas propuestas

El enunciado no fija criterios numéricos específicos, así que se proponen estas reglas para implementar el algoritmo:

- Cada nota debe estar entre **0,0 y 5,0**.
- El docente puede corregir **una nota registrada**, seleccionando el número del estudiante, si hubo un error de digitación.
- Se considera aprobado al estudiante con nota **mayor o igual a 3,0**.

### Lógica de solución

1. Solicitar la cantidad de estudiantes.
2. Registrar cada nota en una lista y validar su rango.
3. Preguntar si el docente desea corregir una nota; si responde que sí, validar la posición y la nueva calificación.
4. Calcular el promedio mediante `sum(notas) / len(notas)`.
5. Obtener la nota mayor y menor con `max()` y `min()`.
6. Recorrer las notas para contar aprobados y reprobados.
7. Mostrar los resultados consolidados.

**Archivo:** `gestion_calificaciones.py`.

### Ejemplo ilustrativo (no es evidencia de ejecución)

Para las notas `[3.5, 2.0, 4.2, 3.0, 4.5]`, si se corrige la segunda nota de 2.0 a 3.2, la lista queda `[3.5, 3.2, 4.2, 3.0, 4.5]`. Su promedio es **3,68**, la mayor es **4,5**, la menor **3,0** y hay **5 aprobados y 0 reprobados**.

### Conclusión de la Parte 2

Una lista es suficiente para registrar y corregir calificaciones en un problema académico sencillo. El algoritmo emplea ciclos, condicionales y operaciones básicas para producir resultados consolidados y mantiene los datos en el orden de ingreso.

## Evidencias de ejecución

- **Parte 1:** agregar en la carpeta `evidencias/` una captura de la consola con los tiempos reales de `comparacion_rendimiento.py`.
- **Parte 2:** ejecutar `gestion_calificaciones.py` y guardar una captura real donde se vean las notas, una corrección y los resultados.

> Las capturas deben corresponder a ejecuciones reales. Este informe no incluye capturas fabricadas.

## Organización del repositorio

```text
taller-1-listas-arrays/
├── README.md
├── rendimiento_listas.py
├── rendimiento_numpy.py
├── comparacion_rendimiento.py
├── gestion_calificaciones.py
└── evidencias/
```

## Instrucciones para ejecutar

1. Instalar NumPy con `python -m pip install numpy`.
2. Ejecutar `python comparacion_rendimiento.py` para comparar los tiempos.
3. Ejecutar `python gestion_calificaciones.py` para probar el registro de notas.
4. Subir los archivos y las evidencias al repositorio público de GitHub.
