from collections import Counter
from typing import List


def solve(d, days):
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


        # for f in range(len(d)):
        #     fish = d[f]
        #     fish -= 1
        #     if fish < 0:
        #         fish = 6
        #         d.append(8)
        #     d[f] = fish

        fishes = after_day_fishes

    print(fishes)
    total_count = sum(fishes.values())
    print(total_count)


if __name__ == '__main__':
    data = [int(x) for x in open('./test.txt', 'r').read().split(',')]
    solve(data, 18)



