from tabulate import tabulate
from random import randint
from colorama import Fore, Back, Style
from termcolor import colored
import datetime

ejesocupados = []

ocupado = []

matriz = []

Personas = [{"Nombre": "Roosevelt", "Cedula": 208400858, "Genero": "Masculino", "Asientos": [], "Valor a Pagar": 0}]


def funcion_matriz():
    for i in range(8):
        matriz.append([])
        for k in range(9):
            matriz[i].append("             ")


p = 1
while p == 1:
    funcion_matriz()
    p += 1

cont = 1


def salas_de_cine():
    global cont
    conta_x = 0
    conta_y = 0
    listaletra = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    listanum = ["8", "7", "6", "5", "4", "3", "2", "1"]
    for k in listanum:
        for v in listaletra:
            matriz[conta_y][conta_x] = k + v
            conta_x += 1
            if conta_x == 9:
                conta_y += 1
                conta_x = 0

    for fila in range(len(matriz)):
        for colum in range(len(matriz[fila])):
            for o in ocupado:
                if o == matriz[fila][colum]:
                    matriz[fila][colum] = Fore.RED + matriz[fila][colum] + Fore.RESET


    NumFila = 0
    NumColumna = 0
    if cont == 1:
        for i in range(25):
            while True:
                NumColumna = randint(0, 8)
                NumFila = randint(0, 7)
                num = [NumColumna, NumFila]
                if num not in ejesocupados:
                    if matriz[NumFila][NumColumna] in ocupado:
                        return
                    else:
                        ocupado.append(matriz[NumFila][NumColumna])
                        matriz[NumFila][NumColumna] = Fore.RED + matriz[NumFila][NumColumna] + Fore.RESET
                        ejesocupados.append(num)
                        break
                else:
                    i -= 1
    cont += 1
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
    for i in Personas:
        if i["Cedula"] == question and i["Asientos"] == []:
            verificacion = True
            break
        else:
            verificacion = False


#####################################################COMPRAS######################################################################################################################

def com():
    if len(i["Asientos"]) < 5:
        question2 = str(input("Ingrese el asiento que desea: "))
        if question2 in ocupado:
            print("El asiento esta ocupado")
        else:
            ocupado.append(question2)
            i["Asientos"].append(question2)
            print("Asiento comprado")
            print("Asientos comprados por", i["Nombre"])
            cont = 0
            conta_x = 0
            conta_y = 0
            for k in matriz:
                for v in k:
                    if v == question2:
                        matriz[conta_y][conta_x] = Fore.BLUE + matriz[conta_y][conta_x] + Fore.RESET
                        break
                    else:
                        conta_x += 1
                if conta_x == 9:
                    conta_y += 1
                    conta_x = 0
            if conta_y < 4:
                i["Valor a Pagar"] += 3000
            elif conta_y >= 4:
                i["Valor a Pagar"] += 5000
        print(tabulate(matriz))
        question3 = str(input("¿Desea comprar otro asiento? \n1< Si \n2< No \n"))
        if question3 == "1":
            com()
        elif question3 == "2":
            i["Fecha"] = datetime.datetime.now()
            print("Valor a pagar: ", i["Valor a Pagar"])
            print("¡Gracias por su compra!")
            salas_de_cine()
            # Aqui se va al menu
    elif len(i["Asientos"]) == 5:
        i["Fecha"] = datetime.datetime.now()
        print("Ha comprado el máximo de asientos")
        # Aqui se va al menu


def compras():
    global question
    question = int(input("Ingrese su cedula: "))
    verificaciondeexistencia()
    if verificacion == True:
        print("Bienvenido", i["Nombre"])
        print(tabulate(matriz))
        com()
    else:
        print("Error, no se encuentra registrado o ya ha comprado los asientos")



#########################################REPORTES###################################################################################################################################
def reporte1():
    hombres = 0
    mujeres = 0
    for i in Personas:
        if len(i["Asientos"]) > 0:
            if i["Genero"] == "Masculino":
                hombres += 1
            elif i["Genero"] == "Femenino":
                mujeres += 1
    print("Hombres: ", hombres)
    print("Mujeres: ", mujeres)


def reporte2():
    print(ocupado)
    print(tabulate(matriz))


def reporte3():
    cont = 72
    ocupados = len(ocupado)
    resta = cont - ocupados
    mul = resta * 100 / 72
    print("Porcentaje de asientos disponibles: ", mul, "%")


def reporte4():
    question1 = int(input("Ingrese su cedula: "))
    for p in Personas:
        if p["Cedula"] == question1:
            print("Nombre: ", p["Nombre"])
            print("Cedula: ", p["Cedula"])
            print("Genero: ", p["Genero"])
            print("Asientos: ", p["Asientos"])
            print("Valor a pagar: ", p["Valor a Pagar"])
            print("Fecha: ", p["Fecha"])
            break
        else:
            print("No se encuentra registrado")


def reporte5():
    may1 = 0
    may2 = 0
    for i in Personas:
        if i["Valor a Pagar"] > may1 and i["Valor a Pagar"] > may2:
            may1 = i["Valor a Pagar"]
        elif i["Valor a Pagar"] < may1 and i["Valor a Pagar"] > may2:
            may2 = i["Valor a Pagar"]
    for i in Personas:
        if i["Valor a Pagar"] == may1:
            print("La persona que mas ha gastado es: ", i["Nombre"])
            print("Nombre: ", i["Nombre"])
            print("Cedula: ", i["Cedula"])
            print("Genero: ", i["Genero"])
            print("Asientos: ", i["Asientos"])
            print("Valor a pagar: ", i["Valor a Pagar"])
            print("Fecha: ", i["Fecha"])
        elif i["Valor a Pagar"] == may2:
            print("La segunda persona que mas ha gastado es: ", i["Nombre"])
            print("Nombre: ", i["Nombre"])
            print("Cedula: ", i["Cedula"])
            print("Genero: ", i["Genero"])
            print("Asientos: ", i["Asientos"])
            print("Valor a pagar: ", i["Valor a Pagar"])
            print("Fecha: ", i["Fecha"])


def reportes():
    question1 = int(input(
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
        print("No ha ingresado una opción correcta")


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