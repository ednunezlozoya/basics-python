
# Ejemplo1
age_dog = 7

if age_dog < 5:
    print("Su lomito es joven")
else:
    print("Su lomito es adulto")

# Ejemplo2
annio_nacimiento = int(input("Introduzca su año de nacimiento: "))

if annio_nacimiento >= 1930 and annio_nacimiento <= 1948:
    print("Eres de los \"niños de la Posguerra\"")
elif annio_nacimiento >= 1949 and annio_nacimiento <= 1968:
    print("Eres un \"Baby Boomer\"")
elif annio_nacimiento >= 1969 and annio_nacimiento <= 1980:
    print("Eres de la \"Generacion X\"")
elif annio_nacimiento >= 1981 and annio_nacimiento <= 1993:
    print("Eres \"Millenial\"")
elif annio_nacimiento >= 1994 and annio_nacimiento <= 2010:
    print("Eres de la \"Generacion Z\"")
elif annio_nacimiento >= 2011:
    print("Eres de los \"Alfa\"")
else:
    print("Eres de etapa no definida")

# ternary operators
age_of_dog = input("Cual es la edad de su perro? ")

result_dog = "Joven" if int(age_of_dog) <= 5 else "Adulto"

print(f"Su perro es: {result_dog} !")

# foor loop with range
# Sample1 imprime numeros del 1..10
for x in range(10):
    print(x + 1)

# Sample2 impresion de la sumatoria de los numeros del 1..10
suma = 0
for i in range(1, 11):
    suma += i

print(f"Suma del 1 al 10: {suma}")

# Sample2 impresion de numeros pares del 2 al 20
for num_par in range(2, 22, 2):
    print(f"Numero Par: {num_par}")

# Sample3 impresion de numeros impares del 1..20
for num_impar in range(1, 20, 2):
    print(f"Numero Impar: {num_impar}")

# foor loop with range
# Imprime numeros del 3..10
x = 3                              
while x <= 10:
    print(f"Value of \'x\'= {x}")
    x = x + 1


