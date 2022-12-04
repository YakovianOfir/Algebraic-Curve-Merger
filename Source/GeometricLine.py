from galois import FieldArray


class GeometricLine:

    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
        assert p1 != p2

    def _first(self):
        return self._p1

    def _second(self):
        return self._p2

    def _x1(self) -> FieldArray:
        return self._p1[0]

    def _y1(self) -> FieldArray:
        return self._p1[1]

    def _x2(self) -> FieldArray:
        return self._p2[0]

    def _y2(self) -> FieldArray:
        return self._p2[1]

    def _n(self) -> FieldArray:
        return self._y2() - self.slope() * self._x2()

    def slope(self) -> FieldArray:
        assert self._x2() != self._x1()
        return (self._y2() - self._y1()) / (self._x2() - self._x1())

    def contains(self, p3: FieldArray) -> bool:
        return self._n() == (p3[1] - self.slope() * p3[0])

    def __str__(self):
        return \
            "[({}, {}) -> ({}, {})] == [y = ({})x + ({})]".format(
                str(self._x1()),
                str(self._y1()),
                str(self._x2()),
                str(self._y2()),
                str(self.slope()),
                str(self._n()))

    p1 = property(_first)
    p2 = property(_second)

