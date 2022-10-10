# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:52:56 2022

@author: rubca
"""

#Determinar si un número es primo

def EsPrimo(n):
    while n != 0:
        if n == 1:
            return None
        if n == 2:
            return True 
        
        if n%2 == 0:
            return False
    print (n)
    return True

#Problema Dani 

def EsPrimo2():
    n = int(input("Dime un nº: "))
    dv = 2 
    while n > dv:
        if n%dv == 0:
            print("El nº es divisible entre: ",dv)
            return False
        dv += 1
    return True
            
    
        
if __name__ == '__main__':
    
   #q = int(input("Introduzca el nº que desee para validar si es primo: "))
   #print(EsPrimo(q))
   
   print(EsPrimo2())
   
    