import re
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Line:
    def __init__(self, coords: str):
        coords = [int(v) for v in re.split('[^0-9]', coords) if v]
        self.x1, self.y1, self.x2, self.y2 = coords
        self.is_horizontal = self.y1 == self.y2
        self.is_vertical = self.x1 == self.x2
        self.is_diagonal = not(self.is_horizontal or self.is_vertical)

    def get_points(self):
        xmin, xmax = min(self.x1, self.x2), max(self.x1, self.x2)
        ymin, ymax = min(self.y1, self.y2), max(self.y1, self.y2)

        if self.is_diagonal:
            pts = []
            steps = xmax-xmin+1
            left_to_right = self.x1 < self.x2
            increases = self.y1 < self.y2 if left_to_right else self.y1 > self.y2
            start_y = ymin if increases else ymax

            for i in range(steps):
                y_delta = i if increases else -i
                pts.append(Point(xmin+i, start_y+y_delta))
            return pts

        else:
            if self.is_horizontal:
                return [Point(x, self.y1) for x in range(xmin, xmax + 1)]

            if self.is_vertical:
                return [Point(self.x1, y) for y in range(ymin, ymax + 1)]


class Board:
    """columns[0]    rows[0][0]"""
    """top left is [0][0]"""
    def __init__(self):
        self.points = []

    def add(self, point: Point):
        while len(self.points) <= point.x:
            self.points.append([])

        while len(self.points[point.x]) <= point.y:
            self.points[point.x].append(0)

        self.points[point.x][point.y] += 1

    def pprint(self):
        # make square first
        size = len(self.points)

        for col in self.points:
            size = max(size, len(col))

        while len(self.points) < size:
            self.points.append([])

        for col in self.points:
            while len(col) < size:
                col.append(0)

        board_rows = [list(z) for z in zip(*self.points)]  # rezip columns to rows
        for row in board_rows:
            print(row)


def solve(board_data):
    board_without_diagonals = Board()
    board_with_diagonals = Board()

    for d in board_data:
        line = Line(d)
        for p in line.get_points():
            board_with_diagonals.add(p)
            if not line.is_diagonal:
                board_without_diagonals.add(p)

    at_least_two_excluding_diagonal = at_least_two = 0

    for cols in board_without_diagonals.points:
        for v in cols:
            if v >= 2:
                at_least_two_excluding_diagonal += 1

    for cols in board_with_diagonals.points:
        for v in cols:
            if v >= 2:
                at_least_two += 1

    print(f"Part1: {at_least_two_excluding_diagonal}\nPart2: {at_least_two}")


def test(board_data):
    b = Board()
    l = Line('0,0 -> 2,2')
    k = Line('0,2 -> 2,0')
    j = Line('0,5 -> 6,5')

    for p in l.get_points() + k.get_points() + j.get_points():
        b.add(p)
    b.pprint()


if __name__ == '__main__':
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    solve(data)
    # test(data)



