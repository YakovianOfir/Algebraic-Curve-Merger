from CartesianProduct import CartesianProduct
from GeometricLine import GeometricLine
from FiniteField import FiniteField
from numpy import ndarray


class HermitianCurve:

    def __init__(self, p: int):
        self._universe = HermitianCurve.CreateUniverse(p)
        self._curve = HermitianCurve.AnalyzeCurve(p)
        assert len(self._universe) == p ** 4
        assert len(self._curve) == p ** 3
        self.show()

    @staticmethod
    def CreateUniverse(p: int) -> CartesianProduct:
        Fq = FiniteField(p, 2)
        assert len(Fq) == p ** 2
        return CartesianProduct(Fq, Fq)

    @staticmethod
    def AnalyzeCurve(p: int) -> ndarray:
        universe = HermitianCurve.CreateUniverse(p)
        # print("Constructing Hermitian curve. Fq -> \n{}".format(str(universe.X)))

        curve = []
        for i, j in universe.P:
            x, y = universe.get(i, j)
            xt = universe.X.traceElement(x)
            yn = universe.Y.normElement(y)
            if xt == yn:
                # print("Found Hermitian curve point -> ({}, {})".format(str(x), str(y)))
                curve.append((x, y))

        return curve

    def show(self):
        lines = []
        for p1 in self._curve:
            for p2 in self._curve:
                if p1 == p2:
                    continue
                if p1[0] == p2[0]:
                    continue
                line = GeometricLine(p1, p2)
                # print("Found Hermitian line -> ({})".format(line))
                lines.append(line)

        for line in lines:
            count = 0
            if line.slope() == 0:
                continue
            for p in self._curve:
                if line.contains(p):
                    count = count + 1
            print("Found Hermitian intersection -> (L: {}) (I: {})".format(line, count))


