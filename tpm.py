# -*- coding: utf-8 -*-
import random
import math
from lrule import *
from unit import Unit

class TreeParityMachine(object):

    def __init__(self, K, N, lrule=Hebbian, L=6):
        self.units = []
        self.K = K
        self.N = N
        self.y = None
        for unit in range(K):
            self.units.append(Unit(N, L, lrule))

    def __call__(self, x):
        self.y = 1
        x = self._chunks(x, self.N)
        for unit, xi in zip(self.units, x):
            self.y = self.y * unit(xi)
        return self.y
    
    def _chunks(self, lista, tamanho):
        offset = 0
        chunks = []
        for i in range(len(lista)/tamanho):
            chunk = []
            for j in range(tamanho):
                chunk.append(lista[offset + j])
            offset = offset + j + 1
            chunks.append(chunk)
        return chunks

    def ativacao(self, y):
        return (self.y == y)

    def train(self, x):
        x = self._chunks(x, self.N)
        for unit, xi in zip(self.units, x):
            unit.treinar(xi, self.y)

    def weights(self):
        w = []
        for unit in self.units:
            for wi in unit.w:
                w.append(wi)
        return w

    def outputs(self):
        w = []
        for unit in self.units:
                w.append(unit.o)
        return w


if __name__ == "__main__":
    Cripto();

class Cripto(object):
    def criar_tpm(self, n, e, L=3):
        self.n = n
        self.e = e
        self.tpm = TreeParityMachine(n,e, L=L)

    def gerar_entradas(self):
        self.entradas = [[-1,1][random.randint(0,1)] for whatever in range(self.n*self.e)]

    def __init__(self, n, e, L=3):
        self.criar_tpm(n, e, L)

    def calcular_saida(self, entradas):
        self.entradas = entradas
        self.saida = self.tpm(entradas)
        return self.saida

    def treinar(self):
        self.tpm.train(self.entradas)
