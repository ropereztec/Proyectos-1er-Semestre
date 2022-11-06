from random import choice

Equipos= []

jornadas = 1
def Jugar():
    j = 2
    global jornadas
    
    equipos= [{"Equipo" : "San Carlos", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0},
    {"Equipo" : "Saprissa", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0},
    {"Equipo" : "LDA", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0},
    {"Equipo" : "Heredia", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0},
    {"Equipo" : "Cartago", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0},
    {"Equipo" : "Puntarenas", "Puntos": 0, "Goles a Favor": 0, "Goles en contra": 0, "Partidos Ganados": 0}]
    print("Los Partidos a Jugar son:")
    i = 1
    while i < 4:
        Equipo1 = choice(equipos)
        print(Equipo1["Equipo"])
        delete = equipos.remove(Equipo1)
        print("vs")
        Equipo2 = choice(equipos)
        print(Equipo2["Equipo"])
        delete = equipos.remove(Equipo2)
        if i == 1:
            def partidas():
                Partido1 = [Equipo1, Equipo2]
                if jornadas == 1: 
                    Agregar1 = Equipos.append(Equipo1)
                    Agregar2 = Equipos.append(Equipo2)
                goles = [0,1,2,3,4,5]
                gol1 = choice(goles)
                gol2 = choice(goles)
                if gol1 > gol2:
                    for p in Equipos:
                        if p["Equipo"] == Equipo1["Equipo"]:
                            p["Puntos"] += 3
                            p["Partidos Ganados"] += 1
                            p["Goles a Favor"] += gol1
                            p["Goles en contra"] += gol2
                        else:
                            p["Puntos"] += 0
                            p["Goles a Favor"] += gol2
                            p["Goles en contra"] += gol1
                    print("El equipo ganador es: ",Equipo1["Equipo"])
                    print(Equipo1["Equipo"], "hizo", gol1, "goles")
                    print(Equipo2["Equipo"], "hizo", gol2, "goles")
                elif gol1 < gol2:
                    for p in Partido1:
                        if p["Equipo"] == Equipo1["Equipo"]:
                            p["Puntos"] += 0
                            p["Goles en contra"] += gol2
                            p["Goles a Favor"] += gol1
                        else:
                            p["Puntos"] += 3
                            p["Partidos Ganados"] += 1
                            p["Goles a Favor"] += gol2
                            p["Goles en contra"] += gol1
                    print("El equipo ganador es: ",Equipo2["Equipo"])
                    print(Equipo1["Equipo"], "hizo", gol1, "goles")
                    print(Equipo2["Equipo"], "hizo", gol2, "goles")
                else:
                    print("Se generó un empate, ahora vamos a tanda de penales")
                    print("Tome en consideración lo siguiente \nUsted va a patear los penales y deberá decidir donde patear \n1< Arriba a la derecha \n2< Arriba en el centro \n3< Arriba a la izquierda \n4< Abajo a la izquierda \n5< Abajo en el centro \n6< Abajo a la derecha")
                    patear = 1
                    Porteria = [1,2,3,4,5,6]
                    penales_anotados= 0
                    penales_atajados= 0
                    while patear < 5:
                        print("Seleccione el area donde vas a patear")
                        pat = int(input())
                        Port = choice(Porteria)
                        if pat == Port:
                            print("El portero atajó tu tiro")
                            patear = patear + 1
                            penales_atajados = penales_atajados + 1
                        else:
                            print("Has maracado gol")
                            patear = patear + 1
                            penales_anotados = penales_anotados + 1
                    if penales_anotados > penales_atajados:
                        print("Ganó el equipo",Equipo1["Equipo"])
                        Equipo1["Puntos"] += 1
                        Equipo1["Partidos Ganados"] +=1
                    elif penales_anotados < penales_atajados:
                        print("Ganó el equipo",Equipo2["Equipo"])
                        Equipo2["Puntos"] += 1
                        Equipo2["Partidos Ganados"] +=1
            partidas()
        elif i == 2:
            partidas()
        elif i == 3:
            partidas()
        print("---------------------------------------------------------------")
        i = i + 1 
    print(Equipos)
    jornadas += 1

def tabladepos():
    puntos=[]
    cont = 1
    for e in Equipos:
        puntos.append(e["Equipo"])
        puntos.append(e["Puntos"])
    for p in puntos:
        if p[1] > p[2]:
            print(cont, ".", puntos[0])
            cont +=1
        elif p[1] < p[2]:
            print(cont, ".", puntos[2])
        elif p[1] < p[2]:
            print(cont, ".", puntos[4])


def reportes():
    print("Partidos Ganados por cada equipo")
    for e in Equipos:
        print("-", e["Equipo"], e["Partidos Ganados"])
##################################################

def menu():
    while True:
        print("Menú")
        print("1 > Jugar \n2 > Tablas de Posiciones \n3 > Reportes \n4 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("Jugar")
            
            Jugar()
            
        elif opcionSelec == 2:
            print("Tablas de Posiciones")
            tabladepos()
        elif opcionSelec == 3:
            print("Reportes")
            reportes()
        elif opcionSelec == 4:
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()