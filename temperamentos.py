# Modulo "temperamentos"

"""
Conjunto de funciones utiles para afinaciones y temperamentos.

La funcion mas compleja es T12_cents(list()).
Input: una lista con el temperamento de cada quinta en cents.
	Existe una serie de variables con contienen las principales comas
	expresadas en cents para facilitar la representacion tel temperamento.
	La quinta que contiene el resto acumulado en 11 quintas,
	o quinta del lobo se representa con la variable L y no es necesario
	conocer su valor previamente. El orden de las quintas parten de DO
	y finalizan en SI# (o DO enharmonico)
Output: La funcion devuelve otra lista que contiene la desviacion en cents
	de cada nota de la escala (de DO a SI) respecto al temperamento igual.

Ejemplo 1: Temperamento igual

t = cp/12							# quinta temperada = coma pitatorica / 12
TI = [t,t,t,t, t,t,t,t, t,t,t,t]
print T12_cents (TI)

Ejemplo 2: Temperamento pitagorico

TP = [0,0,0,0, 0,L,0,0, 0,0,0,0]		# La quinta del lobo se situa en SI - FA#
print T12_cents (TP)
"""
	

import math

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


# Constantes

quinta_pitag = 3.0/2
q = round(cents(quinta_pitag),4)

tercera_justa = 5.0/4
t = round(cents(tercera_justa),4)
octava = 2
o = round(cents(octava),4)

coma_pitag = (3.0/2)**12 / 2**7
cp = round(cents(coma_pitag),4)

coma_sint = (3.0/2)**4 / 2**2 / (5.0/4)
cs = round(cents(coma_sint),4)

diesis = coma_sint**3 / coma_pitag
die = round(cents(diesis),4)

fi = (math.sqrt (5) + 1) / 2

q_i = quinta_temperamento_igual = cp/12

L = l = 'lobo'

	
class Escala:
	def __init__ (self,
	notas = [q_i,q_i,q_i,q_i,q_i,q_i,q_i,q_i,q_i,q_i,q_i,q_i,], nombre,
	inicio = 0, referencia = 9):
		self.nombre = nombre
		self.notas = notas
		self.inicio = inicio
		self.referencia = referencia
	
	def get_nombre():
		return self.nombre
		
	def get_notas():
		return self.notas
		
	def get_inicio():
		return self.inicio
		
	def get_referencia():
		return self.referencia
		
	
	def set_nombre(nombre):
		self.nombre = nombre
		
	def set_notas(notas):
		self.notas = notas
		
	def set_inicio(inicio):
		self.inicio = inicio
		
	def set_referencia(referencia):
		self.referencia = referencia
	
	


def T12_cents (_quintas, redondeo = 2):
	
	if len(_quintas) != 12:
		print "Error: No se han introducido 12 valores para las quintas."
		return
	_T12 = []
	_suma = 0
	
	for i in range(len(_quintas)):
		if _quintas[i] == L:
			_T12.append ('lobo')
			continue
		_suma = (_suma + q + _quintas[i])
		_T12.append (_suma)	
		
	# Calculo de la quinta de lobo si la hay
	if 'lobo' in _T12:
		lobo = _T12[-1] + q - o*7
		print "lobo =", lobo
		punto_lobo = _T12.index('lobo')
		_T12[punto_lobo] = _T12[punto_lobo-1] + q - lobo
		for i in range(punto_lobo+1, len(_T12)):
			_T12[i] = _T12[i] + q - lobo
	
	# Reduccion a una octava
	for i in range(len(_T12)):
	
		_T12[i] = _T12[i] % 1200
	
	# Ordenacion por semitonos
	_T12_orden = [_T12[6], _T12[1],  _T12[8], _T12[3], _T12[10], _T12[5], _T12[0], _T12[7], _T12[2], _T12[9], _T12[4], _T12[11]]
	
	for i in range(len(_T12_orden)):
		_T12_orden[i] = _T12_orden[i] - ((i+1)*100)%1200

	_T12_orden.insert(0, _T12_orden[-1])
	del _T12_orden[-1]
	
	if round(_T12_orden[0],3) != 0:
		print "Error: El circulo de quintas no se cierra."
		return
		
	# Poner LA como referencia, a 0.0 cents
	la_dif = 0 - _T12_orden[9]
	for i in range(len(_T12_orden)):
		_T12_orden[i] = _T12_orden[i] + la_dif
		
	# Redondeo
	for i in range(len(_T12_orden)):
		_T12_orden[i] = round (_T12_orden[i], redondeo)
		
	return _T12_orden
	

