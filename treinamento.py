# -*- coding: utf-8 -*-
import random
import math

class LearningRule:

    def degrau(self, y, o):
        if (y * o) < 0:
            return 0
        else:
            return 1

class Hebbian(LearningRule):
    def __call__(self, w, x, y, o):
        nw = w
        if self.degrau(y, o):
            nw = w + (x * y)
        return nw

class AntiHebbian(LearningRule):
    def __call__(self, w, x, y, o):
        nw = w
        if self.degrau(y, o):
            nw = w - (x * o)
        return nw

class RandomWalk(LearningRule):
    def __call__(self, w, x, y, o):
        nw = w
        if self.degrau(y, o):
            nw = w + x
        return nw