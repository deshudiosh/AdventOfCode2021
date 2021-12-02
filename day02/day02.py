dirs, vals = zip(*(x.split() for x in open('./input.txt', 'r').readlines()))

forward = depth = 0
for d, v in zip(dirs, [int(v) for v in vals]):
    if d == 'forward': forward += v
    else: depth += v if d == "down" else -v

print(forward, depth, forward*depth)
