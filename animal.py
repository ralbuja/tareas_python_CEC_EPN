# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:19:42 2023

@author: ACER
"""

class Animal:
    def __init__(self, nombre, especie, edad, color, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.peso = peso

    def comer(self, comida):
        return f"{self.nombre} está comiendo {comida}."

    def hacer_sonido(self, sonido):
        return f"{self.nombre} hace {sonido}."

    def envejecer(self):
        self.edad += 1
        return f"{self.nombre} ha envejecido un año. Ahora tiene {self.edad} años."

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"{self.nombre} ahora tiene un pelaje de color {self.color}."

    def pesar(self):
        return f"{self.nombre} pesa {self.peso} kilogramos."

perro = Animal(nombre="Carbón", especie="Canino", edad=3, color="negro", peso=25)
print(perro.comer("galletitas"))
print(perro.hacer_sonido("ladridos"))
print(perro.envejecer())
print(perro.cambiar_color("negro"))
print(perro.pesar())
