# -*- coding: utf-8 -*-
import random
import math

class LearningRule:

    def step(self, y, o):
        if (y * o) <= 0:
            return 0
        else:
            return 1


class Hebbian(LearningRule):
    def __call__(self, w, x, y, o):
        return w + (x * y) * self.step(y, o)


class AntiHebbian(LearningRule):
    def __call__(self, w, x, y, o):
        return w - (x * y) * self.step(y, o)


class RandomWalk(LearningRule):
    def __call__(self, w, x, y, o):
        return w + x * self.step(y, o)