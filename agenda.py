import datetime

# ========================
# GESTOR DE PELÍCULAS
# ========================
# Aplicación de consola para gestionar una agenda de películas con funciones avanzadas.
# Autor: [Tu Nombre]

# Base de datos de películas (simulada en una lista de diccionarios)
peliculas = [
    {"titulo": "Inception", "director": "Christopher Nolan", "genero": "Ciencia Ficción", "anio": 2010, "duracion": 148, "clasificacion": 13},
    {"titulo": "Get Out", "director": "Jordan Peele", "genero": "Terror", "anio": 2017, "duracion": 104, "clasificacion": 18},
    {"titulo": "Icarus", "director": "Bryan Fogel", "genero": "Documental", "anio": 2017, "duracion": 121, "clasificacion": 18},
    {"titulo": "Shrek", "director": "Andrew Adamson", "genero": "Animación", "anio": 2001, "duracion": 90, "clasificacion": 0}
]

# ==============================
# FUNCIÓN: PELÍCULA MÁS LARGA
# ==============================
def pelicula_mas_larga():
    pelicula = max(peliculas, key=lambda x: x["duracion"])
    print(f"\n🎥 La película más larga es '{pelicula['titulo']}' con {pelicula['duracion']} minutos de duración.\n")

# ===================================
# FUNCIÓN: DURACIÓN PROMEDIO (hh:mm)
# ===================================
def duracion_promedio():
    promedio = sum(p["duracion"] for p in peliculas) // len(peliculas)
    horas, minutos = divmod(promedio, 60)
    print(f"\nLa duración promedio de las películas es {horas:02}:{minutos:02}.\n")

# ========================================
# FUNCIÓN: PELÍCULAS ESTRENADAS DESPUÉS DE UN AÑO
# ========================================
def peliculas_estreno(anio):
    nuevas = [p["titulo"] for p in peliculas if p["anio"] > anio]
    print(f"\nPelículas estrenadas después de {anio}: {', '.join(nuevas) if nuevas else 'Ninguna'}\n")

# ====================================
# FUNCIÓN: CUÁNTAS PELÍCULAS SON +18
# ====================================
def peliculas_mayores_18():
    mayores = sum(1 for p in peliculas if p["clasificacion"] >= 18)
    print(f"\nEl número de películas 18+ es: {mayores}.\n")

# ==================================
# FUNCIÓN: REAGENDAR UNA PELÍCULA
# ==================================
def reagendar_pelicula(nombre, dia, hora, controlador):
    pelicula = next((p for p in peliculas if p["titulo"].lower() == nombre.lower()), None)
    if pelicula and controlador.upper() == "N":
        print(f"\nLa película '{nombre}' fue reagendada con éxito para {dia} a las {hora}.\n")
    else:
        print(f"\nLa película '{nombre}' no pudo ser reagendada.\n")

# ===========================================
# 👥 FUNCIÓN: REVISAR SI SE PUEDE INVITAR A ALGUIEN
# ===========================================
def se_puede_invitar(pelicula, edad, autorizacion):
    peli = next((p for p in peliculas if p["titulo"].lower() == pelicula.lower()), None)
    if not peli:
        print("\nPelícula no encontrada.\n")
        return
    
    if edad >= peli["clasificacion"] or (edad < peli["clasificacion"] and autorizacion.upper() == "S"):
        print("\nSe puede invitar la persona.\n")
    else:
        print("\nNo se puede invitar la persona.\n")

# ==================
# MENÚ PRINCIPAL
# ==================
def menu():
    while True:
        print("\n========== MENÚ ==========")
        print("1. Consultar película más larga")
        print("2. Consultar duración promedio")
        print("3. Consultar películas estreno")
        print("4. Consultar películas +18")
        print("5. Reagendar película")
        print("6. Revisar si se puede invitar a alguien")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            pelicula_mas_larga()
        elif opcion == "2":
            duracion_promedio()
        elif opcion == "3":
            anio = int(input("Ingresa el año: "))
            peliculas_estreno(anio)
        elif opcion == "4":
            peliculas_mayores_18()
        elif opcion == "5":
            nombre = input("Nombre de la película: ")
            dia = input("Día de la semana: ")
            hora = input("Hora (HHMM): ")
            controlador = input("¿Controlador de horario? (S/N): ")
            reagendar_pelicula(nombre, dia, hora, controlador)
        elif opcion == "6":
            nombre = input("Nombre de la película: ")
            edad = int(input("Edad del invitado: "))
            autorizacion = input("¿Autorización de los padres? (S/N): ")
            se_puede_invitar(nombre, edad, autorizacion)
        elif opcion == "0":
            print("\n¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el menú
menu()
