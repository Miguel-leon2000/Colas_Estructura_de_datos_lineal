import random  #Se importa la libreria random para generar numeros aleatorios

class GenerarNumeros():

    def NumerosAleatorios(self):
        c = []
        for a in range(0, 100):
            b = random.randint(-25, 25)
            c.append(b)
        print(c)

        d = []
        for x in range(0, len(c)):
            if c[x] < 0:
                d.append(c[x])
        print(d)

class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        return self.primero == None

    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def AgregarFinal(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def RemoverInicio(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def RemoverFin(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.primero = aux

Generar = GenerarNumeros
Generar.NumerosAleatorios(GenerarNumeros)
