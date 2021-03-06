# -*- coding: utf-8 -*-
import random
import math
from lrule import *
            
class Unit(object):

    def __init__(self, N=4, L=3, lrule=Hebbian):
        self.lrule = lrule()
        self.w = [random.randint(-L, +L) for _ in range(N)]
        self.L = L

    def __call__(self, x):
        h = 0
        for wi, xi in zip(self.w, x):
            h = h + (wi * xi)
        self.o = self._sgn(h)
        return self.o

    def _sgn(self, v):
        if v <= 0:
            return -1
        else:
            return 1

    def train(self, x, y):
        for i in range(len(self.w)):  
            wi = self.lrule(self.w[i], x[i], y, self.o)
            self.w[i] = self._adjust(wi)

    def _adjust(self, wi):
        if wi > self.L:
            return self.L
        elif wi < (-self.L):
            return -self.L
        else:
            return wi