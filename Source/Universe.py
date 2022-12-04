import galois


class Universe:

    def __init__(self, p, d):
        self.domain = galois.GF(p ** d, display="poly")
        assert self.domain.characteristic == p
        assert self.domain.degree == d

    def __str__(self):
        return self.domain.properties

    def show(self):
        print()
        print("=" * 60)
        print("Universe -> \n{}\n".format(self))
        for i, e in enumerate(self.domain.elements):
            print("Universe Element (#{:06}) -> {}".format(i, str(e)))
        print("=" * 60)
        print()
