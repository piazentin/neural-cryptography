# -*- coding: utf-8 -*-
import random
import math
from treinamento import *
from unidade import Unidade

class TreeParityMachine(object):
    '''
    Esta classe representa uma rede neural Tree Parity Machine
    '''

    def __init__(self, unidades, entradas, lrule=Hebbian, wrange=9):
        '''
        Aqui instanciamos uma rede neural com K hidden units (unidades ocultas)
        cada uma com N entradas (input neurons), e definimos a regra de aprendizagem que será usada,
        por padrão a regra de Hebb (Hebbian).
        A função de ativação padrão é a função degrau (Step ou Threshold).
        Os valores máximos e mínimos dos pesos da rede são números discretos e são definidos 
        pela propriedade pesoss_range (L), com o máximo sendo +L e o mínimo -L.
        '''
        self.unidades = []
        self.formato = (unidades, entradas)
        self.saida = None
        for unidade in range(unidades):
            self.unidades.append(Unidade(entradas, lrule, wrange))


    def __call__(self, entradas):
        '''
        Neste método o vetor de entrada da rede neural é recebido e processado na rede.
        A saída então é retornada.
        '''
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
        if self.saida == saida:
            return True
        else:
            return False

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


if __name__ == "__main__":
    Cripto();

class Cripto(object):
    def criar_tpm(self, n, e):
        self.n = n
        self.e = e
        self.tpm = TreeParityMachine(n,e, wrange=1)

    def gerar_entradas(self):
        self.entradas = [[-1,1][random.randint(0,1)] for whatever in range(self.n*self.e)]

    def __init__(self, n, e):
        self.criar_tpm(n, e)

    def calcular_saida(self, entradas):
        self.entradas = entradas
        self.saida = self.tpm(entradas)
        return self.saida

    def treinar(self):
        self.tpm.treinar(self.entradas)