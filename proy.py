#########################ADMINISTRADOR####################################################################
import contextlib
from datetime import date
from datetime import datetime

Administrador = ["alealfaroitcr", 20221017] #Administrador[0] = Es el usuario, Administrador[1] es la contraseña.
Tecnologias= [{"ID": 999, "Nombre": "Python","type": "Backend"},{"ID": 998, "Nombre": "PHP","type": "Backend"}]

vacantes = [{"ID": 1010,"Puesto": "Desarrollador Backend", "Tecnologías": [["Python", "Basico"]],
"Cantidad de Puestos": 3, "Dominio de ingles": "B1", "edad": [22,34], 
"Empresa": "Coopelesca", "Ubicacion": "Alajuela", "Disponibilidad": []},]
#########################EMPRESA####################################################################
Empresas = [{"ID": 101, "Nombre": "Coopelesca","Provincia": "Alajuela"}] 
#########################PERSONAS####################################################################
Personas = [{"cedula": 208400858, "Nombre": "Roosevelt","edad": 19 ,"Ubicación": "Alajuela", "Tecnología": [['Python', 'Basico']],
"Nivel de Ingles": "B2"}, {"cedula": 207930524, "Nombre": "Bayron","edad": 23, "Ubicación": "Alajuela", "Tecnología": [['Python', 'Basico']],
"Nivel de Ingles": "B2"}]

coincidencia = []
#########################ADMINISTRADOR####################################################################

#----------------------------------Opción 1 del menú Principal-----------------------------------------------

#----------------------------------Administrador-------------------------------------------------------------
def insertar_tecnologías():
    listatecnoogías={}
    print("------------------------------------------------------------------")
    while True:
        try:
            identificador = int(input("identificador: "))
            break
        except ValueError:
            print("Parece que digitaste un caracter incorrecto, por favor usa números")
    nombre = input("Nombre: ")
    tipotec= int(input("Digite el tipo de tecnología \n1= si es Frontend o \n2= si es Backend \n"))
    if tipotec==1:
        tipo="Frontend"
    elif tipotec==2:
        tipo ="Backend"
    else:
        print("------------------------------------------------------------------")
        print("Lo digitado no es admitido, intentelo nuevamente")
        insertar_tecnologías()
    listatecnoogías["ID"]= identificador
    listatecnoogías["Nombre"]= nombre
    if tipotec==1:
        listatecnoogías["type"] = tipo
        Tecnologias.append(listatecnoogías)
    elif tipotec==2:
        listatecnoogías["type"] = tipo
        Tecnologias.append(listatecnoogías)
    print("------------------------------------------------------------------")
    print("Se ha registrado con exito", nombre)
    return
def listas_de_coincidencias():
    print("Las listas de coincidencias son las siguientes")
    print(coincidencia)
def reportesadmi():
    g=0


#----------------------------------Empresa-------------------------------------------------------------
def varificación_de_tecnologías():
    global verificación_de_tec
    for t in Tecnologias:
        if tec == t["Nombre"]:
            verificación_de_tec = True
            break
        else:
            verificación_de_tec = False

def tec_vacante():
    tecnologia1=[]
    tecnologíaavailable=[]
    print("Tecnologías disponibles")
    for t in Tecnologias:
        print(t["Nombre"])
    global tec
    tec= input("Que tecnología desea contratar (Seleccione una)\n")
    varificación_de_tecnologías()
    if verificación_de_tec != False:
        tecnologia1.append(tec)
        level= int(input("Que nivel de dominio requiere la empresa \n1= Basico \n2= intermedio \n3= Avanzado\n"))
        if level == 1:
            tecnologia1.append("Basico")
            tecnologia2.append(tecnologia1)
        elif level ==2:
            tecnologia1.append("Intermedio")
            tecnologia2.append(tecnologia1)
        elif level == 3:
            tecnologia1.append("Avanzado")
            tecnologia2.append(tecnologia1)
        quest=int(input("Desea Agregar más tecnologías \n1= Sí \n2= No\n"))
        if quest ==1:
            tec_vacante()
        elif quest ==2:
            vacante1["Tecnologías"] = tecnologia2
        question3 = int(input("Cuantos puestos hay para esta vacante?\n"))
        vacante1["Cantidad de Puestos"] = question3
        dom= int(input("Nivel de dominio de inglés requerido: \n1= A1\n2= A2\n3= B1\n4= B2\n5=C1\n"))
        if dom == 1:
            vacante1["Dominio de ingles"] = "A1"
        elif dom == 2:
            vacante1["Dominio de ingles"] = "A2"
        elif dom == 3:
            vacante1["Dominio de ingles"] = "B1"
        elif dom == 4:
            vacante1["Dominio de ingles"] = "B2"
        elif dom== 5:
            vacante1["Dominio de ingles"] = "C1"
        edad1= int(input("Cual es el minimo de edad para aplicar a esta vacante: "))
        edad2= int(input("Cual es el maximo de edad para aplicar a esta vacante: "))
        edad = [edad1, edad2]
        vacante1["edad"] = edad
        for e in Empresas:
                if ID_Empresa == e["ID"]:
                    vacante1["Empresa"] = e["Nombre"]
                    vacante1["Ubicacion"] = e["Provincia"]
                    vacante1["Disponibilidad"] = []
        vacantes.append(vacante1)
        menu()
    else:
        print("Error: Verifique que la tecnología que usted digíto este escrita correctamente como se muestra en consola o este disponible")

def lista1():
    global tecnologia2
    tecnologia2=[]
    tec_vacante()

def puesto_():
    global puesto
    question = int(input("¿Que tipo de puesto es? \n1= Desarrollador Backend \n2= Desarrollador Frontend \n3= Desarrollador Fullstack\n"))
    if question==1:
        puesto = "Desarrollador Backend"
        vacante1["Puesto"] = puesto
        lista1()
    elif question==2:
        puesto = " Desarrollador Frontend"
        vacante1["Puesto"] = puesto
        lista1()
    elif question==3:
        puesto = "Desarrollador Fullstack"
        vacante1["Puesto"] = puesto
        lista1()
    else:
        print("Introdujo un número incorrecto, por favor vuelva a intentarlo")
        puesto()

def verificacion_vacante():
    for v in vacantes:
        global ver_vacante
        if v["ID"] == ID_vacante:
            ver_vacante = True
            break
        else:
            ver_vacante = False

def insertar_vacante():
    global vacante1 
    vacante1={}
    global ID_vacante
    ID_vacante = int(input("Agregue el identificador de la vacante: "))
    verificacion_vacante()
    if ver_vacante != True:
        vacante1["ID"] = ID_vacante
        puesto_()
    else:
        print("Ese identificador de vacante ya existe")
#----------------------------------Usuario-------------------------------------------------------------
def vacantesdisponibles():
    global vacante_disponible 
    for p in Personas:
        if cedula == p["cedula"]:
            for v in vacantes:
                edad1 = v["edad"][0]
                edad2 = v["edad"][1]
                if p["edad"] > edad1:
                    if p["edad"] < edad2:
                        v["Disponibilidad"].append(True)
                        
                    else:
                        v["Disponibilidad"].append(False)
                        
                else:
                    v["Disponibilidad"].append(False)
                    


def match():
    for p in Personas:
        if cedula == p["cedula"]:
            for v in vacantes:
                global cont
                cont = 0
                if v["ID"] == question5:
                    if v["Ubicacion"] == p["Ubicación"]:
                        cont += 10
                    else:
                        continue
                    if v["Dominio de ingles"] == p["Nivel de Ingles"]:
                        cont +=20
                    else:
                        continue
            conta = 0
            for i in v["Tecnologías"]:
                for u in p["Tecnología"]:
                    if i[0] == u[0]:
                        conta +=1
                    ope = conta / len(v["Tecnologías"])
                    ope2 = ope * 100
                    if ope2 < 75:
                        continue
                    elif ope2 > 75:
                        cont += 40
                conta = 0
                for i in v["Tecnologías"]:
                    for u in p["Tecnología"]:
                        if i[1] == u[1]:
                            conta +=1
                    ope = conta / len(v["Tecnologías"])
                    ope2 = ope * 100
                    if ope2 < 75:
                        continue
                    elif ope2 > 75:
                        cont += 10
            if cont >= 80:
                print("Usted esta participando por la vacante")
                v["Cantidad de Puestos"] -=1
                now = datetime.now()
                format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
                coincidencia1= []
                coincidencia1.append(v["ID"])
                coincidencia1.append(v["Empresa"])
                coincidencia1.append(v["Ubicacion"])
                coincidencia1.append(v["Tecnologías"])
                coincidencia1.append(v["Dominio de ingles"])
                coincidencia1.append(v["edad"])
                coincidencia1.append(cedula)
                coincidencia1.append(p["Nombre"])
                coincidencia1.append(p["edad"])
                coincidencia1.append(format)
                coincidencia.append(coincidencia1)

            elif cont < 80:
                print("Usted lamentablemente no ha sido seleccionado para participar por la vacante solicitada")




def aplicar_a_vacante():
    vacantesdisponibles()
    print("Vacantes disponibles")
    for v in vacantes:
        if v["Disponibilidad"] == [True]:
            print("Identificador: ", v["ID"], "/", "Empresa", v["Empresa"], "/","Cantidad de puestos", v["Cantidad de Puestos"],"/", "Tecnologías requeridas", v["Tecnologías"], "/", "Puesto: " ,v["Puesto"], "/"  "Cantidad de puestos", v["Cantidad de Puestos"], "/", "Nivel requerido de Ingles", v["Dominio de ingles"], "/","Rango de edad", v["edad"])
        elif ["Disponibilidad"] == [False]:
            continue
    global question5
    question5 = int(input("Digite el identificador de la vacante por la que desea participar: "))
    match()
#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!

#----------------------------------Opción 2 del menú Principal-----------------------------------------------
def Selección_de_provincia():
    selec = int(input("De que provincia es la empresa \n1= San José\n2=Alajuela\n3=Cartago\n4=Heredia\n5=Guanacaste\n6=Puntarenas\n7=Limón\n"))
    global provincia_selecionada
    if selec ==1:
        provincia_selecionada = "San José"
    elif selec ==2:
        provincia_selecionada = "Alajuela"
    elif selec==3:
        provincia_selecionada = "Cartago"
    elif selec ==4:
        provincia_selecionada = "Heredia"
    elif selec==5:
        provincia_selecionada = "Guanacaste"
    elif selec ==6:
        provincia_selecionada = "Puntarenas"
    elif selec==7:
        provincia_selecionada = "Limón"
    else:
        print("Digitó un número incorrecto")
        Selección_de_provincia()


def verificación_de_empresas():
    for e in Empresas:
        if e["ID"] == ident:
            global ver
            ver = True
            break
        else:
            ver = False

def registro_de_empresas():
    Empresa= {}
    print("Por favor digite los datos que se le solicita")
    global ident
    
    while True:
        try:
            ident= int(input("Identificador: "))
            break
        except ValueError:
            print("Error: Parece que digitó un caracter incorrecto, por favor utilice números")
    verificación_de_empresas()
    if ver != True:
        Empresa["ID"] = ident
        name = input("Nombre: ")
        Empresa["Nombre"] = name
        Selección_de_provincia()
        Empresa["Provincia"] = provincia_selecionada
        print("Se ha regitrado la empresa", name, "/ su identificador es", ident, "y es de la provincia de", provincia_selecionada)
        Empresas.append(Empresa)
    else:
        print("Esta empresa ya esta registrada")
    

lista_tecnología_y_nivel = []


#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!


#----------------------------------Opción 3 del menú Principal-----------------------------------------------
def agregar_tecnologia():
    tecno= []
    print("Tecnologías disponibles")
    for t in Tecnologias:
        print(t["Nombre"])
    name= (input("Digite el nombre de su tecnología (Por favor verífique que lo escribe correctamente): "))
    tecno.append(name)
    level=int(input("Nivel de dominio \n1= Basico \n2= Intermedio \n3= Avanazdo\n"))
    if level == 1:
        tecno.append("Basico")
    elif level ==2:
        tecno.append("Intermedio")
    elif level == 3:
        tecno.append("Avanzado")
    else:
        print("Digitó un número incorrecto")
    question1= int(input("Desea agregar más tecnologías \n1= Sí \n2= No\n"))
    lista_tecnología_y_nivel.append(tecno)
    if question1 == 1:
        agregar_tecnologia()
    else:
        return

def Selección_de_provincia_Usuario():
    global provincia_usuario
    selec = int(input("Seleccione su provincia \n1= San José\n2=Alajuela\n3=Cartago\n4=Heredia\n5=Guanacaste\n6=Puntarenas\n7=Limón\n"))
    global provincia_selecionada
    if selec ==1:
        provincia_usuario = "San José"
    elif selec ==2:
        provincia_usuario = "Alajuela"
    elif selec==3:
        provincia_usuario = "Cartago"
    elif selec ==4:
        provincia_usuario = "Heredia"
    elif selec==5:
        provincia_usuario = "Guanacaste"
    elif selec ==6:
        provincia_usuario = "Puntarenas"
    elif selec==7:
        provincia_usuario = "Limón"
    else:
        print("Digitó un número incorrecto")
        Selección_de_provincia()

def verificacióndeusuarios():
    for u in Personas:
        if u["cedula"] == cedu:
            global ver_personas
            ver_personas = True
            break
        else:
            ver_personas = False


def registro_de_usuario():
    global lista_tecnología_y_nivel
    usuario = {}
    print("Por favor digite los datos que se le solicita")
    global cedu
    cedu= int(input("Cedula: "))
    verificacióndeusuarios()
    if ver_personas != True:
        usuario["cedula"] = cedu
        usuario["Nombre"] = input("Nombre: ")
        usuario["edad"] = int(input("Edad: "))
        if usuario["edad"] < 18:
            print("El usuario debe de ser mayor de edad para poderse registrar")
            menu()
        else:
            Selección_de_provincia_Usuario()
            usuario["Ubicacion"] = provincia_usuario
            question1 = agregar_tecnologia()
            usuario["Tecnología"] = lista_tecnología_y_nivel
            lista_tecnología_y_nivel = []
            question2 = int(input("Cual es su nivel de ingles \n1= A1 \n2= A2 \n3= B1 \n4= B2 \n5= C1\n"))
            if question2 == 1:
                usuario["Nivel de Ingles"] = "A1"
            elif question2 == 2:
                usuario["Nivel de Ingles"] = "A2"
            elif question2 == 3:
                usuario["Nivel de Ingles"] = "B1"
            elif question2 == 4:
                usuario["Nivel de Ingles"] = "B2"
            elif question2== 5:
                usuario["Nivel de Ingles"] = "C1"
            Personas.append(usuario)
    else:
        print("Este usuario ya existe")
#----------------------------------Final de las opciones del menú-----------------------------------------------
def inicio_de_sesion():
    inicio = int(input("Cómo deseas ingresar \n1= Administrador \n2= Empresa \n3= Usuario \n"))
    if inicio == 1:
        usuario= input("Digite su nombre de usuario: ")
        if usuario == Administrador[0]:
            contraseña = int(input("Digite su contraseña: "))
            if contraseña == Administrador[1]:
                while True:
                    print("Menú")
                    print("1 > Insertar Tecnologías \n2 > Listas de Coincidencias \n3 > Reportes \n4 > Regresar al menú principal ")
                    opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))
                    if opcionSelec == 1:
                        print("Insertar tecnologías")
                        insertar_tecnologías()
                    elif opcionSelec == 2:
                        print("Listas de coincidencias")
                        listas_de_coincidencias()
                    elif opcionSelec == 3:
                        print("¡Bienvenido al registro de usuarios!")
                        reportesadmi()
                    elif opcionSelec == 4:
                        print("Haz elegido regresar a menú principal")
                        break
                    else:
                        input("No a ingresado un código correcto. Pulse ENTER para continuar.")
            else:
                print("contraseña incorrecta")
        else:
            print("Usuario no encontrado")
    elif inicio == 2:
        global ID_Empresa
        ID_Empresa = int(input("Digite el identificador de la empresa: "))
        for e in Empresas:
            if ID_Empresa == e["ID"]:
                while True:
                    print("Menú")
                    print("1 > Insertar vacantes \n2 > Regresar al menú principal")
                    opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))
                    if opcionSelec == 1:
                        print("Insertar vacantes")
                        insertar_vacante()
                    elif opcionSelec == 2:
                        print("Haz elegido regresar a menú principal")
                        break
                    else:
                        input("No a ingresado un código correcto. Pulse ENTER para continuar.")
            else:
                continue 
    elif inicio == 3:
        global cedula
        cedula = int(input("Digite su numero de cedula: "))
        for p in Personas:
            if p["cedula"] == cedula:
                while True:
                    print("Menú")
                    print("1 > Aplicar a una vacante \n2 > Regresar al menú principal")
                    opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))
                    if opcionSelec == 1:
                        print("Aplicar a una vacante")
                        aplicar_a_vacante()
                    elif opcionSelec == 2:
                        print("Haz elegido regresar a menú principal")
                        break
                    else:
                        input("No a ingresado un código correcto. Pulse ENTER para continuar.")

def menu():
    while True:
        print("Menú")
        print("1 > Inicio de Sesión \n2 > Registro de empresas \n3 > Registro de Usuarios \n4 > Salir ")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))

        if opcionSelec == 1:
            print("¡Bienvenido al inicio de sesión!")
            inicio_de_sesion()
        elif opcionSelec == 2:
            print("¡Bienvenido al registro de empresas!")
            registro_de_empresas()
        elif opcionSelec == 3:
            print("¡Bienvenido al registro de usuarios!")
            registro_de_usuario()
        elif opcionSelec == 4:
            print("¡Gracias por utilizar nuestro programa, hasta luego!")
            print("Tecnologías Registradas: ", Tecnologias)
            print("Empresas Registradas: ", Empresas)
            print("Vacantes Registrados: ", vacantes)
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()
