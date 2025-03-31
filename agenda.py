import json

# =============================
#    MI AGENDA DE PELÍCULAS
# =============================
# Autor: [Tu Nombre]
# Descripción: Programa para gestionar una agenda de películas.
# Permite agregar, mostrar, buscar y eliminar películas guardadas en un archivo JSON.

# Archivo donde se almacenarán los datos
AGENDA_FILE = "agenda_peliculas.json"

# -------------------------------
# FUNCIONES PARA GESTIONAR PELÍCULAS
# -------------------------------

def cargar_peliculas():
    """Carga la lista de películas desde un archivo JSON."""
    try:
        with open(AGENDA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna una lista vacía si el archivo no existe o está dañado

def guardar_peliculas(peliculas):
    """Guarda la lista de películas en un archivo JSON."""
    with open(AGENDA_FILE, "w", encoding="utf-8") as file:
        json.dump(peliculas, file, indent=4, ensure_ascii=False)

def agregar_pelicula():
    """Permite al usuario agregar una nueva película."""
    titulo = input("Ingrese el título de la película: ").strip()
    genero = input("Ingrese el género: ").strip()
    año = input("Ingrese el año de estreno: ").strip()
    director = input("Ingrese el director: ").strip()
    
    pelicula = {"Título": titulo, "Género": genero, "Año": año, "Director": director}
    peliculas = cargar_peliculas()
    peliculas.append(pelicula)
    guardar_peliculas(peliculas)
    print(f"Película '{titulo}' agregada con éxito.\n")

def mostrar_peliculas():
    """Muestra todas las películas guardadas en la agenda."""
    peliculas = cargar_peliculas()
    if not peliculas:
        print("No hay películas en la agenda.")
    else:
        print("\n🎬 LISTA DE PELÍCULAS 🎬")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula['Título']} ({pelicula['Año']}) - {pelicula['Género']} - Dirigida por {pelicula['Director']}")

def buscar_pelicula():
    """Busca una película por su título."""
    titulo = input("Ingrese el título de la película a buscar: ").strip().lower()
    peliculas = cargar_peliculas()
    encontrados = [p for p in peliculas if p["Título"].lower() == titulo]
    
    if encontrados:
        print("\n🔍 RESULTADOS DE LA BÚSQUEDA 🔍")
        for pelicula in encontrados:
            print(f"Título: {pelicula['Título']}\nGénero: {pelicula['Género']}\nAño: {pelicula['Año']}\nDirector: {pelicula['Director']}\n")
    else:
        print("Película no encontrada.")

def eliminar_pelicula():
    """Elimina una película por su título."""
    titulo = input("Ingrese el título de la película a eliminar: ").strip().lower()
    peliculas = cargar_peliculas()
    peliculas_filtradas = [p for p in peliculas if p["Título"].lower() != titulo]
    
    if len(peliculas) == len(peliculas_filtradas):
        print("No se encontró la película para eliminar.")
    else:
        guardar_peliculas(peliculas_filtradas)
        print(f"Película '{titulo}' eliminada con éxito.")

# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------

def menu():
    """Muestra el menú y gestiona la selección del usuario."""
    while True:
        print("\nMI AGENDA DE PELÍCULAS")
        print("1. Agregar película")
        print("2. Mostrar todas las películas")
        print("3. Buscar película")
        print("4. Eliminar película")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            buscar_pelicula()
        elif opcion == "4":
            eliminar_pelicula()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# -------------------------------
# EJECUCIÓN DEL PROGRAMA
# -------------------------------

if __name__ == "__main__":
    menu()
