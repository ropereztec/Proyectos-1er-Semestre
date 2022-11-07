'''Utilizando POO, defina una clase con su respectivo constructor y atributos; además, defina los siguientes métodos dentro de la clase:
def solicitarInformacion() # solicita los datos de la persona.
def calcularIMC() # calcula el IMC a través de la fórmula
def resultado() # imprime el diagnóstico del IMC de la persona

Construir un programa que calcule el Indice de Masa Corporal (IMC) de una persona e indique el estado en el que se encuentra esa persona en función del valor de IMC.

La fórmula para calcular el IMC es: IMC = Peso (kg) / altura (m)2
Donde, kg significa kilos, m significa altura en metros y el 2 significa que esta elevado al cuadrado. Entonces se lee, el IMC es el peso entre altura elevada al cuadrado.

El sistema debe permitir que el usuario coloque su nombre, peso y altura; con base a lo anterior y utilizando la fórmula, debe calcular el IMC. Utilice la siguiente tabla como referencia:

IMC            Diagnóstico
<14           Criterio de ingreso en hospital
De 14 a 16     Infrapeso
De 17 a 18    Bajo peso
De 19 a 25    Peso normal (saludable)
De 26 a 30    Sobrepeso (obesidad de grado I)
De 31 a 35    Sobrepeso crónico (obesidad de grado II)
De 36 a 40    Obesidad premórbida (obesidad de grado III)
>40            Obesidad mórbida (obesidad de grado IV)

Debe imprimir en consola el resultado de la situación de salud de la persona; un ejemplo sería:
Nombre: Carlos
Peso: 68
Altura: 1.65 # recuerde que es en metros

Para el ejemplo anterior, se debe imprimir de la siguiente manera:
Estimado Carlos su IMC es de 24.98 por lo cual el diagnóstico es: Peso normal (saludable)'''


class Persona():
    def __init__(self):
        self.edad = 0
        self.peso = 0
        self.nombre = ""
        self.altura = 0
        self.dignostico = ""
    def solicitarInformacion(self):
        self.nombre = input("Favor ingrese su nombre: ")
        self.edad = int(input("Favor indique su edad: "))
        self.peso = float(input("Favor ingrese su peso en kilogramos: "))
        self.altura = float(input("Favor ingrse su altura en metros: "))
    def calcularIMC(self):
        self.imc = self.peso / (self.altura**2)
        if self.imc < 14:
            self.dignostico = "Criterio de ingreso al hospital"
        elif self.imc >= 14 and self.imc <= 16:
            self.dignostico = "Infrapeso"
        elif self.imc >= 17 and self.imc <= 18:
            self.dignostico = "Bajo Peso"
        elif self.imc >= 19 and self.imc <= 25:
            self.dignostico = "Peso Normal"
        elif self.imc >= 26 and self.imc <= 30:
            self.dignostico = "Sobre Peso (Grado I)"
        elif self.imc >= 31 and self.imc <= 35:
            self.dignostico = "Sobre Peso Crónico (Grado II)"
        elif self.imc >= 36 and self.imc <= 40:
            self.dignostico = "Obesidad premórbida (Grado III)"
        elif self.imc > 40:
            self.dignostico = "Obesidad mórbida (obesidad de grado IV)"


            
    def resultado(self):
        print("Estimado", self.nombre , "su IMC es de" , self.imc , "por lo cual su diagnostico es" , self.dignostico)

Paciente = Persona()
Paciente.solicitarInformacion()
Paciente.calcularIMC()
Paciente.resultado()
