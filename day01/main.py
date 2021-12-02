if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        times_increased = 0
        prev_val = None
        for val in (int(x) for x in f.readlines()):
            times_increased += 1 if prev_val and val > prev_val else 0
            prev_val = val

    with open('./input.txt', 'r') as f:
        times_windows_increased = 0
        prev_window_sum = None
        window = []
        for val in (int(x) for x in f.readlines()):
            window.append(val)
            if len(window) > 2:
                window = window[-3:]
                times_windows_increased += 1 if prev_window_sum and sum(window) > prev_window_sum else 0
                prev_window_sum = sum(window)

    print(f'Puzzle 1: {times_increased}\nPuzzle 2: {times_windows_increased}')
