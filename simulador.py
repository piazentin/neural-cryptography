from tpm import *
import time

n = 4
#e = 3
L = 3
c = 0
i = 0

def calc_distance(xi, yi):
	d = 0
	for x, y in zip(xi, yi):
		d = d + abs(x - y)
	return d
for e in [3,4,5,8,16,32,64,128,256,512,1024]:
	print "-------------------------------------------"
	print e
	print "-------------------------------------------"
	i = 0
	while i < 200:
		i = i + 1
		A = Cripto(n,e, L)
		B = Cripto(n,e, L)
		contador = 0
		t = 0
		sinc = 0
		start = time.time()
		while sinc < 100:
			A.gerar_entradas()
			t = t + 1
			A.calcular_saida(A.entradas)
			B.calcular_saida(A.entradas)

			if A.saida == B.saida:
				A.treinar()
				B.treinar()
				contador = contador + 1
			else:
				sinc = 0

			if A.tpm.pesos() == B.tpm.pesos():
				print t, "\t", (time.time() - start)
				break;
