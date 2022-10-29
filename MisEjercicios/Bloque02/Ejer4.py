# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:27:23 2022

@author: rubca
"""
import random 

def PrIn(v1,v2): #Tu suerte es parte del azar
    print(random.randrange(v1,v2))  
    
def ejer6(n):    
# 6. Escriba una funci´on donde dado un n´umero natural presente por pantalla su tabla de multiplicar.

    for i in range(1,11):
        prd = i * n
        print("La tabla de multiplicar del",n,"x",i," == ",prd)
        
if __name__ == '__main__':
    ejer = int(input("Introduzca el nº del ejercicio: "))
    
    if ejer == 1:
        q = int(input("Introduzca un nº natural: "))
        print(ejer6(q))
    elif ejer == 2:
        v1 = (int(input("Introduzca su 1º valor: ")))
        v2 = (int(input("Introduzca su 2º valor: ")))
        PrIn(v1,v2)
    
    
    
    
    
    
    
    
    
    
    