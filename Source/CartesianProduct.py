import numpy as np
from numpy import ndarray


class CartesianProduct:

    def __init__(self, X: ndarray, Y: ndarray):
        self._X = X
        self._Y = Y
        self._P = CartesianProduct.apply(X, Y)

    def __str__(self):
        return self._P.__str__()

    @staticmethod
    def apply(X: ndarray, Y: ndarray) -> ndarray:
        return np.transpose([np.tile(X, len(Y)), np.repeat(Y, len(X))])

    def _X(self) -> ndarray:
        return self._X

    def _Y(self) -> ndarray:
        return self._Y

    def _P(self) -> ndarray:
        return self._P

    def show(self):
        print()
        print("=" * 60)
        print("X -> \n{}".format(self._X))
        print("=" * 60)
        print("Y -> \n{}".format(self._Y))
        print("=" * 60)
        print("P -> \n{}".format(self._P))
        print("=" * 60)
        print()

    X = property(_X)
    Y = property(_Y)
    P = property(_P)
