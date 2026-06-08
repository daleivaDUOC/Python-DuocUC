#Administación socios de club deportivo
socios=[]
datosSocios={}

def agregar_socio():
    numero=int(input("Ingrese número de socio a asignar: "))
    if numero in datosSocios:
        print("Número ya asignado, regresando al menú...")
        return
    nombre=input("Ingrese nombre: ")
    edad=int(input("Ingrese edad: "))
    categoria=input("Ingrese categoría deportiva: ")

    socios.append(numero)

    datosSocios[numero] = {
        "nombre": nombre,
        "edad": edad,
        "categoria": categoria,
    }
    
    print("")

def buscar_socio():
    numero=int(input("Ingrese número de socio a buscar: "))

    if numero in datosSocios:
        print("\nSOCIO ENCONTRADO")
        print("---------------")
        print("Número:", numero)
        print("Nombre:", datosSocios[numero]["nombre"])
        print("Edad:", datosSocios[numero]["edad"])
        print("Categoría:", datosSocios[numero]["categoria"])

    else:
        print("Socio no encontado")

def modificar_socio():
    numero=int(input("Ingrese número de socio a buscar: "))
    if numero in datosSocios:
        nombre=input("Ingrese nombre: ")
        edad=int(input("Ingrese edad: "))
        categoria=input("Ingrese categoría deportiva: ")

        datosSocios[numero]["nombre"]=nombre
        datosSocios[numero]["edad"]=edad
        datosSocios[numero]["categoria"]=categoria
    else:
        print("Socio no encontado")

def eliminar_socio():
    numero=int(input("Ingrese número de socio a buscar: "))
    if numero in datosSocios:
        socios.remove(numero)
        del datosSocios[numero]
        print("")
    else:
        print("Socio no encontado")

def mostrar_socios():
    if len(socios)==0:
        print("No existen datos.")
        return

    print("\nLISTADO DE SOCIOS")
    print("===================")
    for numero in socios:
        print("---------------")
        print("Número:", numero)
        print("Nombre:", datosSocios[numero]["nombre"])
        print("Edad:", datosSocios[numero]["edad"])
        print("Categoría:", datosSocios[numero]["categoria"])

def mostrar_estadisticas():
    if len(socios)==0:
        print("No existen datos")
        return

    total_socios=len(socios)

    suma_edades=0
    for numero in socios:
        suma_edades += datosSocios[numero]["edad"]
    promedio=suma_edades/total_socios

    mayo_numero = socios[0]
    mayor_edad= datosSocios[mayor_numero]["edad"]
    for numero in socios:
        edad_actual=datosSocios[numero]["edad"]
        if edad_actual>mayor_edad:
            mayor_edad=edad_actual
            mayor_numero=numero

    print("\nESTADÍSTICAS")
    print("========================")
    print("Total socios:", total_socios)
    print("Edad promedio:", round(promedio, 2))
    print(
        "Socio de mayor edad:",
        datosSocios[mayor_numero]["nombre"],
        "(",
        mayor_edad,
        "años)"
    )


while True:
    print("\n===============")
    print("CLUB DEPORTIVO FUTURO")
    print("===============")
    print("1. Agregar socio")
    print("2. Buscar socio")
    print("3. Modificar socio")
    print("4. Eliminar socio")
    print("5. Mostrar todos los socios")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    menu=input("Eliga su opción: ")
    if "1" in menu:
        print("Ejecutando agregar_socio...")
        agregar_socio()
    elif "2" in menu:
        print("Ejecutando buscar_socio")
        buscar_socio()
    elif "3" in menu:
        print("Ejecutando modificar_socio")
        modificar_socio()
    elif "4" in menu:
        print("Ejecutando eliminar_socio")
        eliminar_socio()
    elif "5" in menu:
        print("Ejecutando mostrar_socios")
        mostrar_socios()
    elif "6" in menu:
        print("Ejecutando mostrar_estadisticas")
        mostrar_estadisticas()
    elif "7" in menu:
        print("Saliendo...")
        break
    else:
        print("Error. No ha seleccionado un número válido")

#Cambio para pull request
