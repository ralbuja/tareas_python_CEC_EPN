# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 08:25:14 2023

@author: Rommel Albuja
"""

import calendar


# Prueba de error 1
#anio = 2023
#mes = 113
#dia= 31


testYears = [2020, 2021, 2022, 2023, 2024, 2025]
testMonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
testDays = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

def daysInMonth(year, month):
    numberDays = calendar.monthrange(year, month)[1]
    return numberDays

def dayOfYear(anio, mes, dia):
    try:
        if not (1 <= mes <= 12) or not (1 <= dia <= 31):
            return None
        if dia > calendar.monthrange(anio, mes)[1]:
            return None
        return calendar.monthrange(anio, mes)[1]
    except ValueError:
        return None


#prueba
numeroDia = dayOfYear(testYears[2], testMonths[5], testDays[28])
print(numeroDia)

if numeroDia is not None:
    print(f"El mes {testMonths[5]} del año {testYears[2]} tiene {numeroDia} días.")
else:
    print("Los argumentos ingresados son inválidos.") 

    