#Conversion 


def validacorreocontra(usuario,contraseña):
    while (usuario!="Admin" or contraseña!="Secret*" ):
     print("----ERROR----")
     print("----Usuario o Contraseña INCORRECTOS----")
     usuario=input("Ingrese su usuario: ")
     contraseña=input("Ingrese su contraseña: ")
    
def caf(centigrado):
   centigrado=int(input("Ingrese su valor en Grados Celsius(C): "))
   faren=((centigrado*(9/5))+32)
   print(f"Su valor en Farenheit es de: {faren}")
   return faren

def cak(kelvin):
   kelvin=int(input("Ingrese su valor en Kelvin(K): "))
   ke=(kelvin+273.15)
   print(f"Su valor en Farenheit es de: {ke}")
   return ke
def main ():
   
    usuario=input("Ingrese su usuario: ")
    contraseña=input("Ingrese su contraseña: ")
    validacorreocontra(usuario,contraseña)
    opcion=0
    while opcion!=3:
      print("Bienvenido Admin")
      print("------MENU------")
      print("1)Grados Centigrafos(C) a Grados Farenheit(F)")
      print("2)Grados Kelvin (K) a Grados Centigrado(C)")
      print("3)Salir del programa")
      opcion=int(input("Ingrese la opcion deseada: ")) 
      if opcion==1:
        centigrado = caf(1)
      elif opcion==2:
         kelvin = cak(1)
         
    print("Gracias por usarnos")
main ()