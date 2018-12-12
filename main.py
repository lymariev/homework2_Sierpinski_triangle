from SierpinskiTriangle import *


def main():
    triangle1 = SierpinskiTriangle()
    triangle1.draw(method='iterative', degree_of_deep=5)
    triangle2 = SierpinskiTriangle()
    triangle2.draw(method='chaotic', drawing_speed=10000000)


if __name__ == "__main__":
    main()