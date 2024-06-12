#bucle
no_empleados = int(input("Ingrese el número de empleados: "))
no_profesores = 0
for i in range (no_empleados):
    print(f"Empleado No. {i+1}")
    sueldo = float(input("Por favor ingrese el sueldo: "))
    no_horas = int(input("Ingrese el número de horas trabajadas: "))
    profesor = input("¿Es profesor? Sí o no: ")
    if profesor == 'Si' or profesor == 'si':
        no_profesores +=1

        print(f"Su sueldo es de: ${sueldo}")
        print(f"Horas trabajadas: {no_horas}")
        print(f"{profesor} es profesor.")
    else:
      print(f"Su sueldo es de: ${sueldo}")
      print(f"Horas trabajadas: {no_horas}")
      print(f"{profesor} es profesor.")

print("El número total de profesores es de: ", no_profesores)