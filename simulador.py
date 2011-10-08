from tpm import *

n = 16
e = 16
c = 0
i = 0

while i < 100:
	i = i + 1
	A = Cripto(n,e)
	B = Cripto(n,e)

	contador = 0
	t = 0
	sinc = 0
	while sinc < 30:
		A.gerar_entradas(n,e)
		t = t + 1
		A.calcular_saida(A.entradas)
		B.calcular_saida(A.entradas)

		if A.saida == B.saida:
			A.treinar()
			B.treinar()
			sinc = sinc + 1
			contador = contador + 1
		else:
			sinc = 0

	if A.tpm.pesos() == B.tpm.pesos():
		c = c + 1


print c
