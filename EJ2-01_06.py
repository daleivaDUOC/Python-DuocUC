# Ejercicio 2: Números Primos con Diccionarios
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
    
rango_inferior = int(input("Ingrese el rango inferior: "))
rango_superior = int(input("Ingrese el rango superior: "))

# Crear diccionario para almacenar números primos
numeros_primos = {num: "Es un número primo" for num in range(rango_inferior, rango_superior + 1) if es_primo(num)}
print("Números primos encontrados:")
for numero, descripcion in numeros_primos.items():
    print(f"{numero}: {descripcion}")
