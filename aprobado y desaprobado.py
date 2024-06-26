#Porcentaje de estudiantes aprobadas y desaprobados



def notas(numero):
   sumapr=0  
   luego=0
   prueba=0

   total=int(input("Ingresa el numero de notas a ingresar"))
   while sumapr < numero:
    numero=int(input(f"Ingrese la nota numero {sumapr+1}: "))
    luego += numero
    print("La nota supera o es igual a 7")
    aprova = input("si o no")
    if aprova == "si":
        prueba += 1
    sumapr += 1
    print(f"El numero total de aprobado es de: {prueba}")
    print(f"El numero total de desaprobados es de: {sumapr}")


def main ():
 opcion=0  
 while opcion!=3:
     print("--------MENU------")
     print("1)Agregar Notas de estudiantes")
     print("2)Comprobar aprobados y desaprovados")
     print("3)Salir")
     opcion=int(input("Ingrese su opcion deseada: "))
     if opcion== 1:
       numero=notas(1)
 print("Gracias por usar este servicio")

main()

