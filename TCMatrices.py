import random
import tabulate

#Ejercicio 1

print("\nEjercicio #1 \n")

matriz = []
def matriz_():
    for f in range(5):
        matriz.append([])
        for c in range(5):
            num = random.randint(1, 50)
            matriz[f].append(num)
    print(matriz)
matriz_()

def test():
    from tabulate import tabulate
    print(tabulate(matriz))
test()

def recorrer():
    for f in range(5): 
        for c in range(5) : 
            if (matriz[f][c] %2 == 0):
                matriz[f][c] = "$"
            else:
                matriz[f][c] = "#"
    from tabulate import tabulate
    print(tabulate(matriz))
recorrer()


###################################################################################################

#Ejercicio 2

print("\nEjercicio #2 \n")

matriz_2 = []
print("Cuantas filas desea tener en su matriz: ")
fil = int(input())
print("Cuantas columnas desea tener en su matriz: ")
col = int(input())
def matriz__():
    for f in range(fil):
        matriz_2.append([])
        for c in range(col):
            nume = random.randint(1, 20)
            matriz_2[f].append(nume)
    print(matriz_2)
matriz__()
def recorrer2():
    cont = 0
    fila = 1
    for f in matriz_2:
        if matriz_2[cont][0] == 5:
            print("La fila", fila, "inicia en 5")
            cont +=  1
            fila = fila + 1
        else:
            print("La fila", fila, "no inicia en 5")
            cont +=  1
            fila += 1
recorrer2()
