import interfaz

def main():
    while True:
        interfaz.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            interfaz.calcular_y_mostrar_imc()
        elif opcion == "2":
            interfaz.calcular_y_mostrar_igc()
        elif opcion == "3":
            interfaz.calcular_y_mostrar_tmb()
        elif opcion == "4":
            print("Saliendo... Gracias por usar la calculadora.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
