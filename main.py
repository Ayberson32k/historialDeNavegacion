class Navegador:
    def __init__(self):
        self.historial = []  # Pila para el historial
        self.avance = []     # Pila para el avance (opcional)

def visitar_pagina(self, url):
    self.historial.append(url)
    # Limpia la pila de avance al visitar una nueva pagina
    self.avance.clear()

def retroceder (self):
    if len(self.historial) > 1: #verifica si existe pagina anteriormente
        pagina_actual = self.historial.pop()
        self.avance.append(pagina_actual)
        return self.historial[-1] #regresa a la pagina anterior
    else:
        print("No existen paginas anteriores.")
        return None
    
def avanzar(self):
    if self.avance:
        pagina_siguiente = self.avance.pop()
        self.historial.append(pagina_siguiente)
        return pagina_siguiente
    else:
        print("No hay paginas siguientes.")
        return None

def borrar_historial(self):
        self.historial.clear()
        self.avance.clear()
        print("Historial borrado.")

# Menu de usuario
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
