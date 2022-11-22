#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:48:43 2022

@author: george
"""

"""Vpython es una biblioteca que tiene funciones gráficas.
Para importar la biblioteca usamos import.
El asterisco se traduce como importa TODO."""
from vpython import * #Desde vpython importa TODO

ball = sphere(pos = vector(-3,-3,0),
             color = color.orange,
             radius = 0.5)
velocity = vector(3,1.5,4)
arrow(pos = ball.pos, 
     axis = velocity,
     color = color.green)