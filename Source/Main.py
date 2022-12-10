from AlgebraicMerger import AlgebraicMerger
from sys import argv


def main(p: int, h: int):
    agm = AlgebraicMerger(p, h)
    agm.analyzeIntersection()


if __name__ == "__main__":
    main(int(argv[1]), int(argv[2]))
