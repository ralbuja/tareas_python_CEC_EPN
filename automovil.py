# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:31:34 2023

@author: ACER
"""

class Automovil:
    def __init__(self, marca, modelo, color, anio_fabricacion, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio_fabricacion = anio_fabricacion
        self.kilometraje = kilometraje

    def obtener_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nAño de fabricación: {self.anio_fabricacion}\nKilometraje: {self.kilometraje} km"

    def encender(self):
        return "El automóvil está encendido."

    def apagar(self):
        return "El automóvil está apagado."

    def recorrer(self, distancia):
        self.kilometraje += distancia
        return f"Se ha recorrido {distancia} km. El kilometraje actual es {self.kilometraje} km."

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        return f"El color del automóvil ha sido cambiado a {self.color}."

    def calcular_antiguedad(self, anio_actual):
        return anio_actual - self.anio_fabricacion



auto1 = Automovil(marca="Ford", modelo="Fiesta", color="Verde", anio_fabricacion=2006, kilometraje=235000)
print(auto1.obtener_info())
print("Estado:", auto1.encender())
print(auto1.recorrer(120))
print(auto1.cambiar_color("Rojo"))
print("Antigüedad:", auto1.calcular_antiguedad(anio_actual=2023))
