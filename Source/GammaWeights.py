from galois import FieldArray

from FiniteField import FiniteField
from random import choice


class GammaWeights:

    def __init__(self, field: FiniteField):
        self._gammas = GammaWeights.AnalyzeGammaElements(field)

    def g1(self) -> FieldArray:
        return self._gammas[0]

    def g2(self) -> FieldArray:
        return self._gammas[1]

    @staticmethod
    def RandomizeFieldElement(field: FiniteField) -> FieldArray:
        return choice(field.elements)

    @staticmethod
    def AnalyzeGammaElements(field: FiniteField):
        g1, g2 = GammaWeights.RandomizeFieldElement(field), 0
        while True:
            g2 = GammaWeights.RandomizeFieldElement(field)
            if g1 != g2:
                break
        return g1, g2
