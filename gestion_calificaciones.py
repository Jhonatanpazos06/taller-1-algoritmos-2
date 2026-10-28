
# Profe, aquí creé una lista para guardar las notas.
notas = []

# Profe, aquí solicité la cantidad de estudiantes.
cantidad = int(input("Ingrese la cantidad de estudiantes: "))

# Profe, aquí utilicé un ciclo for para registrar las notas.
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))

    # Profe, aquí validé que la nota esté entre 0 y 5.
    while nota < 0 or nota > 5:
        print("Error: la nota debe estar entre 0 y 5.")
        nota = float(input("Ingrese nuevamente la nota: "))

    # Profe, aquí agregué cada nota a la lista.
    notas.append(nota)

# Profe, aquí permití corregir una nota registrada.
if len(notas) > 0:
    print("Notas registradas:", notas)

    corregir = input("¿Desea corregir una nota? (si/no): ")

    if corregir.lower() == "si":
        posicion = int(input("Número del estudiante: "))

        if 1 <= posicion <= len(notas):
            nueva_nota = float(input("Ingrese la nueva nota: "))

            if 0 <= nueva_nota <= 5:
                notas[posicion - 1] = nueva_nota
                print("Nota corregida correctamente.")
            else:
                print("La nueva nota no es válida.")
        else:
            print("El estudiante no existe.")

    # Profe, aquí calculé el promedio de las notas.
    promedio = sum(notas) / len(notas)

    # Profe, aquí identifiqué la nota mayor y menor.
    mayor = max(notas)
    menor = min(notas)

    # Profe, aquí conté aprobados y reprobados.
    aprobados = 0
    reprobados = 0

    for nota in notas:
        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    # Profe, aquí mostré los resultados generales.
    print("\n--- RESULTADOS FINALES ---")
    print("Notas:", notas)
    print("Promedio:", round(promedio, 2))
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)

else:
    print("No se registraron estudiantes.")
