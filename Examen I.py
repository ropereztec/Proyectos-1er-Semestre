personas =[]
personas.append(["Roosevelt", 208400858, "Masculino",[]]) #Datos quemados para probar el programa
mascotas = []
mascotas.append([111, "Tom", "Perro", "Disponible"]) #Datos quemados para probar el programa
Ver_Cedulas = []
Ver_Cedulas.append(208400858) #Datos quemados para probar el programa
Ver_Id_Pets = []
pets_Disponibles = []
pets_Disponibles.append([111, "Tom", "Perro", "Disponible"]) #Datos quemados para probar el programa
pets_NoDisponibles = []

####################################################################################################

def registro_de_personas():
    personas_ = []
    print("Favor indique su nombre: ")
    nombre = input()
    personas_.append(nombre)
    print("Favor indique su número de cedula")
    cedula = int(input())
    personas_.append(cedula)
    Ver_Cedulas.append(cedula)
    print('Favor indique su género\n"Masculino" o "Femenino"')
    genero = (input())
    personas_.append(genero)
    mascotas_ = []
    personas_.append(mascotas_)
    personas.append(personas_)
    print(personas)
####################################################################################################

def registro_de_mascotas():
    mimascota = []
    print("Favor indique el identificador de la mascota")
    id_pet = int(input())
    mimascota.append(id_pet)
    print("Favor indique el nombre de la mascota")
    nom_pet= input()
    mimascota.append(nom_pet)
    print('Favor indique el tipo de mascota "Perro o Gato"') 
    type_pet= input()
    mimascota.append(type_pet)
    print('Favor indique el estado de la mascota "1. Disponible o 2. adoptado"') 
    status_pet = int(input())
    if status_pet <= 1:
        mimascota.append("Disponible")
        pets_Disponibles.append(mimascota)
    if status_pet >= 2:
        mimascota.append("Adoptado")
        pets_NoDisponibles.append(mimascota)
    mascotas.append(mimascota)
    print(mascotas)
####################################################################################################

def adoptar_mascotas():
    print("Favor ingrese su cédula")
    cedula = int(input())
    if cedula in Ver_Cedulas:
        print("Estas son las mascotas disponibles")
        print(pets_Disponibles)
        print("Ingrese el ID de la mascota que quiere adoptar")
        ID_pets = int(input())
        for p in personas:
            if p[1] == cedula:
                if len(p[3]) > 1:
                    print("No puede adoptar más mascotas")
                    break
                else:
                    p[3].append(ID_pets)
                    print("Felicidades a adoptado a una nueva mascota")
                    for m in mascotas:
                        if m[0] == ID_pets:
                            m[3] = "Adoptado"
                    for m in pets_Disponibles:
                        if m[0] == ID_pets:
                            pets_Disponibles.remove(m) 
                            print(personas)
    if not cedula in Ver_Cedulas:
        print("Ingresar un número de cédula válido o registrese")
####################################################################################################
def reporte1():
    for p in personas:
        if len(p[3])>= 1:
            for id_pet in p[3]:
                for m in mascotas:
                    if id_pet == m[0]:
                        print("[", p[0],",", p[1],"," ,p[2],"]", m)
####################################################################################################
def reporte2():
    Hom = 0
    Muj = 0
    for p in personas:
        if len(p[3])>=1:
            if p[2] == "Masculino":
                Hom +=1
            else:
                Muj +=1
    print("La cantidad de hombres es: ", Hom)
    print("La cantidad de mujeres es: ", Muj)


###################################################################################################
def menúreportes():
    while True:
        print("Menú de Reportes")
        print("1 > Reporte 1 \n2 > Reporte 2 \n3 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("Reporte 1")
            reporte1()
        elif opcionSelec == 2:
            print("Reporte 2")
            reporte2()
        elif opcionSelec == 3:
            print("Regresar al menú principal")
            break

###################################################################################################
def menu():
    while True:
        print("Menú")
        print("1 > Registros de Personas \n2 > Registro de Mascotas \n3 > Adoptar Mascotas \n4 > Reportes \n5 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))


        if opcionSelec == 1:
            print("Registros de Personas")
            registro_de_personas()
        elif opcionSelec == 2:
            print("Registro de Mascotas")
            registro_de_mascotas()
        elif opcionSelec == 3:
            print("Adoptar Mascotas")
            adoptar_mascotas()
        elif opcionSelec == 4:
            print("Reportes")
            menúreportes()
        elif opcionSelec == 5:
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()
####################################################################################################
