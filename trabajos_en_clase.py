# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Rommel Albuja

Ejercicios Varios...
"""

# x=5
# x+4
# x+2.5
# resultado1 = x+2.5
# resultado2 = x//2
# txt = "Cisco"
# opt = txt*x
# print ("\n") 
# print ("\t")


# =============================================================================
# aclNum = int (input("Ingrese el número de ACL: "))
# if aclNum >= 1 and aclNum <= 99:
#     print("Es una ACL estandar.")
# elif aclNum >=100 and aclNum <= 199:
#     print("Es una versión extendida.")
# else:
#     print("El número ingresado no es un ACL.")
#     
# =============================================================================
    
# =============================================================================
# print ("Programa identificación de condición de una persona según su edad")
# edad = int(input("Cuál es la edad? "))
# if edad >= 1 and edad <= 10:
#     print ("La persona es un infante")
# elif edad > 10 and edad <=17:
#     print ("La persona es un adolescente")
# elif edad > 17 and edad <=30:
#     print ("La persona es un adulto joven")
# elif edad > 30 and edad <=65:
#     print ("La persona es un adulto")
# elif edad > 65 and edad <=100:
#     print ("La persona es un adulto mayor")
# else: 
#     print ("El valor ingresado supera la expectativa de vida humana, contacte a los Records Guinness")
# 
# =============================================================================


# =============================================================================
# lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# 
# for item in lista1:
#     print (item)
# for i in range(1, 16+1,1):
#         print(i, end=" * ")
# =============================================================================

# =============================================================================
# listar=[]
# listas=[]
# listaap=[]
# listaf=[]
# listap=[]
# lista=["R1", "R2", "R3", "S1", "S2", "S3", "AP1", "AP2", "AP3","FW1", "PC1", "PC2"]
# for elemento in lista:
#     if "R" in elemento:
#         listar.append(elemento)
#     elif "S" in elemento:
#         listas.append(elemento)
#     elif "AP" in elemento:
#         listaap.append(elemento)
#     elif "FW" in elemento:
#         listaf.append(elemento)
#     elif "PC" in elemento:
#         listap.append(elemento)
# print(listar)
# =============================================================================


# matriz = [[1,2,3],[4,5,6][7,8,9]]        
# for j in range(1, 3+1, 1):
#     for k in range (1,3+1,1):
#         print (j, k)


# =============================================================================
# contar=input("Ingrese el número al que debo contar: ")
# contar = int(contar)
# contador = 1
# while contador <= contar:
#     print(contador)
#     contador += 1
# =============================================================================



# =============================================================================
# contar=input("Ingrese el número al que debo contar: ")
# contar = int(contar)
# contador = 1
# while True:
#     print(contador)
#     contador += 1
#     if contador > contar:
#         break
# =============================================================================


# =============================================================================
# while True:
#     x=input("Ingrese un número a contar: ")
#     if x == 'q' or x == 'quit':
#         break
#     x=int (x)
#     y=1
#     while True:
#         print(y)
#         y=y+1
#         if y>x:
#             break
# =============================================================================


# =============================================================================
# def mensaje():
#      print("Escriba un mensaje: ")
#      
# mensaje()
# a = int (input())
# print (a)
# 
# mensaje() 
# b = int(input())
# print(b)
# =============================================================================


# =============================================================================
# def saludo(nombre):
#     print ("Hola", nombre)
# 
# saludo("Rommel")
# 
# 
# def saludo2(nombre, apellido):
#     print("Hola", nombre, apellido)
#     
# saludo2("Rommel", "Albuja")
# 
# 
# def saludo3(nombre="CEC", apellido="EPN"):
#     print("Hola", nombre, apellido)
#     
# saludo3()
# 
# 
# def direccion (ciudad,barrio,calle):
#     print("La dirección de entrega es: ")
#     print("La ciudad es:", ciudad)
#     print("El barrio es:", barrio)
#     print("La calle de referencia es", calle)
#     
# ci=input ("Ingrese la ciudad de entrega: ")
# ca=input ("Ingrese la calle de referencia: ")
# ba=input ("Ingrese el barrio: ")
# direccion (ci,ba,ca)
# =============================================================================


# =============================================================================
# def resta (a,b):
#     print (a-b)
#     print ("\n")
# 
# resta(5,2)
# resta(2,5)
# resta (a=5, b=2)
# resta (5, b=2)
# =============================================================================


# =============================================================================
# def multiply (a=5, b=3):
#     print ("El resultado de multiplicar a * b s:",  a*b)
#     return (a*b)
# 
# 
# print (multiply())
# 
# resultado = multiply(10,5)
# print(type(resultado))
# opt = resultado+1
# print(opt)
# =============================================================================


# =============================================================================
# def funlista (lista):
#     for item in lista:
#         print ("Hola", item)
#     print ("")
#     
# funlista(["Juan"])
# funlista(["Juan","Carlos"])
# funlista(["Juan","Carlos", "Alejandro"])
# =============================================================================



# =============================================================================
# def suma(*a):
#     print("\nTipo de datos del argumento:",
#          type(a))
#     sum = 0
#     for n in a:
#         sum +=n
#         #sum=sum+n
# 
#     print("Suma:",sum)
# suma(1)
# suma(5,8)
# suma(1,6)
# suma (2,8,10)
# suma(0,1)
# suma(1,2)
# suma(3,5)
# suma(4,5,6,7)
# suma(1,2,3,5,6)
# suma(1,2,3,5,6,7,8,9,10)
# suma(1,2,3,5,6,7,8,9,10,11,12,13,14)
# suma(1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17)
# =============================================================================

  


# =============================================================================
# def keyw(**datos):
#     print("\nTipo de datos del argumento:",
#           type(datos))
# 
#     for key, value in datos.items():
#         print("{} is {}".format(key,value))
# 
# keyw(Firstname="Juan", 
#      Lastname="DomÃ­nguez", 
#      Age=42, 
#      Phone=1234567890)
# keyw(Firstname="John", 
#      Lastname="Wood",
#      Email="johnwood@nomail.com",
#      Country="Wakanda", 
#      Age=25, 
#      Phone=9876543210)
# keyw(Firstname="Rommel",
#      Secondname="Rodrigo",
#      Lastname="Albuja",
#      SecondLastName="Bolaños",
#      )
# 
# =============================================================================


# =============================================================================
# def crealista(n):
#     lista=[]
#     for item in range (n):
#         lista.append(item)
#     return lista
# print (crealista(10))
# =============================================================================




# =============================================================================
# def EsPrimo(numero):
# 
#     if numero < 2:
#         return False
# 
#     # Se verifica si el número es divisible por algún otro número menor que él
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
# 
#     return True
# 
# 
# for i in range(1, 40):
# 	if EsPrimo (i + 1):
# 			print(i + 1, end=" ")
# print()
# 
# =============================================================================



# =============================================================================
# def isPrime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
# 
#     return True
# #print (isPrime(7))
# 
# for i in range(1, 20):
# 	if isPrime(i + 1):
# 			print(i + 1,end=" ")
# print()
# =============================================================================



# =============================================================================
# def is_prime(x):
#     if x < 2:
#        
#         return False
#     elif x == 2:
#         
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True
# """
# w=is_prime()
# print(w)
# """
# for i in range(1, 20):
# 	if is_prime(i+1):
# 			print(i + 1, end=" ")
# print()
# =============================================================================


# =============================================================================
# 
# import math
# import sys
# 
# seno = math.sin(math.pi/2)
# print (seno)
# 
# =============================================================================


# =============================================================================
# from math import sin, pi
# 
# opt = sin(pi/2)
# print (opt)
# =============================================================================


# =============================================================================
# from math import *
# opt = sin(pi/2)
# print (opt)
# =============================================================================

import math

print ("INICIO")
try:
    print (1)
    x = 1/0
    print (2)

except ArithmeticError:
    print("Se presentó un error aritmético...")
except ZeroDivisionError:
    print("No se puede dividir para cero")
except ValueError:
    print("Se debe ingresar un dato entero")
except:    
    print ("Hey!!! parece que algo salió mal en el código")
    print ("3")

print ("FIN")






