

def puzzle1(data):
    rows = [[int(x) for x in list(row)] for row in data]
    u, v = len(rows[0]), len(rows)

    sum_risk = 0
    for r_idx, row in enumerate(rows):
        for c_idx, col in enumerate(row):
            adjacent = []
            if c_idx > 0:  # left
                adjacent.append(row[c_idx-1])
            if c_idx < u-1:  # right
                adjacent.append(row[c_idx+1])
            if r_idx > 0:  # top
                adjacent.append(rows[r_idx-1][c_idx])
            if r_idx < v-1:
                adjacent.append(rows[r_idx+1][c_idx])

            if col < min(adjacent):
                sum_risk += col+1

    print(f'Puzzle1 sum of risk levels: {sum_risk}')


if __name__ == '__main__':
    data_in = [d.strip() for d in open('./input.txt', 'r').readlines()]

    # test data
    # data = "2199943210 3987894921 9856789892 8767896789 9899965678".split(' ')
    puzzle1(data_in)
