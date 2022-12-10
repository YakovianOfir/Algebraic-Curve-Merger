from FiniteField import FiniteField
from itertools import product


class FiniteUniverse:

    def __init__(self, p: int, h: int):
        self._p = p
        self._h = h
        self._universe = self._createUniverse()

    def __len__(self):
        return self.axisSize() ** self.axisCount()

    def _createUniverse(self) -> [FiniteField]:
        axisSystem = []
        for i in range(0, self.axisCount()):
            axisSystem.append(self._createUniverseAxis())
        return axisSystem

    def _createUniverseAxis(self) -> FiniteField:
        Fq = FiniteField(self._p, 2)
        assert len(Fq) == self.axisSize()
        return Fq

    def axisCount(self) -> int:
        return self._h + 1

    def axisSize(self) -> int:
        return self._p ** 2

    def getAxis(self, i: int) -> FiniteField:
        return self._universe[i]

    def getIterator(self):
        return product(*self._universe)
