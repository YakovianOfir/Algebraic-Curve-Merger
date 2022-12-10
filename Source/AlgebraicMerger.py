from HermitianCurve import HermitianCurve


class AlgebraicMerger:

    def __init__(self, p: int, h: int):
        self._p = p
        self._h = h
        self._curve = HermitianCurve(p, h)

    def analyzeIntersection(self):
        for line in self._curve.getLines():
            count = 0
            for p in self._curve.getCurve():
                if line.contains(p):
                    count = count + 1
            print("Found Hermitian intersection -> (L: {}) (I: {})".format(line, count))
