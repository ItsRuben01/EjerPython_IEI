# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:10:50 2022

@author: rubca
"""


def DivisoresQ(q):
    Li = [] #Creamos una lista para almacenar todos los números perfectos posteriormente
    for i in range(1,q+1):
        if q%i == 0:
            Li.append(i)
    return Li

 
''' Calcular el producto de los q primeros números perfectos '''

def PrdQpN(q):
    prd = 0
    
    for i in range(1,q):
        prd = prd + 1
        if DivisoresQ(i):
            prd = prd * i 
    return prd
   
if __name__=='__main__':
        
    print(PrdQpN(5))
   