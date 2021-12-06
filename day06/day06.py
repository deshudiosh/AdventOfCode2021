from collections import Counter
from typing import List


def solve(d, days, msg: str):
    fishes = Counter(d)

    for day in range(days):
        after_day_fishes = Counter()

        for fish in fishes.keys():
            count = fishes[fish]
            fish -= 1
            if fish < 0:
                after_day_fishes[6] += count
                after_day_fishes[8] = count
            else:
                after_day_fishes[fish] += count

        fishes = after_day_fishes

    print(f'{msg} {sum(fishes.values())}')


if __name__ == '__main__':
    data = [int(x) for x in open('./input.txt', 'r').read().split(',')]
    solve(data, 80, 'puzzle1:')
    solve(data, 256, 'puzzle2:')



