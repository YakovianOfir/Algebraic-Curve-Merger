from CartesianProduct import CartesianProduct
from Universe import *


def main():
    u = Universe(2, 5)
    p = CartesianProduct(u.elements, u.elements)
    u.show()
    p.show()


if __name__ == "__main__":
    main()
