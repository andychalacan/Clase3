#control
print("Bienvenido al menu digite el numeral que necesite")
print("1-Configuracion a Internet")
print("2-Dispositivos conectados")
print("3-Configuracion estandar")
print("4-Comando de Voz")
print("5-Recomendaciones de contenido")
print("6-Buscar actualizaciones")
print("7-Dispositivos de salida")
print("8-Seleccion de Perfiles")
print("9-Acerca del equipo")

opci=int(input("Digite la opcion que desee: "))

match opci:
    case (1):
        print("Desea configurar internet para este equipo")
    case (2):
        print("Verficando los dispositivos conectados")
    case (3):
        print("Configuraciones basicas del equipo")
    case (4):
        print("Activando el uso por comando de voz")
    case (5):
        print("Se recomendara contenido respecto a sus gustos mediante IA")
    case (6):
        print("Buscando actualizaciones del equipo...")
    case (7):
        print("Seleccione el dispositivo de salida que desea usar")
    case (8):
        print("Escoga el usuario que desea")
    case (9):
        print("Informacion acerca del equipo")
    case _:
        print("Opcion no valida")