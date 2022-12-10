import sys

from AlgebraicMerger import AlgebraicMerger


def main(p: int):
    agm = AlgebraicMerger(p)

    if agm.assesIntersection():
        print("Theorem holds for prime -> [(p) = ({})]".format(p))
    else:
        print("Theorem does not hold for prime -> [(p) = ({})]".format(p))


if __name__ == "__main__":
    main(int(sys.argv[1]))
