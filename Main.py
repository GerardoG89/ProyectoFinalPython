#Proyecto final Happy burguer  

#Importacion de modulos
from mispaquetes import CC


def menu_principal():
    opcion = ""

    while opcion != "s":
        print("Bienvenidos a Happy Burguer \n")
        print("a. pedidos")
        print("b. clientes")
        print("c. menu")
        print("s. salir")

        opcion = input(" \n selecciona una opcion: \n")

        if opcion == "a":
            #print("elegiste pedidos")
            #se ejecuta el pedido
            Captura_Productos()
        elif opcion == "b":
            print("elegiste Clientes")
            CC.cliente()
        elif opcion == "c":
            print("elegiste el Menu")    
        elif opcion == "s":
            print("elegiste Salir")
        else:
            print("La opcion es invalida")
#Pide datos de los productos y los muestra
def Captura_Productos():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    unidades = int(input("Ingresa el numero de unidades a pedir: "))

#Se calcula el total del pedido
   # total_pedido = precio * unidades

    print("\n Datos del pedido \n")
    print("Tu producto es: ", nombre)
    print("El precio unitario es: ", precio)
    print("El total de unidades es: ", unidades)
    print("El total de pedido es: ", Calculo_total_pedido(precio,unidades))

def Calculo_total_pedido(uno,dos):
    return uno * dos


#Inicia la ejecucion del menu
menu_principal() 