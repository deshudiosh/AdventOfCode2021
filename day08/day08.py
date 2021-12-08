def puzzle1(d):
    output_values = [[abc for abc in v.split('|')[1].strip().split(' ')] for v in d]

    count = 0
    for out in output_values:
        for abc in out:
            if len(abc) in [2, 3, 4, 7]:  # digits 1, 4, 7, and 8
                count += 1

    print(f'Puzzle1: {count}')


if __name__ == '__main__':
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]
    puzzle1(data)