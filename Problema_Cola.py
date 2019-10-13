import random  #Se importa la libreria ramdom para generar numeros aleatorios

class GenerarNumeros(): #Se crea la clase

    """
    Ciclo for en el que toma un tamaño de 100 numeros aleatorios,
    en el rango de -25 a 25
    """
    for a in range(0, 100):
        contador = a  #Se agrega un contador para cada elemento (para verificar)
        b = random.randint(-25, 25)
        print(b)
        contador += 1
        print("Numero: ", contador)