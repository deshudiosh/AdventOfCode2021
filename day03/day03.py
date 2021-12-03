from collections import Counter

data = [d.strip() for d in open('./input.txt', 'r').readlines()]

# part1
gamma_binary = "".join(Counter(li).most_common(1)[0][0] for li in zip(*[list(x) for x in data]))
epsilon_binary = "".join(["1" if i == "0" else "0" for i in list(gamma_binary)])
gamma, epsilon = map(lambda x: int(x, 2), [gamma_binary, epsilon_binary])

print(gamma*epsilon, "\n")


# part2

# oxygen
oxygen = co2 = data

def most_common(data, i):
    c = Counter([b[i] for b in data])
    return "1" if c['0'] == c['1'] else c.most_common()[0][0]

for i in range(len(data[0])):
    if len(oxygen) > 1:
        oxygen = [x for x in oxygen if x[i] == most_common(oxygen, i)]
    if len(co2) > 1:
        co2 = [x for x in co2 if x[i] != most_common(co2, i)]


print(oxygen, co2)
print("answer:", int(oxygen[0], 2)*int(co2[0], 2))

