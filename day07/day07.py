import timeit


def fuel_to_align_constant(crab_pos_list):
    possible_alignments = range(min(crab_pos_list), max(crab_pos_list)+1)
    fuel_usages = []

    for p_a in possible_alignments:
        fuel = 0
        for pos in crab_pos_list:
            fuel += abs(pos - p_a)

        fuel_usages.append(fuel)

    return sorted(fuel_usages)[0]


def fuel_to_align_incremental(crab_pos_list):
    possible_alignments = range(min(crab_pos_list), max(crab_pos_list)+1)
    fuel_usages = []

    for p_a in possible_alignments:
        fuel = 0

        for pos in crab_pos_list:
            num_steps = abs(pos - p_a)
            # fuel += sum(range(1, num_steps + 1))  # slow 27sec, formula is faster - below 1sec

            """ Sum of arithmetic series = ((n / 2) * (2 * a + (n - 1) * d))
                Where:
                a - First term
                d - Common difference
                n - No of terms """

            # simplified formula
            fuel += int((num_steps / 2) * (2 + (num_steps - 1)))

        fuel_usages.append(fuel)

    return sorted(fuel_usages)[0]


if __name__ == '__main__':
    data = [int(x) for x in open('./input.txt', 'r').read().split(',')]
    # data = list(map(int, "16,1,2,0,4,2,7,1,2,14".split(',')))
    print(f'Puzzle1: {fuel_to_align_constant(data)}')
    print('exec time:', timeit.Timer(lambda: print(f'Puzzle2: {fuel_to_align_incremental(data)}')).timeit(number=1))
