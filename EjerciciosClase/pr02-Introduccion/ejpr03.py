#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:04:44 2022

@author: acalvo
"""
import math

def sumaNpnn(n):#n=4
    '''
    Obtener la suman de los n primeros números naturales
    '''
    i=1#Dato extra que voy a necesitar
    suma=0 #Asigno valor inicia a la variable suma
    while i<n+1:#Mientras i menor 5
        suma= suma+i#Asigno a suma lo que haya 
                    #en suma mas i
        #print (i,suma)
        i=i+1
    return suma

def primo(n):
    for i in range(2,n):#n=9 [2,3,4,5,6,7,8]
        #print (i)
        if n%i==0:
            return False
    return True
    
    
def listaPrimosHastaQ(q):#q=7 [2,3,4,5,6,7]
    lp=[]#Inicia la lista lp vacía
    for i in range(2,q+1):
        if primo(i):#Si i es primo lo añado a la lista
            lp.append(i)
    return lp
    
    
    
    
    
    
    

def areaRectangulo(a,b):
    area=a*b
    return area



def areaCirculo(r):
    area=math.pi*r**2
    return area



if __name__=='__main__':
    
    #print (areaRectangulo(3,4))
    #print (areaCirculo(8))
    n=18
    #print ("es primo ",n,"?",primo(n))
    q=17
    print (listaPrimosHastaQ(q))
    
    #n=3
    #print ("La suma de los ", n," primeros numeros natulales es: ",sumaNpnn(n))
    pass