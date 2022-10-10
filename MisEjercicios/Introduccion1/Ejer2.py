# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:29:06 2022

@author: rubca
"""

 
 #Obtener la suman de los n primeros números naturales
 
def SumaNpN(n):
    i=1
    suma=0
    for i in range(1,n+1):
        suma = suma + i 
        i=i+1
        
    return suma
 
if __name__=='__main__':
     
     print(SumaNpN(9))