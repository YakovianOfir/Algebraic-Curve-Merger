import sys

from AlgebraicMerger import AlgebraicMerger
from FiniteUniverse import FiniteUniverse
from HermitianCurve import HermitianCurve


def mainOld(p: int):
    agm = AlgebraicMerger(p)

    if agm.assesIntersection():
        print("Theorem holds for prime -> [(p) = ({})]".format(p))
    else:
        print("Theorem does not hold for prime -> [(p) = ({})]".format(p))


def mainNew(p: int, h: int):
    curve = HermitianCurve(p, h)


if __name__ == "__main__":
    mainNew(int(sys.argv[1]), int(sys.argv[2]))
