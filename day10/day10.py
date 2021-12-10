from typing import List


def recognize_lines(lines: List[str]):
    corrupted = []
    incomplete = []

    for i, line in enumerate(lines):
        test = ""
        corrupted_char = None

        for char in line:
            if char in ['(', '[', '{', '<']:
                test += char
            else:
                last = test[-1:]

                match = any([last == "(" and char == ")",
                             last == '[' and char == ']',
                             last == '{' and char == '}',
                             last == '<' and char == '>'])

                if match:
                    test = test[:-1]
                else:
                    corrupted_char = char
                    # print(f'line {i + 1} corrupt')
                    break

        if corrupted_char:
            corrupted.append({'line': line, 'char': corrupted_char})
        else:
            incomplete.append(line)

    return {'corrupted': corrupted, 'incomplete': incomplete}


def puzzle1(lines):
    corrupted_chars = [line['char'] for line in lines]
    closings = [')', ']', '}', '>']
    points = [3, 57, 1197, 25137]
    print(f'Puzzle1: syntax error score: {sum([points[closings.index(c)] for c in corrupted_chars])}')


def input_data():
    print('\nInput Data:')
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    lines = recognize_lines(data)

    puzzle1(lines['corrupted'])


def test_data():
    print('Test Data:')
    data = """[({(<(())[]>[[{[]{<()<>>
            [(()[<>])]({[<{<<[]>>(
            {([(<{}[<>[]}>{[]{[(<()>
            (((({<>}<{<{<>}{[]{[]{}
            [[<[([]))<([[{}[[()]]]
            [{[{({}]{}}([{[{{{}}([]
            {<[[]]>}<{[{[{[]{()[[[]
            [<(<(<(<{}))><([]([]()
            <{([([[(<>()){}]>(<<{{
            <{([{{}}[<[[[<>{}]]]>[]]"""

    data = [x.strip() for x in data.split('\n')]

    lines = recognize_lines(data)

    puzzle1(lines['corrupted'])


if __name__ == '__main__':
    test_data()
    input_data()

