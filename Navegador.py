class Navegador:
    def __init__(self):
        self.historial = []  # Pila para el historial
        self.avance = []     # Pila para el avance (opcional)

    def visitar_pagina(self, url):
        self.historial.append(url)
        # Limpiar la pila de avance al visitar una nueva página
        self.avance.clear()

    def retroceder(self):
        if len(self.historial) > 1:  # Al menos una página anterior
            pagina_actual = self.historial.pop()
            self.avance.append(pagina_actual)
            return self.historial[-1]  # Retorna la página anterior
        else:
            print("No hay más páginas a las que retroceder.")
            return None

    def avanzar(self):
        if self.avance:
            pagina_siguiente = self.avance.pop()
            self.historial.append(pagina_siguiente)
            return pagina_siguiente
        else:
            print("No hay más páginas a las que avanzar.")
            return None

    def mostrar_historial(self):
        if not self.historial:
            print("El historial está vacío.")
        else:
            print("Historial de navegación:")
            for url in self.historial:
                print(url)

    def borrar_historial(self):
        self.historial.clear()
        self.avance.clear()
        print("Historial borrado.")

# Función principal para interactuar con el usuario
def menu():
    navegador = Navegador()
    while True:
        print("\n1. Visitar nueva página")
        print("2. Retroceder página")
        print("3. Avanzar página")
        print("4. Mostrar historial")
        print("5. Borrar historial")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            url = input("Ingrese URL: ")
            navegador.visitar_pagina(url)
        elif opcion == "2":
            pagina = navegador.retroceder()
            if pagina:
                print(f"Retrocediendo a: {pagina}")
        elif opcion == "3":
            pagina = navegador.avanzar()
            if pagina:
                print(f"Avanzando a: {pagina}")
        elif opcion == "4":
            navegador.mostrar_historial()
        elif opcion == "5":
            navegador.borrar_historial()
        elif opcion == "6":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa
menu()
