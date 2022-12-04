from galois import FieldArray, GF


class Universe:

    def __init__(self, p, d):
        self._domain = GF(p ** d, display="poly")
        assert self._domain.characteristic == p
        assert self._domain.degree == d

    def __str__(self):
        return self._domain.properties

    def norm(self) -> FieldArray:
        return self._domain.elements.field_norm()

    def trace(self) -> FieldArray:
        return self._domain.elements.field_trace()

    def normElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_norm()

    def traceElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_trace()

    def _getElements(self):
        return self._domain.elements

    elements = property(_getElements)

    def show(self):
        print()
        print("=" * 60)
        print("Universe -> \n{}\n".format(self))
        for i, e in enumerate(self._domain.elements):
            n, t = self.normElement(e), self.traceElement(e)
            print("Universe Element (#{:06}) -> (N: {}) (T: {}) [{}]".format(i, str(n), str(t), str(e)))
        print("=" * 60)
        print()

