from tabulate import tabulate
from random import randint
from colorama import Fore, Back, Style
from termcolor import colored
import datetime

ejesocupados = []

ocupado = []

matriz = []

Personas = [{"Nombre": "Roosevelt", "Cedula": 208400858, "Genero": "Masculino", "Asientos": [], "Valor a Pagar": 0}]


def funcion_matriz(): #Esta funcion crea la matriz
    for i in range(8):
        matriz.append([])
        for k in range(9):
            matriz[i].append("             ")


p = 1
while p == 1: #Aqui se cre la matriz automaticamente
    funcion_matriz()
    p += 1

cont = 1


def salas_de_cine(): #Esta función es la que se encarga de agregar los asientos a la matriz y sus colores 
    global cont
    conta_x = 0 #Esta variable es la que se encarga de contar los datos en las filas
    conta_y = 0 #Esta variable es la que se encarga de contar las filas
    listaletra = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] #Esta lista es la que se encarga de agregar las letras a la matriz
    listanum = ["8", "7", "6", "5", "4", "3", "2", "1"] #Esta lista es la que se encarga de agregar los numeros a la matriz
    for k in listanum: #Este for es el que se encarga de agregar los numeros a la matriz, tambien es la encargada de resetear la matriz una vez un usuario haya comprado uno o mas asientos
        for v in listaletra: #este for es el que se encarga de agregar las letras a la matriz
            matriz[conta_y][conta_x] = k + v #Aqui se le agrega a la matriz los numeros y las letras
            conta_x += 1 #Aqui verficamos en que espacio de la fila nos encontramos
            if conta_x == 9: #Aqui verificamos si ya hemos llegado al final de la fila
                conta_y += 1 #Aqui verificamos en que fila nos encontramos
                conta_x = 0 #Aquí reiniciamos la variable que nos ayuda a saber en que espacio de la fila nos encontramos

    for fila in range(len(matriz)): 
        for colum in range(len(matriz[fila])):
            for o in ocupado: #Aqui recores la lista de asientos ocupados
                if o == matriz[fila][colum]: #Si la matriz fue reseteada y el asiento que se encuentra en la lista de asientos ocupados es igual a la matriz, se le agrega el color rojo
                    matriz[fila][colum] = Fore.RED + matriz[fila][colum] + Fore.RESET #Aqui se le agrega el color rojo a los asientos ocupados


    NumFila = 0 #Esta variable es la que se encarga de contar las filas
    NumColumna = 0 #Esta variable es la que se encarga de contar los datos en las filas
    if cont == 1:
        for i in range(25): #Este for se encarga de generar los asientos ocupados aleatoriamente
            while True:
                NumColumna = randint(0, 8) #Aqui se genera un numero aleatorio para la columna
                NumFila = randint(0, 7) #Aqui se genera un numero aleatorio para la fila
                num = [NumColumna, NumFila] #Aqui se crea una lista con los numeros aleatorios
                if num not in ejesocupados: #Aqui se verifica si los numeros aleatorios ya se encuentran en la lista de asientos ocupados
                    if matriz[NumFila][NumColumna] in ocupado: #Aqui se verifica si el asiento ya se encuentra ocupado
                        return
                    else:
                        ocupado.append(matriz[NumFila][NumColumna]) #Aqui se agrega el asiento a la lista de asientos ocupados
                        matriz[NumFila][NumColumna] = Fore.RED + matriz[NumFila][NumColumna] + Fore.RESET #Aqui se le agrega el color rojo a los asientos ocupados
                        ejesocupados.append(num) #Aqui se agrega a la lista de ejes ocupados el eje que recien se creo
                        break
                else:
                    i -= 1 #Este contador es por ai algún numero que ya estaba en la lista de asientos ocupados se repite, se le resta uno al contador para que no se genere un asiento mas
    cont += 1 #Aqui se le suma uno al contador para que no se generen mas asientos ocupados aleatoriamente
    print("------------Pantalla -------------")
    print(tabulate(matriz))
    print("Precio de la fila 1 - 4: 5000 \nPrecio de la fila 5 - 8: 3000")

salas_de_cine() 
####################################################REGISTRO######################################################################################################################


def registro():
    persona = {}
    nombre = input("Ingrese su nombre: ")
    cedula = int(input("Ingrese su cedula: "))
    genero = input("Ingrese su genero \n1< Masculino \n2< Femenino \n")
    if genero == "1":
        genero = "Masculino"
    elif genero == "2":
        genero = "Femenino"
    else:
        print("No ha ingresado una opción correcta")
    persona["Nombre"] = nombre
    persona["Cedula"] = cedula
    persona["Genero"] = genero
    persona["Asientos"] = []
    persona["Valor a Pagar"] = 0
    Personas.append(persona)


def verificaciondeexistencia():
    global verificacion
    global i
    for i in Personas: #Aqui se recorre la lista de personas
        if i["Cedula"] == question and i["Asientos"] == []: #Aqui se verifica si la cedula ingresada por el usuario se encuentra en la lista de personas y si la lista de asientos esta vacia, esto es para que no se pueda comprar asientos si ya compraron anteriormente
            verificacion = True #Aqui se le asigna el valor True a la variable verificacion en caso de que la cedula ingresada por el usuario se encuentre en la lista de personas y si la lista de asientos esta vacia
            break #Aqui se rompe el ciclo for
        else:
            verificacion = False #Aqui se le asigna el valor False a la variable verificacion en caso de que la cedula ingresada por el usuario no se encuentre en la lista de personas o si la lista de asientos no esta vacia


#####################################################COMPRAS######################################################################################################################
def com():
    if len(i["Asientos"]) < 5:
        question = input("Ingrese el asiento que desea comprar: ") #Aqui se le pide al usuario que ingrese el asiento que desea comprar
        if question in ocupado: #Aqui se verifica si el asiento que ingreso el usuario se encuentra en la lista de asientos ocupados
            print("El asiento que ingreso se encuentra ocupado") #Aqui se verifica si el asiento que ingreso el usuario se encuentra ocupado
        else:
            conta_x = 0 #Esta variable es la que se encarga de contar los datos en las filas
            conta_y = 0 #Esta variable es la que se encarga de contar las filas
            for k in matriz: #Aqui se recorre la matriz
                for v in k: #Aqui se recorre las filas de la matriz
                    if question == v: #Aqui se verifica si el asiento que ingreso el usuario es igual a algun asiento disponible de la matriz
                        ocupado.append(question) #Aqui se agrega el asiento a la lista de asientos ocupados
                        i["Asientos"].append(question) #Aqui se agrega el asiento a la lista de asientos de la persona que lo compro
                        matriz[conta_y][conta_x] = Fore.BLUE + matriz[conta_y][conta_x] + Fore.RESET #Aqui se le agrega el color azul a los asientos comprados
                        break #Aqui se rompe el ciclo for
                    else:
                        conta_x += 1 #Aqui se le suma uno a la variable conta_x para que se pueda contar los datos en las filas
                    if conta_x == 9: #Aqui se verifica si la variable conta_x es igual a 9
                        conta_y += 1 #Aqui se le suma uno a la variable conta_y para que se pueda contar las filas
                        conta_x = 0 #Aqui se le asigna el valor 0 a la variable conta_x para que se pueda contar los datos en las filas
            if question in ocupado and question in i["Asientos"]: #Aqui se verifica si el asiento que ingreso el usuario se encuentra en la lista de asientos ocupados y si se encuentra en la lista de asientos de la persona que lo compro
                if question[0] == "8" or question[0] == "7" or question[0] == "6" or question[0] == "5": #Aqui se verifica si el asiento que ingreso el usuario se encuentra en la fila 5 - 8
                    i["Valor a Pagar"] += 3000 #Aqui se le suma 3000 al valor a pagar de la persona que compro el asiento
                    print("El asiento se ha comprado con exito")
                    print(tabulate(matriz))
                elif question[0] == "4" or question[0] == "3" or question[0] == "2" or question[0] == "1": #Aqui se verifica si el asiento que ingreso el usuario se encuentra en la fila 1 - 4
                    i["Valor a Pagar"] += 5000 #Aqui se le suma 5000 al valor a pagar de la persona que compro el asiento
                    print("El asiento se ha comprado con exito")
                    print(tabulate(matriz))
            else: #Aqui se verifica si el asiento que ingreso el usuario no se encuentra en la lista de asientos ocupados y si no se encuentra en la lista de asientos de la persona que lo compro
                print("El asiento que ingreso no existe") 
        question2 = input("Desea comprar otro asiento? \n1< Si \n2< No \n") #Aqui se le pregunta al usuario si desea comprar otro asiento
        if question2 == "1": #Aqui se verifica si el usuario ingreso 1
            com() #Aqui se llama a la funcion com que es la que se encarga de comprar los asientos
        elif question2 == "2": #Aqui se verifica si el usuario ingreso 2
            print("Gracias por su compra")
            print("El valor a pagar es: ", i["Valor a Pagar"]) #Aqui se imprime el valor a pagar de la persona que compro los asientos
            i["Fecha"] = datetime.datetime.now() #Aqui se le asigna la fecha y hora actual a la variable fecha de la persona que compro los asientos
            salas_de_cine() #Aqui se llama a la funcion salas_de_cine que es la que se encarga de mostrar el menu de salas de cine
            return 
    else:
        print("Ya ha comprado el maximo de asientos permitidos") #Aqui se imprime que la persona ya compro el maximo de asientos permitidos




def compras():
    global question
    question = int(input("Ingrese su cedula: ")) #Aqui se le pide al usuario que ingrese su cedula
    verificaciondeexistencia() #Aqui se verifica si la cedula ingresada se encuentra en la lista de personas
    if verificacion == True: #Aqui se verifica si la variable verificacion es igual a True
        print("Bienvenido", i["Nombre"]) #Aqui se le da la bienvenida al usuario
        print(tabulate(matriz)) #Aqui se muestra la matriz con los asientos
        com() #Aqui se llama a la funcion com
    else:
        print("Error, no se encuentra registrado o ya ha comprado los asientos") #Aqui se le indica al usuario que no se encuentra registrado o que ya ha comprado los asientos, esto se hace en caso de que la variable verificacion sea igual a False



#########################################REPORTES###################################################################################################################################
def reporte1():
    hombres = 0 #Esta variable es la que se encarga de contar la cantidad de hombres
    mujeres = 0 #Esta variable es la que se encarga de contar la cantidad de mujeres
    for i in Personas: #Aqui se recorre la lista de personas
        if len(i["Asientos"]) > 0: #Aqui se verifica si la cantidad de asientos de la persona es mayor a 0
            if i["Genero"] == "Masculino": #Aqui se verifica si el genero de la persona es igual a Masculino
                hombres += 1 #Aqui se le suma uno a la variable hombres
            elif i["Genero"] == "Femenino": #Aqui se verifica si el genero de la persona es igual a Femenino
                mujeres += 1 #Aqui se le suma uno a la variable mujeres
    print("Hombres: ", hombres)
    print("Mujeres: ", mujeres)


def reporte2():
    print(ocupado) #Aqui se imprime la lista de asientos ocupados
    print(tabulate(matriz)) #Aqui se imprime la matriz con los asientos


def reporte3():
    cont = 72 #Esta variable es la que se encarga de contar la cantidad de asientos totales
    ocupados = len(ocupado) #Esta variable es la que se encarga de contar la cantidad de asientos que se han vendido
    resta = cont - ocupados #Esta variable es la que se encarga de restar la cantidad de asientos totales menos la cantidad de asientos que se han vendido
    mul = resta * 100 / 72 #Esta variable es la que se encarga de multiplicar la resta entre 100 y dividirlo entre 72
    print("Porcentaje de asientos disponibles: ", mul, "%") #Aqui se imprime el porcentaje de asientos disponibles


def reporte4():
    question1 = int(input("Ingrese su cedula: ")) #Aqui se le pide al usuario que ingrese su cedula
    for p in Personas: #Aqui se recorre la lista de personas
        if p["Cedula"] == question1: #Aqui se verifica si la cedula ingresada por el usuario es igual a la cedula de la persona
            print("Nombre: ", p["Nombre"]) #Aqui se imprime el nombre de la persona
            print("Cedula: ", p["Cedula"])  #Aqui se imprime la cedula de la persona
            print("Genero: ", p["Genero"]) #Aqui se imprime el genero de la persona
            print("Asientos: ", p["Asientos"]) #Aqui se imprime los asientos que compro la persona
            print("Valor a pagar: ", p["Valor a Pagar"]) #Aqui se imprime el valor a pagar de la persona
            print("Fecha: ", p["Fecha"]) #Aqui se imprime la fecha en la que la persona compro los asientos
            break
        else:
            print("No se encuentra registrado")


def reporte5():
    may1 = 0 #Esta variable es la que se encarga de contar la cantidad de asientos que compro la persona con mayor cantidad de asientos
    may2 = 0 #Esta variable es la que se encarga de contar la cantidad de asientos que compro la segunda persona con mayor cantidad de asientos
    for i in Personas: #Aqui se recorre la lista de personas
        if i["Valor a Pagar"] > may1 and i["Valor a Pagar"] > may2: #Aqui se verifica si el valor a pagar de la persona es mayor a la variable may1 y may2
            may1 = i["Valor a Pagar"] #Aqui se le asigna el valor a pagar de la persona a la variable may1
        elif i["Valor a Pagar"] < may1 and i["Valor a Pagar"] > may2: #Aqui se verifica si el valor a pagar de la persona es menor a la variable may1 y mayor a la variable may2
            may2 = i["Valor a Pagar"] #Aqui se le asigna el valor a pagar de la persona a la variable may2
        elif i["Valor a Pagar"] == may1 and i["Valor a Pagar"] == may2: #Aqui se verifica si el valor a pagar de la persona es igual a la variable may1 y may2
            may2 = i["Valor a Pagar"] #Aqui se le asigna el valor a pagar de la persona a la variable may2
    for i in Personas: #Aqui se recorre la lista de personas
        if i["Valor a Pagar"] == may1: #Aqui se verifica si el valor a pagar de la persona es igual a la variable may1
            print("La persona que mas ha gastado es: ", i["Nombre"]) #Aqui se imprime el nombre de la persona que mas ha gastado
            print("Cedula: ", i["Cedula"]) #Aqui se imprime la cedula de la persona que mas ha gastado
            print("Genero: ", i["Genero"]) #Aqui se imprime el genero de la persona que mas ha gastado
            print("Asientos: ", i["Asientos"]) #Aqui se imprime los asientos que compro la persona que mas ha gastado
            print("Valor a pagar: ", i["Valor a Pagar"]) #Aqui se imprime el valor a pagar de la persona que mas ha gastado
            print("Fecha: ", i["Fecha"]) #Aqui se imprime la fecha en la que la persona que mas ha gastado compro los asientos
        elif i["Valor a Pagar"] == may2: #Aqui se verifica si el valor a pagar de la persona es igual a la variable may2
            print("La segunda persona que mas ha gastado es: ", i["Nombre"]) #Aqui se imprime el nombre de la segunda persona que mas ha gastado
            print("Cedula: ", i["Cedula"]) #Aqui se imprime la cedula de la segunda persona que mas ha gastado
            print("Genero: ", i["Genero"]) #Aqui se imprime el genero de la segunda persona que mas ha gastado
            print("Asientos: ", i["Asientos"]) #Aqui se imprime los asientos que compro la segunda persona que mas ha gastado
            print("Valor a pagar: ", i["Valor a Pagar"]) #Aqui se imprime el valor a pagar de la segunda persona que mas ha gastado
            print("Fecha: ", i["Fecha"]) #Aqui se imprime la fecha en la que la segunda persona que mas ha gastado compro los asientos


def reportes():
    question1 = int(input( #Aqui se le pide al usuario que ingrese el numero del reporte que desea ver
        "Ingrese el código del reporte que desea ver \n1< Cantidad de Hombres y Mujeres que compraron entradas\n2< Espacios Ocuapdos\n3< Porcentaje de espacios Disponibles\n4< Imprimir información de Compra de una Persona\n5< Imprimir las personas que más compraron entradas\n"))
    if question1 == 1: 
        reporte1()
    elif question1 == 2:
        reporte2()
    elif question1 == 3:
        reporte3()
    elif question1 == 4:
        reporte4()
    elif question1 == 5:
        reporte5()
    else:
        print("No ha ingresado una opción correcta") #Aqui se le indica al usuario que no ha ingresado una opcion correcta


#####################################################MENU######################################################################################################################

def menu():
    while True:
        print("Menú")
        print("1 > Ver Salas de Cine \n2 > Registro de Personas \n3 > Comprar Boletos \n4 > Reportes \n5 > Salir ")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))

        if opcionSelec == 1:
            print("¡Ver Salas de Cine!")
            salas_de_cine()
        elif opcionSelec == 2:
            print("¡Registro de Personas!")
            registro()
        elif opcionSelec == 3:
            print("¡Comprar Boletos!")
            compras()
        elif opcionSelec == 4:
            print("¡Reportes!")
            reportes()
        elif opcionSelec == 5:
            print("¡Gracias por usar nuestro sistema!")
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")


menu()
