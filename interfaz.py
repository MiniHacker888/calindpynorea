import calculadora

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nCalculadora de Índices Corporales")
    print("1. Calcular Índice de Masa Corporal (IMC)")
    print("2. Calcular Índice de Grasa Corporal (IGC)")
    print("3. Calcular Tasa Metabólica Basal (TMB)")
    print("4. Salir")

def solicitar_datos_basicos():
    """Solicita el peso y la altura al usuario."""
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    return peso, altura

def calcular_y_mostrar_imc():
    """Solicita datos, calcula y muestra el IMC."""
    print("\n📌 Cálculo del Índice de Masa Corporal (IMC)")
    peso, altura = solicitar_datos_basicos()
    imc = calculadora.calcular_imc(peso, altura)
    print(f"Su IMC es: {imc}")

def calcular_y_mostrar_igc():
    """Solicita datos, calcula y muestra el IGC."""
    print("\n📌 Cálculo del Índice de Grasa Corporal (IGC)")
    peso, altura = solicitar_datos_basicos()
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (M/F): ").strip().lower()
    imc = calculadora.calcular_imc(peso, altura)
    igc = calculadora.calcular_igc(imc, edad, sexo)
    print(f"Su IGC es: {igc}%")

def calcular_y_mostrar_tmb():
    """Solicita datos, calcula y muestra la TMB."""
    print("\n📌 Cálculo de la Tasa Metabólica Basal (TMB)")
    peso, altura = solicitar_datos_basicos()
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (M/F): ").strip().lower()
    tmb = calculadora.calcular_tmb(peso, altura, edad, sexo)
    print(f"Su TMB es: {tmb} calorías/día")
