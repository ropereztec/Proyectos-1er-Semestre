
listaPadre = []

def mostrarjuegos(): #Convierte de archivo a lista
    listaPadre.clear()
    global lista
    archivo = open("Games.txt", "r")
    for linea in archivo.readlines():
        linea = linea.rstrip()
        listaHija = [str(i) for i in linea.split(",")]
        listaPadre.append(listaHija)
    archivo.close()
mostrarjuegos()
def muestra(): #Muestra los juegos
    lista = []
    question = int(input("¿Que rango de juegos desea imprimir \n1. A - E \n2. F - K \n3. L - P \n4. Q - V \n5. W - Z \n"))
    if question == 1:
        lista = ["A", "B", "C", "D", "E"]
    elif question == 2:
        lista = ["F", "G", "H", "I", "J", "K"]
    elif question == 3:
        lista = ["L", "M", "N", "O", "P"]
    elif question == 4:
        lista = ["Q", "R", "S", "T", "U", "V"]
    elif question == 5:
        lista = ["W", "X", "Y", "Z"]
    for l in lista:
        for v in listaPadre:
            cont = 0
            for i in v:
                if cont == 0:
                    cont +=1
                    continue
                elif cont == 1:
                    cont +=1
                    if i[0] == l:
                        print(i)
                else:
                    break


def modificar(): #Modifica los juegos
    console = input("De que consola es el juego que desea modificar: ")
    game = input("Ingrese el nombre del juego que desea modificar: ")
    reseña = input("Ingrese la reseña del juego: ")
    puntaje = str(input("Ingrese el puntaje del juego: "))
    for i in listaPadre:
        if i[0] == console and i[1] == game and i[2] == reseña and i[3] == puntaje:
            i[3] = str(input("Ingrese el nuevo puntaje del juego: "))
    archivos()

def archivos(): #esta función se encarga de editar el archivo
    archivo = open("Games.txt", "w")
    for p in listaPadre:
        archivo.write(p[0] + "," + p[1] + "," + p[2] + "," + p[3] + "\n") #Este metodo permite que no se escriba en el archivo con comillas
    archivo.close()
    mostrarjuegos()

def rep1():
    question = int(input("De que consola desea ver los juegos \n1. PS4 \n2. Xbox One \n3. Nintendo Switch \n4. PC \n"))
    if question == 1:
        for i in listaPadre:
            if i[0] == "PS4":
                print(i[1])
    elif question == 2:
        for i in listaPadre:
            if i[0] == "XONE":
                print(i[1])
    elif question == 3:
        for i in listaPadre:
            if i[0] == "NS":
                print(i[1])
    elif question == 4:
        for i in listaPadre:
            if i[0] == "PC":
                print(i[1])
    else:
        print("No a ingresado un código correcto")


def rep2():
    question = int(input("1 > Great \n2 > Good \n3 > Superb \n4 > Fair \n5 > Mediocre \n"))
    if question == 1:
        for i in listaPadre:
            if i[2] == "Great":
                print(i[1])
    elif question == 2:
        for i in listaPadre:
            if i[2] == "Good":
                print(i[1])
    elif question == 3:
        for i in listaPadre:
            if i[2] == "Superb":
                print(i[1])
    elif question == 4:
        for i in listaPadre:
            if i[2] == "Fair":
                print(i[1])
    elif question == 5:
        for i in listaPadre:
            if i[2] == "Mediocre":
                print(i[1])
    else:
        print("No a ingresado un código correcto")

def rep3():
    cont = 0
    question = int(input("1 > 0 - 1 \n2 > 2 - 4 \n3 > 5 - 6 \n4 > 7 - 8 \n5 > 9 - 10 \n"))
    if question == 1:
        for i in listaPadre:
            if int(i[3]) >= 0 and int(i[3]) <= 1:
                cont +=1
    elif question == 2:
        for i in listaPadre:
            if int(i[3]) >= 2 and int(i[3]) <= 4:
                cont +=1
    elif question == 3:
        for i in listaPadre:
            if int(i[3]) >= 5 and int(i[3]) <= 6:
                cont +=1
    elif question == 4:
        for i in listaPadre:
            if int(i[3]) >= 7 and int(i[3]) <= 8:
                cont +=1
    elif question == 5:
        for i in listaPadre:
            if int(i[3]) >= 9 and int(i[3]) <= 0:
                cont +=1
    else:
        print("No a ingresado un código correcto")
    mul = cont * 100 / len(listaPadre)
    print("El porcentaje de juegos que tiene ese puntaje es de: " + str(mul) + "%")

def reportes():
    print("Reportes")
    question = int(input("1 > Reporte de juegos por consola \n2 > Cantidad de juegos por reseña \n3 > Porcentaje de juegos por Puntaje\n"))
    if question == 1:
        rep1()
    elif question == 2:
        print("Cantidad de juegos por reseña")
        rep2()
    elif question == 3:
        print("Porcentaje de juegos por Puntaje")
        rep3()

def menu(): #Menú principal
    while True:
        print("Menú")
        print("1 > Mostar Juegos \n2 > Modificar Juegos \n3 > Reportes \n4 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("Bienvenido a Mostrar Juegos")
            muestra()
        elif opcionSelec == 2:
            print("¡Bienvenido a modificar!")
            modificar()
        elif opcionSelec == 3:
            print("¡Bienvenido a Reportes!")
            reportes()
        elif opcionSelec == 4:
            print("¡Hasta luego!")
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()