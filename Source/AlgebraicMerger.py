from HermitianCurve import HermitianCurve


class AlgebraicMerger:

    def __init__(self, p: int):
        self._curve = HermitianCurve(p)
        self._p = p

    def assesIntersection(self) -> bool:
        for line in self._curve.getLines():
            count = 0
            if line.slope() == 0:
                continue
            for p in self._curve.getCurve():
                if line.contains(p):
                    count = count + 1
            print("Found Hermitian intersection -> (L: {}) (I: {})".format(line, count))
            if count != (self._p + 1):
                return False
        return True
