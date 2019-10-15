import random  #Se importa la libreria random para generar numeros aleatorios

"""
Se define la clase nodo en el que toma como parametro el dato (en el metodo constructor)
que en este caso esta vacio y por consiguiente su nodo siguiente es nulo.
"""
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

"""
Se agrega la clase ListaCircular en el que no tiene un principio ni un fin, 
es por eso que se le agrega nulo al primero y al ultimo nodo.
"""
class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    """
    Metodo "Vacio" en el que indica si la lista esta vacia,
    regresa que el primer nodo no tiene elementos.
    """
    def Vacia(self):
        return self.primero == None

    """
    Metodo para asignar un dato al inicio del nodo,
    agregando una condicion para saber si la lista esta vacia y si no realiza las instrucciones.
    """
    def AgregarInicio(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    """
    Metodo para mandar llamar al primer nodo para que asi 
    la lista se considere circular.
    """
    def AgregarFinal(self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    """
    Metodo para realizar el recorrido, en el que se implementa las instrucciones para
    generar una nueva lista en el que se le van agregar los valores negativos de la lista original.
    """
    def Recorrer(self):
        aux = self.primero
        Cola_negativa = "Los numero negativos son: "
        negativos = ListaCircular()

        while aux:
            print(aux, aux.dato, aux.siguiente)
            if aux.dato < 0:
                negativos.AgregarFinal(aux.dato)
                Cola_negativa = str(Cola_negativa) + str(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
        print(Cola_negativa)

    """
    Metodo para remover el inicio del nodo, considerando tambien 
    si la lista esta vacia mediante una condicion if.
    """
    def RemoverInicio(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    """
    Metodo para remover el fin del nodo, en el que tambien se le aplica 
    la condicion para saber si la lista esta vacia.
    """
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


Lista = ListaCircular()  #Se le asigna el nombre al objeto de la clase "ListaCircular()"

"""
Se implementa un ciclo for, en el que se le agrega un tamaño de 100 numeros aleatorios,
mandando llamar al metodo "AgregarFinal" agregandolo asi a una nueva lista considerando la variable c
y por ultimo se realiza el recorrido.
"""
for a in range(1, 100):
    c = random.randint(-25, 25)
    Lista.AgregarFinal(c)
Lista.Recorrer()
