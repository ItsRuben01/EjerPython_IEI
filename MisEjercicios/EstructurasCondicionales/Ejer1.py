# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:31:25 2022

@author: rubca
"""

#Calcular el producto de todos los números perfectos de un nº q determinado

def DivisoresQ(q):
    Li = [] #Creamos una lista para almacenar todos los números perfectos posteriormente
    for i in range(1,q+1):
        if q%i == 0:
            Li.append(i)
    return Li
 
def productoNPerf(q):
    Li2 = DivisoresQ(q)
    x = 0
    for i in Li2:  

        Producto = x*i
        x = x+1
    return Producto
  
if __name__=='__main__':
    
   #print(DivisoresQ(50))
   #print(productoNPerf(50))
   print(PrdQpN(5))