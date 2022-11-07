import math
import random
from tabulate import tabulate

sucias = []
limpias = []
obstaculos = []

ocupadas=[]
matriz = []
fil = 8
col = 8
def matriz__():
    for i in range(8):
        matriz.append([])
        for k in range(8):
            matriz[i].append("             ")
    for i in range(32):
        while True:
            x=random.randint(0,7)
            y=random.randint(0,7)
            cordenada = [x,y]
            if cordenada in ocupadas:
                continue
            matriz[x][y] = "Sucio"
            ocupadas.append(cordenada)
            sucias.append(cordenada)
            break
    for k in range(10):
        while True:
            x=random.randint(0,7)
            y=random.randint(0,7)
            cordenada = [x,y]
            if cordenada == [0,0]:
                continue
            if cordenada in ocupadas:
                continue
            ocupadas.append(cordenada)
            matriz[x][y] = "Obstaculo"
            obstaculos.append(cordenada)
            break
    for v in range(22):
        while True:
            x=random.randint(0,7)
            y=random.randint(0,7)
            cordenada = [x,y]
            if cordenada in ocupadas:
                continue
            ocupadas.append(cordenada)
            matriz[x][y] = "Limpio"
            limpias.append(cordenada)
            break
    print(tabulate(matriz))
matriz__()

robot_ =[0,0]
pos_reco = 0
pos_clean= 0
def robot(d):
    global pos_reco
    global pos_clean
    global robot_
    if d == "N":
        x_s = robot_[0] 
        y_s = robot_[1] - 1
        robot_ = [x_s, y_s]
        if y_s == -1:
            print("Este movimiento es invalido, debido a que se sale del limite")
            return
        if matriz[y_s][x_s ]== "Obstaculo":
            print("El robot no se puede mover debido a un obstaculo")
            print(tabulate(matriz))
        elif matriz[y_s][x_s]== "Sucio":
            question1 = int(input("Esta Casilla esta sucia, desea limpiarla? \n1- Si \n2- No \n"))
            if question1 == 1:
                limpiar()
                pos_reco += 1
                pos_clean +=1
                print(tabulate(matriz))
            else:
                return
        elif matriz[y_s][x_s]== "Limpio":
            print("Esta casilla esta limpia")
            print(tabulate(matriz))
            pos_reco +=1
    if d == "S":
        x_s = robot_[0]
        y_s = robot_[1] + 1
        robot_ = [x_s, y_s]
        if y_s == 8:
            print("Este movimiento es invalido, debido a que se sale del limite")
            return
        if matriz[y_s][x_s]== "Obstaculo":
            print("El robot no se puede mover debido a un obstaculo")
            print(tabulate(matriz))

        elif matriz[y_s][x_s]== "Sucio":
            question1 = int(input("Esta Casilla esta sucia, desea limpiarla? \n1- Si \n2- No \n"))
            if question1 == 1:
                limpiar()
                pos_reco += 1
                pos_clean +=1
                print(tabulate(matriz))
            else:
                return

        elif matriz[y_s][x_s]== "Limpio":
            print("Esta casilla esta limpia")
            pos_reco += 1
            print(tabulate(matriz))

    if d == "E":
        x_s = robot_[0] + 1
        y_s = robot_[1]
        robot_ = [x_s, y_s] 
        if x_s == 8:
            print("Este movimiento es invalido, debido a que se sale del limite")
            return
        if matriz[y_s][x_s]== "Obstaculo":
            print("El robot no se puede mover debido a un obstaculo")
            robot_ = [x_s - 1, y_s]
            print(tabulate(matriz))
        elif matriz[y_s][x_s]== "Sucio":
            question1 = int(input("Esta Casilla esta sucia, desea limpiarla? \n1- Si \n2- No \n"))
            if question1 == 1:
                limpiar()
                pos_reco += 1
                pos_clean +=1
                print(tabulate(matriz))
            else:
                return
        elif matriz[y_s][x_s]== "Limpio":
            print("Esta casilla esta limpia")
            print(tabulate(matriz))
            pos_reco += 1

    if d == "O":
        x_s = robot_[0] -1
        y_s = robot_[1] 
        robot_ = [x_s, y_s]
        if x_s == -1:
            print("Este movimiento es invalido, debido a que se sale del limite")
            return
        if matriz[y_s][x_s]== "Obstaculo":
            print("El robot no se puede mover debido a un obstaculo")
            print(tabulate(matriz))
        elif matriz[y_s][x_s]== "Limpio":
            print("Esta casilla esta limpia")
            pos_reco += 1
            print(tabulate(matriz))
        elif matriz[y_s][x_s]== "Sucio":
            question1 = int(input("Esta Casilla esta sucia, desea limpiarla? \n1- Si \n2- No \n"))
            if question1 == 1:
                limpiar()
                pos_reco += 1
                pos_clean +=1
                print(tabulate(matriz))
            else:
                pos_reco += 1
                return

def limpiar():
    global robot
    x = robot_[0]
    y = robot_[1]

    if matriz[y][x] =="Sucio":
        matriz[y][x] = "Limpio"
        print("La casilla ya se limpió")
    elif matriz[y][x] =="Limpio":
        print("La casilla ya esta limpia")
    elif matriz[y][x] =="Obstaculo":
        print("No se puede mover, hay un obstaculo")


def obtenerestado():
    question2= int(input("Seleccione el punto en el eje x que desea conocer: "))
    question1= int(input("Seleccione el punto en el eje y que desea conocer: "))
    if matriz[question1][question2] == "Sucio":
        print("Esa casilla se encuentra sucia")
    elif matriz[question1][question2] == "Limpia":
        print("Esa casilla se encuentra Limpia")
    elif matriz[question1][question2] == "Obstaculo":
        print("Esa casilla tiene un obstaculo")

def verificacionobstaculo():
    question2= int(input("Seleccione el punto en el eje x que desea conocer: "))
    question1= int(input("Seleccione el punto en el eje y que desea conocer: "))
    if matriz[question1][question2] == "Obstaculo":
        print("Hay un obstaculo")
    else:
        print("No hay obstaculo")


def porcent_suciedad():
    suciedad = 0
    for i in matriz:
        for k in i:
            if k == "Sucio":
                suciedad +=1
            else:
                continue
    math = suciedad / 64
    global math2 
    math2 = math * 100
    print("El porcentaje de suciedad en el salon es:", math2)


def menu():
    while True:
        print("Menú")
        print("La Poscición del robot es: ", robot_)

        print("1 > Mover Robot \n2 > Obtener Estado \n3 > Verificación de Obstaculos \n4 > Porcentaje de Suciedad \n5 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))
        global math
        global math2
        porcent_suciedad()






        if math2 == 0.0:
            info = open("info.txt", "a")
            info.write("Espacios limpios" "\n")
            info.write(str(limpias))
            info.write("\n""Espacios sucios" "\n")
            info.write(str(sucias))
            info.write("\n""Espacios con obstaculos" "\n")
            info.write(str(obstaculos))
            info.write("\n" "Espacios Recorridos" "\n")
            info.write(str(pos_reco))
            quit()

        else:
            if opcionSelec == 1:
                print("Jugar")
                Quest = int(input("Elija la poscición a que desea moverse: \n1- N \n2- S \n3- E \n4- O "))
                if Quest == 1:
                    robot("N")
                elif Quest==2:
                    robot("S")
                elif Quest==3:
                    robot("E")
                elif Quest==4:
                    robot("O")
                
            elif opcionSelec == 2:
                print("Obtener Estado")
                obtenerestado()
            elif opcionSelec == 3:
                print("Verificación de Obstaculo")
                verificacionobstaculo()
            elif opcionSelec == 4:
                print("Porcentaje de Suciedad")
                porcent_suciedad()
            elif opcionSelec == 5:
                quit()
            else:
                input("No a ingresado un código correcto. Pulse ENTER para continuar.")
        


menu()