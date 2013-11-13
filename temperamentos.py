# Modulo "temperamentos"
# Conjunto de funciones utiles para afinaciones y temperamentos

import math

# Constantes

quinta_pitag = 3.0/2
q = quinta_pitag

tercera_justa = 5.0/4
t = tercera_justa

octava = 2
o = octava

coma_pitag = (3.0/2)**12 / 2**7
cp = coma_pitag

coma_sint = (3.0/2)**4 / (5.0/4)**4
cs = coma_sint

diesis = coma_sint**3 / coma_pitag
die = diesis

fi = (math.sqrt (5) + 1) / 2

def cents (inter):
    return math.log(inter, math.pow (2.0, (1.0 / 1200)))


def pitch_pipe (pitch, temp_ideal, temp):
    return (pitch * math.sqrt (1.4 * 8.314 * (273.15 + temp) /
    28.95 * 10**-3)
    /
    math.sqrt (1.4 * 8.314 * (273.15 + temp_ideal) /
    28.95 * 10**-3))

def divide_inter (a, b, n_divisiones, division):
	return float(a) / math.pow(float(a)/b,1.0/n_divisiones)**division






	
