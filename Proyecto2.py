from tabulate import tabulate
from random import randint
from colorama import Fore, Back, Style
from termcolor import colored

ocupado = []

matriz=[]

Personas = []

def funcion_matriz():
    for i in range(8):
            matriz.append([])
            for k in range(9):
                matriz[i].append("             ")
p = 1
while p==1:
    funcion_matriz()
    p+=1


cont = 1
def salas_de_cine():
    global cont
    conta_x = 0
    conta_y = 0
    listaletra= ["A","B","C","D","E","F","G","H","I"]
    listanum= ["8","7","6","5","4","3","2","1"]
    if cont ==1:
        for k in listanum:
            for v in listaletra:
                matriz[conta_y][conta_x] = k + v
                conta_x +=1
                if conta_x == 9:
                    conta_y += 1
                    conta_x =0
    NumFila = 0
    NumColumna = 0
    for i in range(25):
        while True:
            NumColumna = randint(0,8)
            NumFila = randint(0,7)
            if matriz[NumFila][NumColumna] in ocupado:
                return
            else:
                ocupado.append(matriz[NumFila][NumColumna])
                matriz[NumFila][NumColumna] =colored(matriz[NumFila][NumColumna], 'red', attrs=['bold'])
                break
    cont +=1
    print(tabulate(matriz))

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
    Personas.append(persona)

def verificaciondeexistencia():
    global verificacion
    global i
    for i in Personas:
        if i["Cedula"] == question:
            verificacion = True
            break
        else:
            verificacion = False


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
            for k in matriz:
                for v in k:
                    if v == question2:
                        matriz[matriz.index(k)][k.index(v)] = colored(v, 'red', attrs=['bold'])
        print(tabulate(matriz))
        question3 = str(input("¿Desea comprar otro asiento? \n1< Si \n2< No \n"))
        if question3 == "1":
            com()
        elif question3 == "2":
            print("¡Gracias por su compra!")
            #Aqui se va al menu
    elif len(i["Asientos"]) == 5:
        print("Ha comprado el máximo de asientos")
        #Aqui se va al menu

def compras():
    global question
    question = int(input("Ingrese su cedula: "))
    verificaciondeexistencia()
    if verificacion == True:
        print("Bienvenido", i["Nombre"])
        print(tabulate(matriz))
        com()
    else:
        print("No se encuentra registrado")
        print("¿Desea registrarse?")
        print("1< Si \n2< No")
        question3 = int(input("Ingrese el código de la opción que desea: "))
        if question3 == 1:
            registro()
        elif question3 == 2:
            print("¡Gracias por su visita!")
            #Aqui se va al menu
        else:
            print("No ha ingresado una opción correcta")






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
            #
        elif opcionSelec==5:
            print("¡Gracias por usar nuestro sistema!")
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()
