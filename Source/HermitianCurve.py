
from CartesianProduct import CartesianProduct
from FiniteField import FiniteField
from numpy import ndarray


class HermitianCurve:

    def __init__(self, p: int):
        self._universe = HermitianCurve.CreateUniverse(p)
        self._curve = HermitianCurve.AnalyzeCurve(p)
        assert len(self._universe) == p ** 4
        assert len(self._curve) == p ** 3

    @staticmethod
    def CreateUniverse(p: int) -> CartesianProduct:
        Fq = FiniteField(p, 2)
        assert Fq.size() == p ** 2
        return CartesianProduct(Fq, Fq)

    @staticmethod
    def AnalyzeCurve(p: int) -> ndarray:
        universe = HermitianCurve.CreateUniverse(p)
        print("Constructing Hermitian curve. Fq -> \n{}".format(str(universe.X)))

        curve = []
        for i, j in universe.P:
            x, y = universe.get(i, j)
            xt = universe.X.traceElement(x)
            yn = universe.Y.normElement(y)
            if xt == yn:
                print("Found Hermitian curve point -> ({}, {})".format(str(x), str(y)))
                curve.append((x, y))

        return curve
