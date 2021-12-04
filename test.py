v = [88, 11, 57, 73, 89, 43, 34, 91, 15, 58, 9, 39, 18, 12, 14, 1, 98, 29, 77, 52, 84, 97, 96, 68, 10]

rows = [v[i:i + 5] for i in range(0, len(v), 5)]
cols = [list(z) for z in zip(*rows)]  # invert rows to columns

print(rows)
print(cols)