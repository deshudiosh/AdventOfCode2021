import math
from dataclasses import dataclass


@dataclass
class Field:
    """one of the numbers on the bingo board"""
    value: int
    marked: bool = False

    # logging purpose only
    def __repr__(self):
        return str(self.value) if not self.marked else f'({self.value})'


class Board:
    def __init__(self, rows_data):
        self.fields = [Field(int(d)) for d in " ".join(rows_data).split(" ") if d]
        self.did_bingo_already = False

    def bingo(self, num) -> bool:
        # mark the field as marked if it's on a board
        for field in self.fields:
            if field.value == num:
                field.marked = True

        # check if bingo
        split = int(math.sqrt(len(self.fields)))
        board_rows = [self.fields[i:i + split] for i in range(0, len(self.fields), split)]
        board_cols = [list(z) for z in zip(*board_rows)]  # rezip rows to columns

        for line in (board_rows + board_cols):
            if all([field.marked for field in line]):
                self.did_bingo_already = True
                break

        return self.did_bingo_already

    def sum_of_unmarked(self) -> int:
        return sum([field.value for field in self.fields if not field.marked])


if __name__ == '__main__':
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]
    numbers = [int(x) for x in data.pop(0).split(',')]

    # create boards
    boards = []
    rows = []
    for d in [x for x in data if x]:
        rows.append(d)
        if len(rows) == 5:
            boards.append(Board(rows))
            rows = []

    # find the scores
    scores = []
    for n in numbers:
        for b in [b for b in boards if not b.did_bingo_already]:
            if b.bingo(n):
                scores.append(n * b.sum_of_unmarked())

    print(f"First part: {scores[0]}\nSecond part: {scores[-1]}")




