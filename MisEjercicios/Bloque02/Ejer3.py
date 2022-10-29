# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:13:56 2022

@author: rubca
"""
import numpy as np 
#Hallar el producto escalar de dos vectores predefinidos por el usuario 

def prescalar(a,b):
    suma = 0 
    ne1 = a.shape[0]
    ne2 = b.shape[0]
    
    if not ne1 == ne2:
        return None

    for i in ne1:
        suma = suma + a[i] * b[i]
    return suma

if __name__ == '__main__':

    a = np.array(input("Introducir el 1º vector: ")) 
    b = np.array(input("Introducir el 2º vector: "))   
    print(prescalar(a,b))          
