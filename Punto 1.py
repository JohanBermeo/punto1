"""
Algoritmo: Algoritmo que haya el número mayor, menor y la media de lo números ingresados.
Autor: Johan Stevan Bermeo Buitrago
Fecha: 23/10/2024
"""
print("Bienvenido, analizaremos los números que ingreses y te daremos el número más bajo, el más alto y el promedio de todos")
#Creamos y definimos las variables que vamos a utilizar
contador = 0
suma = 0
mayor = None
menor = None
#Creamos un ciclo infinito que se rompa cuano ingresemos un "fin" por consola
while True:
    numero = int(input("Ingresa los valores a analizar (escribir 'fin' para acabar): "))
    fin = input("¿Desea finalizar el programa? (s/n": )
    if fin == "s":
        break
    else:
    #El programa finalizará si se escribe s en la opción
        contador += 1
        suma += numero
        if mayor is None or numero > mayor:
            mayor = numero
        if menor is None or numero < menor:
            menor = numero
    

if contador > 0:
    promedio = suma / contador
    print("El número más alto es:", mayor)
    print("El número más bajo es:", menor)
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números.")