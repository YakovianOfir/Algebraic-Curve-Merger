from galois import FieldArray, GF


class FiniteField:

    def __init__(self, p: int, d: int):
        self._domain = GF(p ** d, display="poly")
        assert self._domain.characteristic == p
        assert self._domain.degree == d

    def __str__(self):
        return self._domain.properties

    def __len__(self):
        return len(self._domain.elements)

    def normElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_norm()

    def traceElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_trace()

    def _getElements(self) -> FieldArray:
        return self._domain.elements

    elements = property(_getElements)

