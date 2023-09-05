#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:44:07 2023

@author: katedremur
"""

import numpy as np
def posicion(A,k,m,t):
    '''
    Esta función retorna la posición, x, en un tiempo de de una masa m atada a un
    resorte de constante de fuerza k que inicialmente es desplazada A unidades de
    su posición de equilibrio. Esta función devuelve el resultado de 

    $A\sin (\omega t)$ donde $\omega = \sqrt{\frac{k}{m}}$

    Parámetros
    ----------
    A: float
        La amplitud o desplazamiento inicial de la masa.
    k: float
        La constante de fuerza del resorte.
    m: float
        La masa del objeto.
    t: float
        El tiempo en el cual se quiere calcular la posición.
    '''
    omega = np.sqrt(k/m)

    
    return A*np.sin(omega*t)

h =3

def DerivadaDerecha(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x))/h
        
    return d
def DerivadaIzquierda(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x) - f(x-h))/h
        
    return d
def DerivadaCentral(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x-h))/(2*h)
        
    return d
    
    



"t=np.linspace(0,10, 10)"