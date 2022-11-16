#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct 28 12:23:45 2022

@author: rubca
"""

import math 

# =============================================================================
#  EJERCICIO 1
# =============================================================================

def divydivis(divdn,divis):
    '''

    Problema 1: Diseñe e implemente una función donde dados dos números, un dividendo y un divisor, devuelva el
    resultado de la división, comprobando antes si el divisor es cero.

    Parameters
    ----------
    
    divdn :  Float
        Dividendo.
        
    divis : Float
        Divisor.

    Returns
    -------
    None.

    '''
    if divis == 0:
        print("ERROR DE DIVISIÓN POR CERO")
    else:
        print("\nDividendo", divdn, "\nDivisor", divis, "\nEl resultado es:", divdn/divis)
        # or 
       #print(f"{divdn}/{divis} = {divdn/divis}")
        
        
# =============================================================================
#  EJERCICIO 2
# =============================================================================

def empresa(ing,gast):
    '''
    Problema 2: Dise˜ne una función donde dadas dos variables de tipo entero, que representan los ingresos y gastos de una
    empresa, calcule los beneficios de la empresa y en caso de ser positivos imprima “La empresa es solvente”,
    si es cero imprimir “Se ha alcanzado el punto de equilibrio” y si es negativo imprimir “La empresa está en
    números rojos”. Ademas la función debe de devolver +1, 0 o -1 con cada una de las situaciones planteadas.
        
    Parameters
    ----------
    ing : float
        Ingresos de la empresa.
    gast : float
        Gastos de la empresa.

    Returns
    -------
    int
        Retorna el número 0 o -1 para diferenciar entre beneficios y banca rota.

    '''
    if ing > gast: 
        return 1
    elif ing == gast:
        return 0 
    else:
        return -1
    
      
# =============================================================================
#  EJERCICIO 3
# =============================================================================
        
def orden(a,b,c):
    '''
    Problema 3: Escribir una función donde dados tres meros detecte si se han introducido en orden creciente. La función
    debe de devolver este resultado.

    Parameters
    ----------
    
    a : int
        1º numero.
    b : int
        2º numero.
    c : int
        3º numero.
    
    
    Returns
    -------
    a : int
        Retorna el 1º número.
    b : int
        Retorna el 2º número.
    c : TYPE
        Retorna el 3º número.
        
        Además de un print diferenciando si los números están en orden creciente o está desordenada

    '''
    if a < b and b < c:
        print("La función se ha introducido en orden creciente")
        return a,b,c
    else:
        print("La función esta desordenada")
        return a,b,c
        
        
# =============================================================================
#  EJERCICIO 4
# =============================================================================
              
def semana(a):
    '''
    Problema 4: Escribir una función en la que dando un número del 1 a 7 devuelva el correspondiente día de la semana.

    Parameters
    ----------
    a : int
        Número entero que se iguala al día de la semana

    Returns
    -------
    None.

    '''
    
    if a == 1:
       print("Lunes")
   
    elif a == 2:      
       print("Martes")
   
    elif a == 3:
       print("Miércoles")
   
    elif a == 4:
       print("Jueves")
   
    elif a == 5: 
       print("Viernes")
   
    elif a == 6:
       print("Sábado")
   
    elif a == 7:
       print("Domingo")
   
    else: 
       print("No es un día de la semana válido")
  
  
# =============================================================================
#  EJERCICIO 5
# =============================================================================
def menu(): 
    '''
    Problema 5: Realizar un funci´on que muestre un men´u principal con las siguientes opciones. En funci´on de la respuesta
    del usuario se imprimir´a por pantalla la opci´on seleccionada. En caso de pulsar otra opci´on distintas a las
    mostradas imprimir “Esta opci´on no est´a disponible”. Utilice para ello esquemas iterativos y condicionales.

    Returns
    -------
    None.

    '''
    print ("\n\tMenú Principal"
               "\n\n1.Cargar fichero de datos"
               "\n2.Almacenar fichero de datos"
               "\n3.Modificar datos"
               "\n4.Salir")
        
# =============================================================================
#  EJERCICIO 6
# =============================================================================        
def tabla(n):  
    '''
    Problema 6: Escriba una funci´on donde dado un n´umero natural presente por pantalla su tabla de multiplicar

    Parameters
    ----------
    n : int
        Número ingresado por parte del usuario para desarrollar la tabla 

    Returns
    -------
    None.

    '''
    for i in range(1,11):
        prd = i * n
        print("La tabla de multiplicar del",n,"x",i," == ",prd)   
        
# =============================================================================
#  EJERCICIO 7
# =============================================================================

def sumaN(a,b):
    '''
    Problema 7: Escriba una funci´on para sumar los n´umeros enteros entre dos n´umeros enteros dados. Utilice para su
    implementaci´on dos posibilidades a seleccionar: un bucle for y un bucle while.

    Parameters
    ----------
    a : int 
       Número que define el rango junto a 'b'
    b : int
       Número que define el rango junto a 'a'

    Returns
    -------
    suma : int
       suma de los números enteros 

    '''
    suma = 0
    
    for i in range(a,b+1):
        suma = suma + i 
    return suma
    
# =============================================================================
#  EJERCICIO 8
# =============================================================================

def factorial(n):
    '''
    Problema 8: Escribir una funci´on que calcule el factorial de un número n ≥ 0.

    Parameters
    ----------
    n : int
        número entero ingresado por el usuario para calcular el factorial.

    Returns
    -------
    int
        producto escalar.

    '''
    s = 0 
    
    while n >= 0:
 
        if n == 0: 
            return 1
        
        for i in range(1,n):
            prd = n * i
            s = s + prd
     
        return s

#   OTRA OPCIÓN

def factorial1(n):
    '''
    Problema 8: Escribir una funci´on que calcule el factorial de un número n ≥ 0.

    Parameters
    ----------
    n : int
        número entero ingresado por el usuario para calcular el factorial.

    Returns
    -------
    int
        producto escalar.


    '''
    while n > 0:
        if n == 0: 
            return 1
        
        for i in range(1,n):     
            prd = n * math.factorial(i)  
        return prd 
    
# =============================================================================
#  EJERCICIO 9
# =============================================================================

def calculadoraN(v1):
    '''
    Problema 9: Escriba una funci´on que calcule y visualice el m´as grande, el m´as peque˜no y la media de N n´umeros. Los
    valores se solicitar´an al invocar la funci´on y los n´umeros ser´an introducidos por el usuario. La solicitud
    de los n´umeros lo implementa con un bucle while. Cuando el usuario introduzca un 0 el programa dejar´a de pedir n´umeros.

    Parameters
    ----------
    v1 : int
        Valor ingresado por el usuario para evaluar el maximo y el minimo.

    Returns
    -------
    float
        Retorna el min, el max y la media de los valores.

    '''
    
    maximo = float('-inf')
    minimo = float('inf')
    suma = 0 
    
    for i in range(v1+1):
        
        suma = suma + i
        
        if maximo < i:
            maximo = i
            
        if minimo > i:
            minimo = i 
            
    return minimo, maximo, (suma/v1) 
   
        
# =============================================================================
#  EJERCICIO 10
# =============================================================================
def esPerfecto(n):
    '''
    Problema 10: Escriba una función que determine si un número entero dado es perfecto o no. Se dice que un número es
    perfecto cuando es igual a la suma de sus divisores, excluido el mismo. Por ejemplo, 6 es perfecto, ya que
    6 = 1 + 2 + 3.

    Parameters
    ----------
    n : int
        Entrada del usuario para definir un número entero y evaluar si es perfecto o no.

    Returns
    -------
    bool
        Devuelve el valor True o False diferenciando entre nº perfecto o no.

    '''
    divisores = []

    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)

    if sum(divisores) == n: 
        return True
    else:
        return False

# =============================================================================
#  EJERCICIO 11
# =============================================================================   
def productoDig(a):
    '''
    Problema 11: Escriba una función que calcule el producto de los dígitos de un número entero. Por ejemplo con el número
    123 el producto sería 1 ∗ 2 ∗ 3 = 6.

    Parameters
    ----------
    a : int
        Número entero dado por el usuario.

    Returns
    -------
    producto : int
        Producto de cada uno de sus dígitos.

    '''
    ne = str(a)
    producto = 1 
    
    if a == 0:
        return None
    
    for i in ne:
        producto = producto * int(i)
    return producto

# OTRA OPCIÓN 

def productoDigII(a):
    '''
    
    Problema 11: Escriba una función que calcule el producto de los dígitos de un número entero. Por ejemplo con el número
    123 el producto sería 1 ∗ 2 ∗ 3 = 6.

    Parameters
    ----------
    a : int
        Número entero dado por el usuario.

    Returns
    -------
    producto : int
        Producto de cada uno de sus dígitos.

    '''
    producto = 1 
    while a > 0: 
        for i in str(a):
            producto = producto * int(i) 
        return producto 

    
if __name__ == '__main__':

    ejer = int(input("\nIntroduzca un ejercicio: "))
    
    if ejer == 1:
        
        a = float(input("Introduzca el dividendo: "))
        b = float(input("Introduzca el divisor: "))
        print(divydivis(a,b))
        
    elif ejer == 2:
        
        a = float(input("Introduzca los ingresos: "))
        b = float(input("Introduzca los gastos: "))
        empresa(a,b)
        if empresa == 1:
            print("La empresa es solvente")
        elif empresa == 0:
            print("La empresa se encuentra en un punto de equilibrio")
        else:
            print("La empresa está en nº rojos")
            
    elif ejer == 3:
        
        a = int(input("Primero número: "))
        b = int(input("Segundo número: "))
        c = int(input("Tercer número: "))
        print(orden(a,b,c))
              
    elif ejer == 4:
        
        a = float(input("Introduzca un nº: "))
        print(semana(a))
        
    elif ejer == 5:
        salir = False
        
        while not salir:        
            print(menu())
            n = int(input("\n\nDime tu opción : "))
         
            if n == 1:
                print("Cargar fichero de datos")
            elif n == 2:
                print("Almacenar fichero de datos")
            elif n == 3:
                print("Modificar datos")
            elif n == 4: 
                salir = True
                print("Saliendo de la interfaz")
            else:
                print("Está opción no está disponible")
                
    elif ejer == 6:
         q = int(input("Introduzca un nº natural: "))
         print(tabla(q))
         
    elif ejer == 7: 
         a = int(input("Primero número: "))
         b = int(input("Segundo número: "))
         print(sumaN(a,b))
         
    elif ejer == 8: 
        #q = int(input("Introduzca un nº natural: "))
        #print(factorial(q))
        
        q = int(input("Introduzca un nº natural: "))
        print(factorial(q))   
        
    elif ejer == 9:
        
        valor = int(input("Introduzca un número: "))
       
        salir = False

        while not salir:
            if valor != 0:
                print(calculadoraN(valor)) 
                valor = int(input("Introduzca un número: "))
            else:
                salir = True
      
    elif ejer == 10:
        a = int(input("Introduzca un nº: "))
        print(esPerfecto(a))
        
    elif ejer == 11:
        
        a = int(input("1º Forma = Introduzca un número: "))
        print(productoDig(a))
        
        # 2º FORMA
        
        a = int(input("2º Forma = Introduzca un número: "))
        print(productoDigII(a))
        
