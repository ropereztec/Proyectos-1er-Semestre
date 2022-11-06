#Estructuras de datos
Personas= [{"Nombre": "Roosevelt", "Cedula": 208400858}]

regalos = []



def Insertar_Regalos():
    regalo = {}
    nombre = input("Por favor mencione el nombre del regalo que está registrando: ")
    regalo["Nombre"] = nombre
    precio = int(input("Cual es el precio de este regalo: "))
    regalo["Precio"] = precio

    while True:
        try:
            categoria = int(input("Que categoría es este regalo \n1< Niño \n2< Niña \n3< Mujer Adolescente \n4< Hombre Adolescente\n"))
            break
        except ValueError: 
            print("Parece que no digitaste un número, por favor solo utiliza números")

    if categoria == 1:
        regalo["Categoría"] = "Niño"
    elif categoria == 2:
        regalo["Categoría"] = "Niña"
    elif categoria == 3:
        regalo["Categoría"] = "Mujer Adolescente"
    elif categoria ==4:
        regalo["Categoría"] = "Hombre Adolescente"
    else:
        print("Parece que digitaste un valor invalido")
    print("Su regalo se ha restrado con éxito")
    regalos.append(regalo)

def Insertar_Personas():
    usuario = {}
    Nombre = input("Por favor digite su nombre: ")
    Cedula = int(input("Favor digite su número de cedula: "))
    usuario["Nombre"] = Nombre
    usuario["Cedula"] = Cedula
    Personas.append(usuario)
    print(usuario["Nombre"], "te registraste con éxito")


def comprar_regalos():
    question1 = int(input("Por favor escriba su numero de cedula: "))
    for p in Personas:
        if question1 == p["Cedula"]:
            question2= int(input("Por favor indique la edad de la persona a quien va dirigido el regalo: "))
            question3 = int(input("Digite el género de la persona que va dirigido el regalo: \n1< Femenino \n2< Masculino \n"))
            if question2 <= 12 and question3 ==1:
                print("Los regalos Disponibles en esta categría")
                for r in regalos:
                    if r["Categoría"] == "Niña":
                        print("Nombre: ", r["Nombre"], "Precio", r["Precio"])
            elif question2 <= 12 and question3 ==2:
                print("Los regalos Disponibles en esta categría")
                for r in regalos:
                    if r["Categoría"] == "Niño":
                        print("Nombre: ", r["Nombre"], "Precio", r["Precio"])
            elif question2 > 12 and question2 <= 17 and question3 ==1:
                for r in regalos:
                    print("Los regalos Disponibles en esta categría")
                    if r["Categoría"] == "Mujer Adolescente":
                        print("Nombre: ", r["Nombre"], "Precio: " , r["Precio"])
            elif question2 > 12 and question2 <= 17 and question3 == 2:
                for r in regalos:
                    print("Los regalos Disponibles en esta categría")
                    if r["Categoría"] == "Hombre Adolescente":
                        print("Nombre: ", r["Nombre"], "Precio", r["Precio"])
            else:
                print("Vaya, parece que no tenemos regalos con los filtros establecidos")
                menu()
            question4 = input("Que articulo desea comprar: ")
            for v in regalos:
                for k in Personas:
                    if k["Cedula"] == question1:
                        if question4 == v["Nombre"]:
                            question5 = int(input("Cuantos articulos desea comprar: "))
                            precio = question5 * v["Precio"]
                            print("Su compra se ha realizado con éxito")
                            print("#################### Factura ####################")
                            print("#", k["Cedula"],                               "#")
                            print("#", k["Nombre"],                               "#")
                            print("#", v["Nombre"],                               "#")
                            print("#", v["Precio"],                               "#")
                            print("#", "Cantidad solicitada: ", question5,        "#")
                            print("#", precio,                                    "#")
                            print("#################################################")


        else:
            print("Lo sentimos, usted no está registrado en nuestro sistema, por favor verifique que escribió correctamente su número de cedula o por favor registrese")








def menu():
    while True:
        print("Menú")
        print("1 > Insertar Regalos \n2 > Insertar Personas \n3 > Comprar Regalos \n4 > Salir")
        opcionSelec = int(input("Ingrese el código de la opción que desea abrir: "))

        if opcionSelec == 1:
            print("¡Insertar Regalos!")
            Insertar_Regalos()
        elif opcionSelec == 2:
            print("¡Insertar Personas!")
            Insertar_Personas()
        elif opcionSelec == 3:
            print("¡Comprar Regalos!")
            comprar_regalos()
        elif opcionSelec == 4:
            print("¡Gracias por usar nuestro sistema, hasta luego!")
            quit()
        else:
            input("No a ingresado un código correcto. Pulse ENTER para continuar.")

menu()