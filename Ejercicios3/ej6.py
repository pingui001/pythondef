tareas = []

def agregar_tarea():
    nombre = input("Ingresa la descripción de la tarea: ")
    tarea = {"nombre": nombre, "completado": False}
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def ver_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✅ Completada" if tarea["completado"] else "❌ Pendiente"
        print(f"{i + 1}. {tarea['nombre']} - {estado}")
    print()

def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a marcar como completada: "))
        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completado"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def menu():
    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()
