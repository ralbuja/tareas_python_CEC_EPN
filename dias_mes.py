# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:40:26 2023

@author: Rommel Albuja
"""

import calendar
# He utilizado la función calendar para obtener el número de días en el mes


#
# Codigo from LAB Listas y return
#


def daysInMonth(year, month):

    numberDays = calendar.monthrange(year, month)[1]
    return numberDays

year = 2023
month = 2

numberDays = daysInMonth(year, month)
print(f"El número de días en el mes {month} del año {year} es: {numberDays}")


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
              yr = testYears[i]
              mo = testMonths[i]
              print(yr, mo, "->", end="")
              result = daysInMonth(yr, mo)
              if result == testResults[i]:
                            print("OK")
              else:
                            print("Failed")
                            
                            