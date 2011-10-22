from tpm import *
import time

K = 4
N = 3
L = 3

c = 0
i = 0

def calc_distance(xi, yi):
	d = 0
	for x, y in zip(xi, yi):
		d = d + abs(x - y)
	return d

for N in [3,4,5]:
	print "-------------------------------------------"
	print N
	print "-------------------------------------------"
	i = 0
	while i < 200:
		i = i + 1
		A = TreeParityMachine(K, N, L)
		B = TreeParityMachine(K, N, L)
		contador = 0
		t = 0
		sinc = 0
		start = time.time()
		while sinc < 100:
			A.generate_inputs()
			t = t + 1
			A(A.x)
			B(A.x)

			if A.activation(B.y):
				A.train(A.x)
				B.train(A.x)
				contador = contador + 1
			else:
				sinc = 0

			if A.weights() == B.weights():
				print t, "\t", (time.time() - start)
				break;
