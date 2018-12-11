import turtle


class SierpinskiTriangle:

    def __init__(self, coordinates=((0, 0), (100, 200), (200, 0)), degree_of_deep=3):
        self.coordinates = coordinates
        self.degree_of_deep = degree_of_deep

    def draw(self, method="iterative", drawing_speed=1):
        drawing_tool = turtle.Turtle()
        drawing_tool.speed(drawing_speed)
        window = turtle.Screen()
        if method == "iterative":
            self._draw_iterative(self.coordinates, self.degree_of_deep, drawing_tool)
            pass
        elif method == "chaotic":
            pass
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
        return (start_point[0]+finish_point[0])/2, (start_point[1]+finish_point[1])/2