# -*- coding: utf-8 -*-
import random
import math
from lrule import *
from unit import Unit


class TreeParityMachine(object):

    def __init__(self, K=3, N=4, L=3, lrule=Hebbian):
        self.units = []
        self.K = K
        self.N = N
        self.y = None
        for unit in range(K):
            self.units.append(Unit(N, L, lrule))

    def __call__(self, x):
        self.y = 1
        self.x = x
        x = self._chunks(x, self.N)
        for unit, xi in zip(self.units, x):
            self.y = self.y * unit(xi)
        return self.y
    
    def _chunks(self, l, chunk_size):
        offset = 0
        chunks = []
        for i in range(len(l)/chunk_size):
            chunk = []
            for j in range(chunk_size):
                chunk.append(l[offset + j])
            offset = offset + j + 1
            chunks.append(chunk)
        return chunks

    def activation(self, y):
        return (self.y == y)

    def train(self, x=None):
        x = x or self.x
        x = self._chunks(x, self.N)
        for unit, xi in zip(self.units, x):
            unit.train(xi, self.y)

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

    def generate_inputs(self):
        self.x = [[-1,1][random.randint(0,1)] for whatever in range(self.K * self.N)]
        return self.x
