from collections import Counter


def puzzle1(lines, steps: int):
    seq, rules = str(lines[:1][0]), lines[2:]

    rules = [{'pair': r[:2], 'ins': r[-1]} for r in rules]

    for _ in range(steps):
        pairs = []
        for i in range(1, len(seq)):
            pairs.append(seq[i-1:i+1])

        new_seq = pairs[0][0]

        for p in pairs:
            for r in rules:
                if r['pair'] == p:
                    new_seq += r['ins'] + p[1]
                    break

        seq = new_seq

    c = Counter(list(seq))
    return max(c.values()) - min(c.values())


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


    # input data
    # data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    print(f'Puzzle1: {puzzle1(data, 10)}')
    # print(f'Puzzle2: {puzzle1(data, 40)}')


if __name__ == '__main__':
    run()
