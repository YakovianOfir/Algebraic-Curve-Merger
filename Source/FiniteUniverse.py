from CartesianProduct import CartesianProduct
from FiniteField import FiniteField


class FiniteUniverse:

    def __init__(self, p: int, h: int):
        self._p = p
        self._h = p
        self._universe = FiniteUniverse._CreateUniverse(p, h)
        print("Created finite universe.[Size: {}]".format(len(self)))

    @staticmethod
    def _CreateUniverseQuadrant(p: int) -> CartesianProduct:
        Fq = FiniteField(p, 2)
        quadrant = CartesianProduct(Fq, Fq)
        assert len(Fq) == p ** 2
        assert len(quadrant) == p ** 4

    @staticmethod
    def _CreateUniverse(p: int, h: int) -> [CartesianProduct]:
        quadrants = []
        for i in range(0, h - 1):
            print("Creating Universe quadrant. [Fq x Fq] -> [{}, {}]".format(i, i + 1))
            quadrants.append(FiniteUniverse._CreateUniverseQuadrant(p))
        assert len(quadrants) == (h - 1)
        return quadrants

    def axisCount(self):
        return self._h + 1

    def axisSize(self):
        return self._p ** 2

    def __len__(self):
        return self.axisCount() * self.axisCount()
