if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        times_increased = 0
        prev_val = None
        for val in (int(x) for x in f.readlines()):
            times_increased += 1 if prev_val and val > prev_val else 0
            prev_val = val
        print(times_increased)
