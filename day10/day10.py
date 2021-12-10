from pprint import pprint
from typing import List

CORRUPTED = 'corrupted'
INCOMPLETE = 'incomplete'


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


def puzzle1(lines: List[str]):
    corrupted_chars = []

    for i, line in enumerate(lines):
        test = ""

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
                    corrupted_chars.append(char)
                    # print(f'line {i + 1} corrupt')
                    break

    closings = [')', ']', '}', '>']
    points = [3, 57, 1197, 25137]
    print(f'Puzzle1: syntax error score: {sum([points[closings.index(c)] for c in corrupted_chars])}')



def input_data():
    print('\nInput Data:')
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]
    puzzle1(data)


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
    # puzzle1(data)

    pprint(recognize_lines(data))




if __name__ == '__main__':
    test_data()
    # input_data()

