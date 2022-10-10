# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:54:13 2022

@author: rubca
"""

#Problema: Obtener la suman de los n primeros números naturales

def suma(n):
 suma=0
 i=1
 
 while i<n+1:
     suma=suma+i
     print(suma,i)
     i=i+1
 return suma


# Determina si un número n es par o impar.
# Devuelve True si el número es par y False si el número en impar

def NumeroPar(n):
    if(n%2 == 0):
        return True
    return False

# Determina si un número n es par o impar.
# Devuelve True si el número es par y False si el número en impar.

def NumeroParOImpar(n):
   while n > 2: 
       if(n%2 == 0):
           print("El número es", n ,"PAR")
           return True
       else:
           print("El número es", n ,"IMPAR")
       return False
    






if __name__=='__main__':
    
 print(suma(6))  
 #print(NumeroPar(4))
 #print(NumeroParOImpar(8))