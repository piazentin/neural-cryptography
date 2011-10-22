# -*- coding: utf-8 -*-
import random
import math

class LearningRule:

    def degrau(self, y, o):
        if (y * o) <= 0:
            return 0
        else:
            return 1

class Hebbian(LearningRule):
    def __call__(self, w, x, y, o):
        return w + (x * y) * self.degrau(y, o)

class AntiHebbian(LearningRule):
    def __call__(self, w, x, y, o):
        return w - (x * y) * self.degrau(y, o)

class RandomWalk(LearningRule):
    def __call__(self, w, x, y, o):
        return w + x * self.degrau(y, o)