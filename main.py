from SierpinskiTriangle import *


def main():
    obj1 = SierpinskiTriangle()
    obj1.draw(method='iterative', degree_of_deep=5)
    obj2 = SierpinskiTriangle()
    obj2.draw(method='chaotic', drawing_speed=10000000)


if __name__ == "__main__":
    main()