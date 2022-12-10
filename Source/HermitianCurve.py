from CartesianProduct import CartesianProduct
from GeometricLine import GeometricLine
from FiniteField import FiniteField
from numpy import ndarray


class HermitianCurve:

    def __init__(self, p: int):
        self._universe = HermitianCurve._CreateUniverse(p)
        self._curve = HermitianCurve._AnalyzeCurve(self._universe)
        assert len(self._universe) == p ** 4
        assert len(self._curve) == p ** 3

    @staticmethod
    def _CreateUniverse(p: int) -> CartesianProduct:
        Fq = FiniteField(p, 2)
        assert len(Fq) == p ** 2
        return CartesianProduct(Fq, Fq)

    @staticmethod
    def _AnalyzeCurve(universe: CartesianProduct) -> ndarray:
        print("Constructing Hermitian curve. [Fq] -> \n{}".format(str(universe.X)))
        curve = []
        for i, j in universe.P:
            x, y = universe.get(i, j)
            xt = universe.X.traceElement(x)
            yn = universe.Y.normElement(y)
            if xt == yn:
                print("Found Hermitian curve point. -> ({}, {})".format(str(x), str(y)))
                curve.append((x, y))
        return curve

    def getLines(self) -> [GeometricLine]:
        lines = []
        for p1 in self._curve:
            for p2 in self._curve:
                if p1 == p2:
                    continue
                if p1[0] == p2[0]:
                    continue
                line = GeometricLine(p1, p2)
                print("Found Hermitian curve line. -> ({})".format(line))
                lines.append(line)
        return lines

    def getCurve(self):
        return self._curve
