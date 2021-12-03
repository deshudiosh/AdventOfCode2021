from collections import Counter

data = [d.strip() for d in open('./input.txt', 'r').readlines()]

# part1
gamma_binary = "".join(Counter(li).most_common(1)[0][0] for li in zip(*[list(x) for x in data]))
epsilon_binary = "".join(["1" if i == "0" else "0" for i in list(gamma_binary)])
gamma, epsilon = map(lambda x: int(x, 2), [gamma_binary, epsilon_binary])

print(gamma*epsilon, "\n")


# part2
num_bits = len(data[0])

# oxygen
oxygen = data.copy()
for i in range(num_bits):
    bits = list(zip(*[list(x) for x in oxygen]))[i]
    counter = Counter(bits).most_common()
    keep_bit = counter[0][0] if counter[0][1] > counter[1][1] else 1  # sure?
    # print(counter, keep_bit)

    cpy = oxygen.copy()
    for o in cpy:
        if o[i] != keep_bit:
            cpy.remove(o)

    oxygen = cpy
    print(len(oxygen))

# print(oxygen)

