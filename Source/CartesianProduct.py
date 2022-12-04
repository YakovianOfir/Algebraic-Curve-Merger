from FiniteField import FiniteField
from numpy import ndarray
import numpy as np


class CartesianProduct:

    def __init__(self, X: FiniteField, Y: FiniteField):
        self._X = X
        self._Y = Y
        self._P = CartesianProduct.Apply(X.elements, Y.elements)

    @staticmethod
    def Apply(X: ndarray, Y: ndarray) -> ndarray:
        return np.transpose([np.tile(X, len(Y)), np.repeat(Y, len(X))])

    def _X(self) -> ndarray:
        return self._X

    def _Y(self) -> ndarray:
        return self._Y

    def _P(self) -> ndarray:
        return self._P

    def __len__(self):
        return len(self._P)

    def get(self, i: int, j: int):
        return self._X.elements[i], self._Y.elements[j]

    X = property(_X)
    Y = property(_Y)
    P = property(_P)
