# Modulo "temperamentos"
# Conjunto de funciones utiles para afinaciones y temperamentos

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
q = cents(quinta_pitag)

tercera_justa = 5.0/4
t = cents(tercera_justa)

octava = 2
o = cents(octava)

coma_pitag = (3.0/2)**12 / 2**7
cp = cents(coma_pitag)

coma_sint = (3.0/2)**4 / (5.0/4)**4
cs = cents(coma_sint)

diesis = coma_sint**3 / coma_pitag
die = cents(diesis)

fi = (math.sqrt (5) + 1) / 2

def T12_cents (_quintas, redondeo = 2):
	if len(_quintas) != 12:
		print "Error: No se han introducido 12 valores para las quintas."
		return
	_T12 = []
	_suma = 0
	for i in range(len(_quintas)):
		if _quintas[i] == 'l' or _quintas[i] == 'L':
			_T12.append ('lobo')
			continue
		_suma = (_suma + q + _quintas[i]) % 1200
		_T12.append (_suma)		
	_T12_orden = [_T12[6], _T12[1],  _T12[8], _T12[3], _T12[10], _T12[5], _T12[0], _T12[7], _T12[2], _T12[9], _T12[4], _T12[11]]
	for i in range(12):
		_T12_orden[i] = _T12_orden[i] - ((i+1)*100)%1200
	#print _T12_orden
	_T12_orden.insert(0, _T12_orden[-1])
	#print _T12_orden
	del _T12_orden[-1]
	if round(_T12_orden[0],5) != 0:
		print "Error: El circulo de quintas no se cierra."
		return
	# Poner LA como referencia, a 0.0 cents
	la_dif = 0 - _T12_orden[9]
	for i in range(len(_T12_orden)):
		_T12_orden[i] = _T12_orden[i] + la_dif
	# Redondeo
	for i in range(len(_T12_orden)):
		_T12_orden[i] = round (_T12_orden[i], redondeo)
	print _T12_orden
	
	
t = -cp/12
temp = [t,cp,t,t,t,t,t,t,t,t,t,t]
pit = [-cp,0,0,0, 0,0,0,0, 0,0,0,0]
T12_cents (pit)
