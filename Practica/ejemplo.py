import datetime

class Temporizador:#se crea un objeto temporalizar 
    def __init__(self):
        self.inicio = datetime.datetime.now()#te dice la hora y fecha actual

    def tiempo_transcurrido(self):
        return datetime.datetime.now() - self.inicio #se resta la hora guardada al inicio.

def probar_temporizador():
    t = Temporizador()# aqui se pondra el temporalizador
    suma = sum(range(1_000_000))# Operación que queremos medir
    duracion = t.tiempo_transcurrido()
    print(f"Tiempo transcurrido: {duracion.total_seconds():.4f} segundos")

probar_temporizador()


import random

class JuegoDado:
    def __init__(self, caras=6):
        self.caras = caras<3 #guarda el número de caras del dado

    def lanzar(self):
        return random.randint(1, self.caras)#random.randint(a, b) devuelve un número entero aleatorio entre a y b, incluyendo ambos.
    

"""Esta función recibe un objeto JuegoDado y cuántas veces quieres lanzarlo.

   Usa un bucle for para repetir las tiradas.

   Muestra el resultado de cada una."""
def jugar(dado, tiradas=5):
    print(f"Lanzando un dado de {dado.caras} caras {tiradas} veces:")
    for i in range(tiradas):
        print(f"Tirada {i+1}: {dado.lanzar()}")

dado6 = JuegoDado()
jugar(dado6)



import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio#Guarda el radio del circulo ahi

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio

def mostrar_info_circulo(radio):
    c = Circulo(radio)
    print(f"Radio: {radio}")
    print(f"Área: {c.area():.2f}")
    print(f"Circunferencia: {c.circunferencia():.2f}")

mostrar_info_circulo(3)
