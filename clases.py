from objeto import *
class Estructura:

    def __init__(self, palabra, lienzo):
        self.palabra = palabra
        self.lienzo = lienzo

    def mostrar(self):
        x1=400
        y1=2
        x2=450
        y2=52
        for e in self.palabra:
            self.lienzo.create_rectangle(x1, y1, x2, y2, width=5)
            self.lienzo.create_text(x1+25,y1+25,fill="darkblue",font="Times 20 italic bold",
                        text=e)
            x1+=50
            x2+=50

class Pila(Estructura):

    def __init__(self, palabra, lienzo):
        self.palabra = palabra
        self.lienzo = lienzo
        self.pila = []

    def mostrar(self, x1, y1, x2, y2, e):
        self.pila.append(Objeto(self.palabra[e],
        self.lienzo.create_text(x1+25,y1+25,fill="darkblue",font="Times 20 italic bold",text=self.palabra[e]),
        self.lienzo.create_rectangle(x1, y1, x2, y2, width=5)))
