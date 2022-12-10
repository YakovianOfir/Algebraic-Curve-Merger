from FiniteField import FiniteField
from GammaWeights import GammaWeights
from galois import FieldArray


class GeometricLine:

    def __init__(self, p1, p2, field: FiniteField, gammas: GammaWeights):
        self._p1 = p1
        self._p2 = p2
        assert p1 != p2
        self._gammas = gammas
        self._line = self._calculateLineElements(field)

    def _first(self):
        return self._p1

    def _second(self):
        return self._p2

    def _n(self) -> FieldArray:
        v1 = tuple(map(lambda p: (self._gammas.g2() * ((self._gammas.g1() - self._gammas.g2()) ** -1)) * p, self._p1))
        v2 = tuple(map(lambda p: (self._gammas.g1() * ((self._gammas.g2() - self._gammas.g1()) ** -1)) * p, self._p2))
        n = tuple(map(lambda x, y: x + y, v1, v2))
        return n

    def _slope(self) -> FieldArray:
        v1 = tuple(map(lambda p: ((self._gammas.g1() - self._gammas.g2()) ** -1) * p, self._p1))
        v2 = tuple(map(lambda p: ((self._gammas.g2() - self._gammas.g1()) ** -1) * p, self._p2))
        slope = tuple(map(lambda x, y: x + y, v1, v2))
        return slope

    def _calculateLineElements(self, field: FiniteField) -> [FieldArray]:
        les = []
        for fe in field.elements:
            ls = tuple(map(lambda p: fe * p, self._slope()))
            ln = tuple(map(lambda p: (-1) * p, self._n()))
            le = tuple(map(lambda x, y: x + y, ls, ln))
            les.append(le)
        return les

    def contains(self, p: FieldArray) -> bool:
        return p in self._line

    def __str__(self):
        return \
            "[({}) -> ({})] == [y = ({})u - ({})]".format(
                str(self._p1),
                str(self._p2),
                str(self._slope()),
                str(self._n()))

    p1 = property(_first)
    p2 = property(_second)
