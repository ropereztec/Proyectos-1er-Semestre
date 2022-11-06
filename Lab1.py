from ast import Break
from datetime import datetime
##############################################################################################################################
#LISTAS OBLIGATORIAS, #LISTAS OBLIGATORIAS, #LISTAS OBLIGATORIAS, #LISTAS OBLIGATORIAS, #LISTAS OBLIGATORIAS, #LISTAS OBLIGATORIAS
Personas = []
Productos = []
Ver_Cedulas = []
edad_g=[]
Carrito = []
######################################################################################################################
#DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS, #DATOS QUEMADOS
roos = [] 
roos.append(208400858) 
roos.append("Roosevelt")
roos.append(19) 
Personas.append(roos)
Ver_Cedulas.append(208400858)
productos_= []
productos_.append("Coca Cola")
productos_.append(1300)
productos_.append("31/12/2022")
Productos.append(productos_)

#########################################################################################################################

def registro_de_personas():
    personas_ = []
    print("Favor indique su cédula")
    cedula = int(input())
    personas_.append(cedula)
    Ver_Cedulas.append(cedula)
    print("Favor indique su nombre")
    nombre = input()
    personas_.append(nombre)
    print("Favor indique su edad")
    edad = int(input())
    edad_g.append(edad)
    personas_.append(edad)
    Personas.append(personas_)
    print(Personas)
##########################################################################################################

def registro_de_productos():
    productos_ = []
    print("Favor indique el nombre del producto")
    nombre_pro= input()
    productos_.append(nombre_pro)
    print("Favor indique el precio del producto")
    precio = int(input())
    
    productos_.append(precio)
    print("Favor indique la fecha de vencimiento del producto")
    while True:
        fecha_str = input('Ingrese fecha "aaaa/mm/dd"...: ')
        try:
            fecha = datetime.strptime(fecha_str, '%Y/%m/%d').strftime('%d/%m/%Y')
            print("La fecha de vencimiento es: ")
            print(str(fecha))
            productos_.append(fecha)
        except ValueError:
            print("\n No ha ingresado una fecha correcta...")
        else:
            break
    Productos.append(productos_)
    print(Productos)
##########################################################################################################

def busqueda_y_compra_de_productos():
    print("Favor ingrese su cédula")
    cont = 1
    i = 1
    cedula = int(input())
    Listadeproductos= []
    Saldo = 0
    o = 0
    carritoxpersona=[]
    if cedula in Ver_Cedulas:
        print("\nEstos son los productos disponibles")
        for x in Productos:
            print(cont,".", x[0],"/", "Fecha de Vencimiento: ", x[2])
            while cont <= i:
                Listadeproductos_hija=[]
                Listadeproductos_hija.append(cont)
                Listadeproductos_hija.append(x[0])
                Listadeproductos_hija.append(x[1])
                Listadeproductos_hija.append(x[2])
                Listadeproductos.append(Listadeproductos_hija)
                cont = cont + 1
            i = i + 1
        print(0, ".", "No comprar más")
        opcionSelec = int(input("Seleccione el productos que va a comprar: "))
        if opcionSelec == 0:
            quit
        while o < 1000:
            o = o + 1
            if opcionSelec == o:
                for l in Listadeproductos:
                    if l[0] == o:
                        Cantidad= int(input("Cuantos elementos de este producto desea comprar: "))
                        Saldo= Saldo + Cantidad * l[2]
                        print("Su saldo actual es: ", Saldo)
                        for p in Personas:
                            if p[0]== cedula:
                                if p[2] < 30:
                                    Descuento = Saldo * 5 / 100
                                    Saldo = Saldo - Descuento
                                    carritoxpersona.append(p[1])
                                    carritoxpersona.append(Saldo)
                                    carritoxpersona.append(l[1])
                                    carritoxpersona.append(l[3])
                                    break
                                else:
                                    p[2] >= 30
                                    Descuento = Saldo * 10 / 100
                                    Saldo = Saldo - Descuento
                                    carritoxpersona.append(p[1])
                                    carritoxpersona.append(Saldo)
                                    carritoxpersona.append(l[1])
                                    carritoxpersona.append(l[3])
                                    break
                        print("Su saldo con descuento es: ", Saldo)
                        Carrito.append(carritoxpersona)
                        
                        break
                    else:
                        continue
    if not cedula in Ver_Cedulas:
        print("Favor ingresar un número de cédula válido o registrese")

################################################################################

def menúreportes():
    for l in Carrito:
        print (l)
        now = datetime.now()
        fecha_dt = datetime.strptime(l[3], '%d/%m/%Y')
        if fecha_dt < now:
            print("Hay productos vencidos")
        elif fecha_dt > now:
            print("No hay productos vencidos")

###############################################################################


def menu():
    while True:
        print("Menú")
        print("1 > Registros de Personas \n2 > Registro de Productos \n3 > Búsqueda y compra de Productos \n4 > Reportes \n5 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("Registros de Personas")
            registro_de_personas()
        elif opcionSelec == 2:
            print("Registro de Productos")
            registro_de_productos()
        elif opcionSelec == 3:
            print("Búsqueda y compra de Productos")
            busqueda_y_compra_de_productos()
        elif opcionSelec == 4:
            print("Reportes")
            menúreportes()
        elif opcionSelec == 5:
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()