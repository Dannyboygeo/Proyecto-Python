# -*- coding: utf-8 -*-
"""
Created on Sun May 28 07:12:53 2023

@author: danny
"""

anio=int(input('Ingrese el anio a convertir: '))
if anio%4==0 and anio%400==0:
    print('Verdadero')
else:
    print('Falso')
        
