# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:27:24 2023

@author: ACER
"""

class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.num_paginas = num_paginas

    def obtener_info(self):
        return f"Libro: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}\nAño de publicación: {self.anio_publicacion}\nNúmero de páginas: {self.num_paginas}"

    def esta_agotado(self):
        return "Agotado" if self.num_paginas == 0 else "Disponible"

    def anios_desde_publicacion(self, anio_actual):
        return anio_actual - self.anio_publicacion

    def cambiar_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        return f"El autor del libro ha sido cambiado a {self.autor}."

    def aumentar_paginas(self, cantidad_paginas):
        self.num_paginas += cantidad_paginas
        return f"Se han añadido {cantidad_paginas} páginas al libro. Ahora tiene {self.num_paginas} páginas."


libro1 = Libro(titulo="Nunca Fuimos Modernos", autor="Bruno Latour", genero="Sociología", anio_publicacion=1991, num_paginas=221)
print(libro1.obtener_info())
print("Estado:", libro1.esta_agotado())
print("Años desde la publicación:", libro1.anios_desde_publicacion(anio_actual=2023))
print(libro1.cambiar_autor("Latour Bruno"))
print(libro1.aumentar_paginas(25))
