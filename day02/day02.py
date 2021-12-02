dirs, vals = zip(*(x.split() for x in open('./input.txt', 'r').readlines()))

forward = depth = 0
for i, d in enumerate(dirs):
    if d == 'forward': forward += int(vals[i])
    else: depth += int(vals[i]) if d == "down" else -int(vals[i])

print(forward, depth, forward*depth)
