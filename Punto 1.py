"""
Algoritmo: Calcula el mcd de formaa iterativa y recursiva de n números
Autor: Johan Stevan Bermeo Buitrago
Fecha: 29/10/2024
"""
print("Bienvenido, te ayudaremos a calcular el mcd de los valores que desees ingresar.")
#Declaramos las variables a, b, num.
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
num = int(input("Ingrese el número de datos adicionales: "))
other = 0

for i in range(num):
  other = int(input("Ingrese el número: "))
  a = b
  b = other


#Creamos una función recursiva para calcular el mcd de los números ingresados
def mcd_iteracion (a, b, other):  
  while b:
    a, b = b, (a % b)
  if not other:
    return a
  else:
    return mcd_iteracion(a, other, b)

# Call mcd_iteracion after the loop
resultado = mcd_iteracion(a, b, other) 
print(f"El valor del mcd iterativo es: {resultado}")

#Creamos una función recursiva para calcular el mcd del primer y el segundo valor ingresado
def mcd_recursivo (a, b):
  if b == 0:
    return a
  else:
    return mcd_recursivo(b, a % b)

resultado = mcd_recursivo(resultado, other)

print(f"El valor del mcd recursivo es: {resultado}")