from collections import Counter, defaultdict


def solve(lines, steps: int):
    templ, rules_lines = str(lines[:1][0]), lines[2:]

    rules = dict()
    for r in rules_lines:
        rules[r[:2]] = r[-1]

    pair_count = Counter()
    for i in range(1, len(templ)):
        pair_count[templ[i-1:i+1]] += 1

    letters = Counter(list(templ))

    for _ in range(steps):
        new_pairs = []
        for pair, count in pair_count.items():
            ins = rules[pair]
            left = pair[0] + ins
            right = ins + pair[1]
            new_pairs.append((left, count))
            new_pairs.append((right, count))
            letters[ins] += count

        pair_count = defaultdict(lambda: 0)
        for pair, count in new_pairs:
            pair_count[pair] += count

    return max(letters.values()) - min(letters.values())


def run():
    test_data = """  NNCB
                
                CH -> B
                HH -> N
                CB -> H
                NH -> C
                HB -> C
                HC -> B
                HN -> C
                NN -> C
                BH -> H
                NC -> B
                NB -> B
                BN -> B
                BB -> N
                BC -> B
                CC -> N
                CN -> C  """

    data = [x.strip() for x in test_data.split('\n')]

    # comment below to work on test data
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    print(f'Puzzle1: {solve(data, 10)}')
    print(f'Puzzle2: {solve(data, 40)}')


if __name__ == '__main__':
    run()
