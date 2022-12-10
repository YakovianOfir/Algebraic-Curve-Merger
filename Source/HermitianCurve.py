from FiniteUniverse import FiniteUniverse
from GammaWeights import GammaWeights
from GeometricLine import GeometricLine
from FiniteField import FiniteField


class HermitianCurve:

    def __init__(self, p: int, h: int):
        self._domain = FiniteField(p, 2)
        self._gammas = GammaWeights(self._domain)
        self._universe = FiniteUniverse(p, h)
        self._curve = self._analyzeCurve()
        assert len(self._curve) == p ** (h + 2)

    def _analyzeCurve(self):
        curve = []
        universeElements = self._universe.getIterator()
        for e in universeElements:
            if self.isCurveElement(e):
                curve.append(e)
        return curve

    def isCurveElement(self, e) -> bool:
        for i in range(len(e) - 1):
            x = e[i]
            y = e[i + 1]
            xn = self._universe.getAxis(i).normElement(x)
            yt = self._universe.getAxis(i + 1).traceElement(y)
            if xn != yt:
                return False
        return True

    def getLines(self) -> [GeometricLine]:
        lines = []
        for p1 in self._curve:
            for p2 in self._curve:
                if p1 == p2:
                    continue
                line = GeometricLine(p1, p2, self._domain, self._gammas)
                lines.append(line)
        return lines

    def getCurve(self):
        return self._curve
