import turtle
import random


class SierpinskiTriangle:

    def __init__(self, coordinates=((0, 0), (100, 200), (200, 0))):
        self.coordinates = coordinates

    def draw(self, method="iterative", drawing_speed=1, degree_of_deep=3, point_number=10000):
        drawing_tool = turtle.Turtle()
        drawing_tool.speed(drawing_speed)
        window = turtle.Screen()
        if method == "iterative":
            self._draw_iterative(self.coordinates, degree_of_deep, drawing_tool)
        elif method == "chaotic":
            self._draw_chaotic(self.coordinates, point_number, drawing_tool)
        else:
            raise ValueError
        window.exitonclick()

    @staticmethod
    def _draw_iterative(coordinates, degree, drawing_tool):
        SierpinskiTriangle.draw_triangle(coordinates, drawing_tool)
        if degree > 0:
            SierpinskiTriangle._draw_iterative((coordinates[0],
                                                SierpinskiTriangle.calc_middle_point(coordinates[0], coordinates[1]),
                                                SierpinskiTriangle.calc_middle_point(coordinates[0], coordinates[2])),
                                               degree - 1, drawing_tool)
            SierpinskiTriangle._draw_iterative((coordinates[1],
                                                SierpinskiTriangle.calc_middle_point(coordinates[0], coordinates[1]),
                                                SierpinskiTriangle.calc_middle_point(coordinates[1], coordinates[2])),
                                               degree - 1, drawing_tool)
            SierpinskiTriangle._draw_iterative((coordinates[2],
                                                SierpinskiTriangle.calc_middle_point(coordinates[2], coordinates[1]),
                                                SierpinskiTriangle.calc_middle_point(coordinates[0], coordinates[2])),
                                               degree - 1, drawing_tool)

    @staticmethod
    def _draw_chaotic(coordinates, degree, drawing_tool):
        drawing_tool.penup()
        drawing_tool.goto(coordinates[0][0], coordinates[0][1])
        drawing_tool.dot(2, 'black')
        drawing_tool.goto(coordinates[1][0], coordinates[1][1])
        drawing_tool.dot(2, 'black')
        drawing_tool.goto(coordinates[2][0], coordinates[2][1])
        drawing_tool.dot(2, 'black')
        for i in range(10000):
            px = drawing_tool.position()[0]
            py = drawing_tool.position()[1]
            random_number = random.randint(1, 3)
            if random_number == 1:
                newX = (px + coordinates[0][0])//2
                newY = (py + coordinates[0][1])//2
            elif random_number == 2:
                newX = (px + coordinates[1][0])//2
                newY = (py + coordinates[1][1])//2
            else:
                newX = (px + coordinates[2][0])//2
                newY = (py + coordinates[2][1])//2
            drawing_tool.goto(newX, newY)
            drawing_tool.dot(2, 'black')
        drawing_tool.end_fill()
        drawing_tool.pendown()

    @staticmethod
    def draw_triangle(coordinates, drawing_tool):
        drawing_tool.up()
        drawing_tool.goto(coordinates[0][0], coordinates[0][1])
        drawing_tool.fillcolor('white')
        drawing_tool.down()
        drawing_tool.begin_fill()
        drawing_tool.goto(coordinates[1][0], coordinates[1][1])
        drawing_tool.goto(coordinates[2][0], coordinates[2][1])
        drawing_tool.goto(coordinates[0][0], coordinates[0][1])
        drawing_tool.end_fill()

    @staticmethod
    def calc_middle_point(start_point, finish_point):
        return (start_point[0]+finish_point[0])//2, (start_point[1]+finish_point[1])//2
