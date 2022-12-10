from galois import FieldArray, GF


class FiniteField:

    def __init__(self, p: int, d: int):
        self._domain = GF(p ** d, display="poly")
        assert self._domain.characteristic == p
        assert self._domain.degree == d
        self._index = -1

    def __str__(self):
        return self._domain.properties

    def __len__(self):
        return len(self._domain.elements)

    def normElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_norm()

    def traceElement(self, e: FieldArray) -> FieldArray:
        return self._domain.elements[e].field_trace()

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._domain.elements):
            raise StopIteration
        return self._domain.elements[self._index]

