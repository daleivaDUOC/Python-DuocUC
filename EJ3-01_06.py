## Ejercicio 3: Datos Personales con Diccionarios
datos_personales = {}
while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    edad = int(input("Ingrese la edad: "))
    datos_personales[nombre] = edad # Agregar al diccionario

# Identificar edades únicas
edades_unicas = {edad for edad in datos_personales.values()}

print("Edades únicas presentes:", edades_unicas)
