# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:52:56 2022

@author: rubca
"""
# I Método (más desarollado) 

def NFibonnacci(n):
    Li = [0,1]
    
    pn, ult = 0,1
    a = 1
    c = 1 #contador
    while c < n:
        ult = a 
        a = pn + ult
        Li.append(a)
        pn = ult
        print (ult,a)
        c+=1
    return Li
            

# II Método (más optimizado)

def NFibonnacci2(n):
    Li = [0,1]
    cont = 1
    
    while cont < n:
        for i in range(2,n+1):
            nval = Li[i-2] + Li[i-1]
            Li.append(nval)
            cont+=1
        return Li
    
# III Método (++ optimizado)

def NFibonnacci3(n):
    Li = [0,1]
    cont = 1

    while cont < n:
        for i in range(2,n+1):
            Li.append(Li[i-2] + Li[i-1])
        return Li; cont +=1


if __name__ == '__main__':
    
    q = int(input("Introduzca un nº: "))
    #print(NFibonnacci(q))
    print(NFibonnacci3(q))