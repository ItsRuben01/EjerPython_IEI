#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct 28 12:23:45 2022

@author: rubca

"""

import math 

# -----------------------------
#   EJERCICIO 1
# -----------------------------

def AreaPerimetroCuadrado(l):
    '''
    Función para calcular el área y el perímetro de un cuadrado

    Returns
    -------
    None.

    '''
    l = float(l)
    a = l * l 
    p = 4 * l
    return a,p 


# -----------------------------
#   EJERCICIO 2
# -----------------------------

def AreaPerimetroRect(b,h):
    '''
    Función para calcular el área y el perímetro de un rectángulo

    Returns
    -------
    None.

    '''
    b = float(b)
    h = float(h)
    a = b*h
    p = 2*b + 2*h
    return a,p


# -----------------------------
#   EJERCICIO 3
# -----------------------------

def areaTriang(b,h):
    '''
    Función para calcular el área y el perímetro de un triángulo usando base y altura

    Returns
    -------
    None.

    '''
    b = float(b)
    h = float(h)
    a = (b*h)/2
    return a


# -----------------------------
#   EJERCICIO 4
# -----------------------------ç

         
def areaPerimTriang(a,b,c):
    '''
    Función para calcular el área y el perímetro de un triángulo usando tres lados

    Returns
    -------
    None.

    '''
    
    s = (a+b+c)/2
    # Este ejercicio tiene 2 posibilidades para calcular su área
    # 1º Forma : Importamos el módulo "math"
    # y usamos la función sqrt
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    # 2º Forma: Hacemos la raíz pero elevada a 1/2
    A1 = (s*(s-a)*(s-b)*(s-c)) ** (1/2)   
    p = a+b+c 
    
    return A,p

    
# -----------------------------
#   EJERCICIO 5
# -----------------------------
   
def persona():
    '''
    Función para preguntar los datos de una persona y mostrarlos en pantalla

    Returns
    -------
    None.

    '''
    nombre = str(input("Introduzca su nombre: "))
    apellidos = str(input("Introduzca sus apellidos: "))
    edad = int(input("Introduzca su edad: "))
    altura = float(input("Introduzca su altura: "))
     
    print("\nSus datos son: ", "\n\nNombre:",nombre,"\nApellidos:", apellidos,"\nEdad:", edad,"\nAltura:", altura)
    
 
# -----------------------------
#   EJERCICIO 6
# -----------------------------

def AreaTrapecio(bmay,bmen,h):
    '''
    Función para calcular el área de un trapecio

     Returns
     -------
     None.

   '''
   
    a = ((bmay+bmen)*h)/2
    return a


# -----------------------------
#   EJERCICIO 7
# -----------------------------
def NumIntValor(a,b):
    '''
    Función para preguntar por dos números y mostrar sus valores intercambiados

    Returns
    -------
    None.

    '''
    print("El valor de A: ",a,"El valor de B: ",b)
    
    aux = a 
    a = b 
    b = aux
    
    print("El valor de A: ",a,"El valor de B: ",b)
    
# -----------------------------
#   EJERCICIO 8
# -----------------------------

def SegAHMinYSeg(s):
    '''
    Función para preguntar por horas, minutos y segundos y devolver su conversión a segundos

    Returns
    -------
    None.

    '''
    horas = s *(1/3600) 
    minutos = horas*(60)
    segundos = minutos*(60)
    print("\nHoras: ", horas, "\nMinutos: ", minutos,"\nSegundos: ", segundos)
  
    
# -----------------------------
#   EJERCICIO 9
# -----------------------------

def SegAHMinYSegII(s):
    '''
    Función para preguntar por segundos y mostrar su conversión a horas, minutos y segundos

    Returns
    -------
    None.

   '''
    horas = s *(1/3600) 
    minutos = horas*(60)
    segundos = minutos*(60)
    print('\nHoras: ', horas, "\nMinutos: ", minutos,"\nSegundos: ", segundos)


# -----------------------------
#   EJERCICIO 10
# -----------------------------

def CambioEuroAPeseta(e):
    '''
    Función para convertir euros a pesetas

    Returns
    -------
    None.

    '''
    p = 166.39 # 1 Euro es igual a 166,39 pesetas españolas
    c = e * p 
    return c 


# -----------------------------
#   BUCLE/PROGRAMA PRINCIPAL
# -----------------------------

if __name__ == '__main__':
    
    ejer = int(input("\nIntroduzca un ejercicio: "))
    
    if ejer == 1:
        
        q = float(input("Introduzca el lado de su cuadrado: "))
        print("El área y el perímetro del cuadrado son: ", AreaPerimetroCuadrado(q))
        
    elif ejer == 2: 
       
        b = float(input("Introduzca la base: "))
        h = float(input("Introduzca la altura: "))
        print("El área y el perímetro del rectángulo son: ", AreaPerimetroRect(b, h))
       
    elif ejer == 3: 
        
        b = float(input("Introduzca la base: "))
        h = float(input("Introduzca la altura: "))
        print("El área del triángulo es: ", areaTriang(b, h)) 
    
    elif ejer == 4: 
          
        a = float(input("Introduzca el 1º lado: "))
        b = float(input("Introduzca el 2º lado: "))
        c = float(input("Introduzca el 3º lado: "))
        print("El área y el perímetro del triángulo son: ", areaPerimTriang(a, b, c)) 
    
    elif ejer == 5:
        
       persona()
       
    elif ejer == 6: 
        
        bmay = float(input("Introduzca la base mayor: "))
        bmen = float(input("Introduzca la base menor: "))
        h = float(input("Introduzca la altura: "))
        print("El área del trapecio es: ", AreaTrapecio(bmay, bmen, h))
        
    elif ejer == 7: 
        
        a = float(input("Introduzca un número: "))
        b = float(input("Introduzca otro número: "))
        print(NumIntValor(a,b))
       
    elif ejer == 8: 
        
        s = int(input("Introduzca un número de segundos: "))
        print(SegAHMinYSeg(s))
       
    elif ejer == 9: 
          
        s = int(input("Introduzca un número de segundos: "))
        print(SegAHMinYSegII(s))
    elif ejer == 10: 
        e = float(input("Introduzca una cantidad de Euros: ")) 
        print(e,"€", "es igual que", CambioEuroAPeseta(e), "ESP")      
        
    else: 
        print("ERROR : No existe ningún ejercicio", ejer)
        
        
        
        
        
    
   
   
   
   
   
   
   
   
   
    
    
    