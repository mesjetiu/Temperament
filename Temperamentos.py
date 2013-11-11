# -*- coding: utf-8 -*-

# Conjunto de funciones utiles para afinaciones y temperamentos

import math

coma_pitag = (3.0/2)**12 / 2**7

coma_sint = (3.0/2)**4 / (4*(5.0/4))

diesis = coma_sint**3 / coma_pitag

fi = (math.sqrt (5) + 1) / 2

def to_cents (inter):
    return math.log(inter, math.pow (2.0, (1.0 / 1200)))

def pitch_pipe (pitch, temp_ideal, temp):
    return (pitch * math.sqrt (1.4 * 8.314 * (273.15 + temp) /
    28.95 * 10**-3)
    /
    math.sqrt (1.4 * 8.314 * (273.15 + temp_ideal) /
    28.95 * 10**-3))

def divide_inter (a, b, n_divisiones, division):
	return float(a) / math.pow(float(a)/b,1.0/n_divisiones)**division





	
