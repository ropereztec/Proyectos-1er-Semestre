import random

Personas = []

def reportes2(): #acá se generan todas las posibles tablas de posciciones 
    puntaje1 = {"Nombre": "", "Puntos": 0}
    puntaje2 = {"Nombre": "", "Puntos": 0}
    puntaje3 = {"Nombre": "", "Puntos": 0}
    cont = 1
    for p in Personas:
        if cont == 1:
            puntaje1["Nombre"] = p["Nombre"]
            puntaje1["Puntos"] = p["Puntos"]
            cont +=1
        elif cont == 2:
            puntaje2["Nombre"] = p["Nombre"]
            puntaje2["Puntos"] = p["Puntos"]
            cont +=1
        elif cont ==3:
            puntaje3["Nombre"] = p["Nombre"]
            puntaje3["Puntos"] = p["Puntos"]
    if puntaje1["Puntos"] > puntaje2["Puntos"] and puntaje2["Puntos"] > puntaje3["Puntos"]: #Primera posibilidad del resultado del juego
        print("Tabla de posición")
        print("1.", puntaje1["Nombre"])
        print("2.", puntaje2["Nombre"])
        print("3.", puntaje3["Nombre"])

    elif puntaje1["Puntos"] > puntaje2["Puntos"] and puntaje2["Puntos"] < puntaje3["Puntos"]: #Segunda posibilidad del resultado del juego
        print("1.", puntaje1["Nombre"])
        print("2.", puntaje3["Nombre"])
        print("3.", puntaje2["Nombre"])

    elif puntaje1["Puntos"] < puntaje2["Puntos"] and puntaje2["Puntos"] > puntaje3["Puntos"]: 
        if puntaje1["Puntos"] > puntaje3["Puntos"]: #Tercera posibilidad del resultado del juego
            print("1.", puntaje2["Nombre"])
            print("2.", puntaje1["Nombre"])
            print("3.", puntaje3["Nombre"])
        elif puntaje1["Puntos"] < puntaje3["Puntos"]: #Cuarta posibilidad del resultado del juego
            print("1.", puntaje2["Nombre"])
            print("2.", puntaje3["Nombre"])
            print("3.", puntaje1["Nombre"])
        
    elif puntaje1["Puntos"] > puntaje2["Puntos"] and puntaje2["Puntos"] < puntaje3["Puntos"]: 
        if puntaje1["Puntos"] > puntaje3["Puntos"]: #Tercera posibilidad del resultado del juego
            print("1.", puntaje1["Nombre"])
            print("2.", puntaje3["Nombre"])
            print("3.", puntaje2["Nombre"])
        elif puntaje1["Puntos"] < puntaje3["Puntos"]: #Cuarta posibilidad del resultado del juego
            print("1.", puntaje3["Nombre"])
            print("2.", puntaje1["Nombre"])
            print("3.", puntaje2["Nombre"])

    elif puntaje1["Puntos"] < puntaje2["Puntos"] and puntaje2["Puntos"] < puntaje3["Puntos"]:  #Quinta posibilidad del resultado del juego
        print("1.", puntaje3["Nombre"])
        print("2.", puntaje2["Nombre"])
        print("3.", puntaje1["Nombre"])

    elif puntaje1["Puntos"] > puntaje2["Puntos"] and puntaje2["Puntos"] == puntaje3["Puntos"]: #Sexta posibilidad del resultado del juego
        cont = 1
        palyer2 = 0
        player3 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                continue
            elif cont ==2:
                player2= p["Estante 3"]
                cont +=1
            elif cont ==3:
                player3 = p["Estante 3"]
            if player2 > player3:
                print("1. ", puntaje1["Nombre"])
                print("2. ", puntaje2["Nombre"])
                print("3. ", puntaje3["Nombre"])
            elif player2 < player3:
                print("1. ", puntaje1["Nombre"])
                print("2. ", puntaje3["Nombre"])
                print("3. ", puntaje2["Nombre"])

    elif puntaje1["Puntos"] < puntaje2["Puntos"] and puntaje2["Puntos"] == puntaje3["Puntos"]: #Septima posibilidad del resultado del juego
        cont = 1
        palyer2 = 0
        player3 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                continue
            elif cont ==2:
                player2= p["Estante 3"]
                cont +=1
            elif cont ==3:
                player3 = p["Estante 3"]
            if player2 > player3:
                print("1. ", puntaje2["Nombre"])
                print("2. ", puntaje3["Nombre"])
                print("3. ", puntaje1["Nombre"])
            elif player2 < player3:
                print("1. ", puntaje3["Nombre"])
                print("2. ", puntaje2["Nombre"])
                print("3. ", puntaje1["Nombre"])

    elif puntaje1["Puntos"] == puntaje2["Puntos"] and puntaje2["Puntos"] < puntaje3["Puntos"]: #Octava posibilidad del resultado del juego
        cont = 1
        palyer1 = 0
        player2 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                player1= p["Estante 3"]
            elif cont ==2:
                player2= p["Estante 3"]
                cont +=1
            elif cont ==3:
                continue
            if player1 > player2:
                print("1. ", puntaje3["Nombre"])
                print("2. ", puntaje1["Nombre"])
                print("3. ", puntaje2["Nombre"])
            elif player1 < player2:
                print("1. ", puntaje3["Nombre"])
                print("2. ", puntaje2["Nombre"])
                print("3. ", puntaje1["Nombre"])
    
    elif puntaje1["Puntos"] == puntaje2["Puntos"] and puntaje2["Puntos"] > puntaje3["Puntos"]: #Novena posibilidad del resultado del juego
        cont = 1
        palyer1 = 0
        player2 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                player1= p["Estante 3"]
            elif cont ==2:
                player2= p["Estante 3"]
                cont +=1
            elif cont ==3:
                continue
            if player1 > player2:
                print("1. ", puntaje1["Nombre"])
                print("2. ", puntaje2["Nombre"])
                print("3. ", puntaje3["Nombre"])
            elif player1 < player2:
                print("1. ", puntaje2["Nombre"])
                print("2. ", puntaje1["Nombre"])
                print("3. ", puntaje3["Nombre"])

    elif puntaje1["Puntos"] == puntaje3["Puntos"] and puntaje3["Puntos"] > puntaje2["Puntos"]: #Decima posibilidad del resultado del juego
        cont = 1
        palyer1 = 0
        player3 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                player1= p["Estante 3"]
            elif cont ==2:
                cont +=1
                continue
            elif cont ==3:
                player3 = p["Estante 3"]
                continue
            if player1 > player3:
                print("1. ", puntaje1["Nombre"])
                print("2. ", puntaje3["Nombre"])
                print("3. ", puntaje2["Nombre"])
            elif player1 < player2:
                print("1. ", puntaje3["Nombre"])
                print("2. ", puntaje1["Nombre"])
                print("3. ", puntaje2["Nombre"])
    
    elif puntaje1["Puntos"] == puntaje3["Puntos"] and puntaje3["Puntos"] < puntaje2["Puntos"]: #Undecima posibilidad del resultado del juego
        cont = 1
        palyer1 = 0
        player3 = 0
        for p in Personas:
            if cont == 1:
                cont += 1
                player1= p["Estante 3"]
            elif cont ==2:
                cont +=1
                continue
            elif cont ==3:
                player3 = p["Estante 3"]
                continue
            if player1 > player3:
                print("1. ", puntaje2["Nombre"])
                print("2. ", puntaje1["Nombre"])
                print("3. ", puntaje3["Nombre"])
            elif player1 < player2:
                print("1. ", puntaje2["Nombre"])
                print("2. ", puntaje3["Nombre"])
                print("3. ", puntaje1["Nombre"])




def reportes(): #esta es la función de reportes que se encargará de imprimir los reportes desde el archivo a la consola
    question2= int(input("Seleccione que reporte desea obtener \n1< Reporte 1 \n2< Reporte 2\n")) #aquí decidimos que reporte queremos obtener
    if question2 == 1:
        archivos() #se llama al reporte 1
    elif question2 ==2:
        reportes2() #se llama al reporte 2
    else:
        print("No digitó un número correcto")
        reportes()



def convertirStringALista(): #esta función se encarga de introducir la info a la consola desde el archivo
    archivo = open("info.txt", "r")
    listaPadre = []
    for linea in archivo.readlines():
        linea = linea.rstrip()
        listaHija = [str(i) for i in linea.split(",")]
        listaPadre.append(listaHija)
    archivo.close()
    print(listaPadre)



def archivos(): #esta función se encarga de introducir las estadiscticas de los usuarios en un archivo
    archivo = open("info.txt", "w")
    archivo.write("Estadisticas de los usuarios\n")
    for p in Personas:
        archivo.write(p["Nombre"])
        archivo.write(" obtuvo un total de ")
        archivo.write(str(p["Puntos"]))
        archivo.write(" puntos ")
        archivo.write("\n")
        archivo.write(str(p["Lista 1"]))
        archivo.write("\n")
        archivo.write(str(p["Lista 2"]))
        archivo.write("\n")
        archivo.write(str(p["Lista 3"]))
        archivo.write("\n")
    archivo.close()
    convertirStringALista() #Aquí se llama la función que se encarga de pasar la información de archivos a consola




def imprimir(): #Esta función se encarga de imprimir las estadisticas al usuario
    for p in Personas:
        print(p["Nombre"], "tuvo", p["Estante 1"], "puntos en el estante 1,", p["Estante 2"], "puntos en el estante 2, y", p["Estante 3"], "puntos en el estante 3 para un total de puntos de: ", p["Puntos"])




def juego(): #aquí esta el algoritmo del programa que se encarga de ver si las personas ganan puntos o no
    for p in Personas:
        Encestos1 = []
        Encestos2 = []
        Encestos3 = []
        if p["Puntos"] == 0:
            Lista_1 = [{"Posición": 1, "Puntos": 1}, {"Posición": 2, "Puntos": 1}, {"Posición": 3, "Puntos": 1},
            {"Posición": 4, "Puntos": 1}, {"Posición": 5, "Puntos": 2}]  #Estante número 1
            Lista_2 = [{"Posición": 1, "Puntos": 1}, {"Posición": 2, "Puntos": 1}, {"Posición": 3, "Puntos": 1},
            {"Posición": 4, "Puntos": 1}, {"Posición": 5, "Puntos": 2}]  #Estante número 2
            Lista_3 = [{"Posición": 1, "Puntos": 2}, {"Posición": 2, "Puntos": 2}, {"Posición": 3, "Puntos": 2},
            {"Posición": 4, "Puntos": 2}, {"Posición": 5, "Puntos": 2}]  #Estante número 3
            cont = 1
            for l in Lista_1:
                aleatorio = [1,2,3,4,5]
                num = random.choice(aleatorio)
                if l["Posición"] == num:
                    p["Puntos"] += l["Puntos"]
                    p["Estante 1"] += l["Puntos"]
                    if cont == 5:
                        Encestos1.append(2)
                    else:
                        Encestos1.append(1)
                        cont +=1
                else:
                    Encestos1.append(0)
                    cont +=1
                    continue
            p["Lista 1"] = Encestos1
            cont = 1
            for j in Lista_2:
                aleatorio = [1,2,3,4,5]
                num = random.choice(aleatorio)
                if j["Posición"] == num:
                    cont = 1
                    p["Puntos"] += j["Puntos"]
                    p["Estante 2"] += j["Puntos"]
                    if cont == 5:
                        Encestos2.append(2)
                    else:
                        Encestos2.append(1)
                        cont +=1
                else:
                    Encestos2.append(0)
                    cont +=1
                    continue
            p["Lista 2"] = Encestos2
            for k in Lista_3:
                aleatorio = [1,2,3,4,5]
                num = random.choice(aleatorio)
                if k["Posición"] == num:
                    p["Puntos"] += k["Puntos"]
                    p["Estante 3"] += k["Puntos"]
                    Encestos3.append(2)
                else:
                    Encestos3.append(0)
                    continue
            p["Lista 3"] = Encestos3
    imprimir() #Aquí se llama la función de imprimir, la cual se encarga de imprimir las estadisticas de los usuarios, esta función es la anterior de la función llamada juego 

def competir():
    cont = 1
    while cont < 4: #Aquí se crea los perfiles de los jugadores, el contador tiene que ser menor de cuatro porque solo son 3 jugadores
        persona = {}
        question1 = input("Cual es el nombre del jugador\n")
        persona["Nombre"] = question1
        persona["Puntos"] = 0
        persona["Estante 1"] = 0
        persona["Estante 2"] = 0
        persona["Estante 3"] = 0
        persona["Lista 1"] = []
        persona["Lista 2"] = []
        persona["Lista 3"] = []
        cont +=1
        Personas.append(persona)
    juego() #Aquí se llama la función que se va a encargar de hacer las partidas







def menu(): #Menú principal
    while True:
        print("Menú")
        print("1 > Competir \n2 > Reportes \n3 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("¡Bienvenido a competir!")
            competir()
        elif opcionSelec == 2:
            print("¡Bienvenido a Reportes!")
            reportes()
        elif opcionSelec == 3:
            print("¡¡Gracias por usar nuestro sistema, hasta pronto!!")
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()