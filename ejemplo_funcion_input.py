# -*- coding: utf-8 -*-
"""
Created on Sat May 27 20:54:59 2023

@author: danny
"""

nombre=input('Ingrese su nombre: ')
apellido=input('Ingrese su apellido: ')
ubicacion=input('imgrese la ciudad donde se ubica: ')
edad=int(input('Ingrese su edad: '))
if edad>=0 and edad<=100:
    print('Su nombre es',nombre, apellido,',','se encuentra en la ciudad de',ubicacion,'y su edad es ',edad ,'años' )
else:
    print('Edad incorrecta,ingrese nuevamente sus datos')