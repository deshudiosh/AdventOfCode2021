from dataclasses import dataclass


@dataclass
class Octopus:
    x: int
    y: int
    value: int
    friends = []
    has_flashed = False


class Grid:
    def __init__(self, lines):
        self.octopi = []
        self.num_rows = len(lines)
        self.num_cols = len(lines[0])

        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                self.octopi.append(Octopus(int(x), int(y), int(value)))

        self.assign_friends()

    def get_octopus(self, x: int, y: int):
        return self.octopi[y * self.num_cols + x]

    def assign_friends(self):
        for octo in self.octopi:

            friends = []
            for v in range(self.num_rows):
                for u in range(self.num_cols):
                    if u in range(octo.x - 1, octo.x + 2) and v in range(octo.y - 1, octo.y + 2):
                        friend = self.get_octopus(u, v)
                        if friend is not octo:
                            friends.append(friend)

            octo.friends = friends
            # print(f'^^^^ {octo} has {len(octo.friends)} friends')

    def print(self):
        """ testing purpose """
        values = ""
        print(' *' * 10)
        last_y = 0
        for o in self.octopi:
            if o.y > last_y:
                print(values)
                values = str(o.value)
                last_y = o.y
            else:
                values += str(o.value)
        print(values)
        print(' *' * 10)


def solve(lines):
    grid = Grid(lines)

    total_flashes_in_100_steps = 0
    step_where_all_flashed = None

    step = 0
    while not step_where_all_flashed:
        step += 1

        # reset flash status first
        for octo in grid.octopi:
            octo.has_flashed = False
            octo.value += 1

        still_flashing = True
        while still_flashing:
            still_flashing = False
            for octo in [o for o in grid.octopi if not o.has_flashed]:
                if octo.value > 9:
                    octo.has_flashed = True
                    still_flashing = True
                    for friend in octo.friends:
                        friend.value += 1

                    if step < 100:
                        total_flashes_in_100_steps += 1

        num_octo_flashed_this_step = 0

        for octo in grid.octopi:
            if octo.value > 9:
                octo.value = 0
                num_octo_flashed_this_step += 1

        if num_octo_flashed_this_step == len(grid.octopi):
            step_where_all_flashed = step

    print(f'Puzzle1: number or flashes = {total_flashes_in_100_steps}')
    print(f'Puzzle2: all octopuses sync-flashed first time in step = {step_where_all_flashed}')


def input_data():
    print('\nInput Data:')
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    solve(data)


def test_data():
    print('Test Data:')
    data = """  5483143223
                2745854711
                5264556173
                6141336146
                6357385478
                4167524645
                2176841721
                6882881134
                4846848554
                5283751526  """

    data = [x.strip() for x in data.split('\n')]

    solve(data)


if __name__ == '__main__':
    test_data()
    input_data()

