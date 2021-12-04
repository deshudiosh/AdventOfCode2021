import functools
import math
import operator
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Field:
    value: int
    marked: bool = False

    # logging purpose only
    def __repr__(self):
        return str(self.value)


class Board:
    def __init__(self, rows_data):
        self.fields = [Field(int(d)) for d in " ".join(rows_data).split(" ") if d]

    def mark_field(self, num: int):
        for field in self.fields:
            if field.value == num:
                field.marked = True

    def is_won(self) -> bool:
        is_won = False

        split = int(math.sqrt(len(self.fields)))
        _rows = [self.fields[i:i + split] for i in range(0, len(self.fields), split)]
        _cols = [list(z) for z in zip(*rows)]  # invert rows to columns

        for line in _rows + _cols:
            if all([field.marked for field in line]):
                is_won = True

        return is_won

    def sum_of_unmarked(self) -> int:
        return sum([field.value for field in self.fields if not field.marked])


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


# find the winner
scores = []
for n in numbers:
    for b in boards:
        b.mark_field(n)
        if b.is_won():
            boards.remove(b)
            scores.append(n * b.sum_of_unmarked())


print(f"First part: {scores[0]}")
print(f"Second part: {scores[-1]}")




