# -*- coding: utf-8 -*-

#Problema: Obtener la suman de los n primeros números naturales
#Análisis:
    #Ejemplo: Obtner la suma de los 3 primeros números naturales
    # suma = 1 + 2 +3 
    #Entrada: n=3
    #Salida: 6
    #Documentar: pydoc -w ej-pr02.py ./
    
def sumaNpnn(n):
    '''
    Obtener la suman de los n primeros números naturales

    Parameters
    ----------
    n : TYPE integer
        DESCRIPTION.
        Número natural para obtener la suma de los primero n naturales
    Returns
    -------
    suma : TYPE Ineger
        DESCRIPTION.
        Suma
    '''
    i=1
    suma=0
    while i<n+1:#Mientras i menor 5
        suma= suma+i
        print (i,suma)
        i=i+1
    return suma

def sumaN(n):
    '''
    Obtener la suman de los n primeros números naturales mediante una estructura iterativa tipo for

    Parameters
    ----------
    n : TYPE Entero
        DESCRIPTION.
   
    Returns
    -------
    suma : TYPE Entero
        DESCRIPTION.
        Devuelve la suma de los primeros números naturales
    '''
    suma=0 #Inicia la variables suma con valor 0
    for i in range(1,n+1): #Para n=3 range(1,n+1) =[1,2,3]
        suma=suma+i #Acumula en la variable suma el resultado de la suma
        print (i,suma) #Muestra ppr pantalla el valor de la suma
    return suma #Devuelve el valor de la suma

def par(n):
    '''
    Determina si un número n es par o impar.
    Devuelve True si el número es par y False si el número en impar.

    Parameters
    ----------
    n : TYPE Integer
        DESCRIPTION.
         
    Returns
    -------
    bool 
        DESCRIPTION.
        Devuelve True si el número es par y False si el número en impar.
    '''
    if n%2==0: #Esteuctura algoritmica condicional
        return True
    else:
        return False

def parB(n):
    '''
    Determina si un número n es par o impar.
    Devuelve True si el número es par y False si el número en impar.

    Parameters
    ----------
    n : TYPE Integer
        DESCRIPTION.
         
    Returns
    -------
    bool 
        DESCRIPTION.
        Devuelve True si el número es par y False si el número en impar.
    '''
    
    while n>2: 
        n=n-2
        print (n)
    if n==2:
        return True
    else:
        return False
    

if __name__=='__main__':
    s=sumaNpnn(3)
    #sumaN(3)
    #print (parB(7))