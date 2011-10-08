# -*- coding: utf-8 -*-
import random
import math
from treinamento import *
            
class Unidade(object):
    ''' 
    Esta classe implementa uma unidade da Tree Parity Machine e
    é uma rede neural Feed Forward com N entradas e 1 saída
    '''

    def __init__(self, x, lrule=Hebbian, L=9):
        '''
        Aqui ocorre a criação de uma unidade da TPM
        parameters:
            inputs: o número de entradas que a unidade possui
            lrule: a regra de apredizagem que será usada
            wrange: número discreto que define os valores máximos e mínimos dos ws da rede
        '''
        self.lrule = lrule()
        self.w = [random.randint(-L, +L) for x in range(x)]
        self.L = L

    def sinal(self, v):
        '''
        Função sgn
        '''
        if v <= 0:
            return -1
        else:
            return 1

    def __call__(self, x):
        '''
        Este método usa as entradas para alimentar a TPM
        '''
        h = 0
        for wi, xi in zip(self.w, x):
            h = h + (wi * xi)
        h = h / math.sqrt(len(self.w))
        self.o = self.sinal(h)
        return self.o

    def treinar(self, x, y):
        for i in range(len(self.w)):      
            self.w[i] = self.ajustar(self.lrule(self.w[i], x[i], y, self.o))

    def ajustar(self, wi):
        if wi > self.L:
            return self.L
        elif wi < (-self.L):
            return -self.L
        else:
            return wi