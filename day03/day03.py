from collections import Counter

data = [d.strip() for d in open('./input.txt', 'r').readlines()]

# part1
gamma_binary = "".join(Counter(li).most_common(1)[0][0] for li in zip(*[list(x) for x in data]))
epsilon_binary = "".join(["1" if i == "0" else "0" for i in list(gamma_binary)])
gamma, epsilon = map(lambda x: int(x, 2), [gamma_binary, epsilon_binary])

print(gamma*epsilon)


