from typing import List


openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']


def recognize_lines(lines: List[str]):
    corrupted = []
    incomplete = []

    for line in lines:
        test = ""
        corrupted_char = None

        for char in line:
            if char in openings:
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
                    if not corrupted_char:  # only first corrupted char matters
                        corrupted_char = char

        if corrupted_char:
            corrupted.append({'line': line, 'char': corrupted_char})
        else:
            missing_end = [closings[openings.index(sign)] for sign in reversed(test)]
            incomplete.append({'line': line, 'missing_end': missing_end})

    return {'corrupted': corrupted, 'incomplete': incomplete}


def puzzle1(lines):
    corrupted_chars = [line['char'] for line in lines['corrupted']]
    points = [3, 57, 1197, 25137]
    print(f'Puzzle1: syntax error score: {sum([points[closings.index(c)] for c in corrupted_chars])}')


def puzzle2(lines):
    scores = []
    lines = lines['incomplete']
    for line in lines:
        score = 0
        for sign in line['missing_end']:
            score *= 5
            score += closings.index(sign)+1
        scores.append(score)

    print(f'Puzzle2: middle score: {sorted(scores)[len(lines)//2]}')


def input_data():
    print('\nInput Data:')
    data = [d.strip() for d in open('./input.txt', 'r').readlines()]

    lines = recognize_lines(data)

    puzzle1(lines)
    puzzle2(lines)


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

    puzzle1(lines)
    puzzle2(lines)


if __name__ == '__main__':
    test_data()
    input_data()

