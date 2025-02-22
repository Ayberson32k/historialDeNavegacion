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