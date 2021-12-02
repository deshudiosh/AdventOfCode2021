# part 1
dirs, vals = zip(*(x.split() for x in open('./input.txt', 'r').readlines()))

forward = depth = 0
for d, v in zip(dirs, [int(v) for v in vals]):
    if d == 'forward': forward += v
    else: depth += v if d == "down" else -v

print(forward*depth)


# part 2
aims, vals = zip(*(x.split() for x in open('./input.txt', 'r').readlines()))

forward = depth = aim = 0
for a, v in zip(aims, [int(v) for v in vals]):
    if a == 'forward':
        forward += v
        depth += v * aim
    else: aim += v if a == "down" else -v

print(forward*depth)


