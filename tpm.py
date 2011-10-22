# -*- coding: utf-8 -*-
import random
import math
from treinamento import *
from unidade import Unidade

class TreeParityMachine(object):

    def __init__(self, units, inputs, lrule=Hebbian, L=6):
        self.unidades = []
        self.formato = (units, inputs)
        self.saida = None
        for unit in range(units):
            self.unidades.append(Unidade(inputs, L, lrule))

    def __call__(self, entradas):
        self.saida = 1
        entradas = self._quebrar(entradas, self.formato[1])
        for unidade, entradasn in zip(self.unidades, entradas):
            self.saida = self.saida * unidade(entradasn)
        return self.saida
    
    def _quebrar(self, lista, tamanho):
        offset = 0
        chunks = []
        for i in range(len(lista)/tamanho):
            chunk = []
            for j in range(tamanho):
                chunk.append(lista[offset + j])
            offset = offset + j + 1
            chunks.append(chunk)
        return chunks

    def ativacao(self, saida):
        return (self.saida == saida)

    def treinar(self, entradas):
        entradas = self._quebrar(entradas, self.formato[1])
        for unidade, entrada in zip(self.unidades, entradas):
            unidade.treinar(entrada, self.saida)

    def pesos(self):
        w = []
        for unidade in self.unidades:
            for wi in unidade.w:
                w.append(wi)
        return w

    def saidas(self):
        w = []
        for unidade in self.unidades:
                w.append(unidade.o)
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
        self.tpm.treinar(self.entradas)
