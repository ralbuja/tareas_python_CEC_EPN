# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:22:41 2023

@author: Rommel Albuja
"""


def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio_actual=2023
anios_para_verificacion=30

for i in range (anio_actual, anio_actual + anios_para_verificacion): 
    if es_bisiesto(i): 
        print(f"El año {i} si es bisiesto")
    else: 
        print(f"El año {i} no es bisiesto.")


testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = es_bisiesto(yr)
            if result == testResults[i]:
                        print("OK")
            else:
                        print("Failed")