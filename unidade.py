# -*- coding: utf-8 -*-
import random
import math
from treinamento import *
            
class Unidade(object):
    ''' 
    Esta classe implementa uma unidade da Tree Parity Machine e
    é uma rede neural Feed Forward com N entradas e 1 saída
    '''

    def __init__(self, N=4, L=3, lrule=RandomWalk):
        self.lrule = lrule()
        self.w = [random.randint(-L, +L) for _ in range(N)]
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