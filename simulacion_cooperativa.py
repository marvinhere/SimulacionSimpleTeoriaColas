# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:16:38 2020

@author: Marvin Quiñónez
"""
import time
from os import system

def factorial(n):
   fact = 1
   for num in range(2, n + 1):
       fact *= num
   return fact

def unServidor(l,u):
    lq=(l**2)/(u*(u-l))
    ws=1/(u-l)
    r = [round(lq),ws]
    return r

def muchosServidores(s,l,u):
    lq1=(l/u)**(s+1)
    lq2=factorial(s-1)*((s-(l/u))**2)
    lq= po(s,l,u)*(lq1/lq2)
    ls=lq+(l/u)
    ws=ls/l
    r = [round(lq),ws]
    return r

def po(s,l,u):
    abajo = 0    
    for x in range(0, s+1):
        r=((l/u)**x)/factorial(x)
        abajo = abajo+r  
    abajo3=(1/(1-(l/(s*u))))
    resultado = 1/(abajo*abajo3)
    return resultado
    
        


print('Con solo una caja')

uS = unServidor(11,12)
print('Tiempo promedio en cola',uS[1],'hr')

for x in range(0, uS[0]):
    print([],end="")
    time.sleep(1)


print('\n\n Con dos cajas')
array = []
mS = muchosServidores(2,11,12)
print('Tiempo promedio en cola',mS[1],'hr')

for x in range(0, mS[0]+1):
    print([])


    
