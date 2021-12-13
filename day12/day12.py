from collections import deque
from itertools import chain, permutations
from pprint import pprint
from typing import List


class Cave:
    def __init__(self, name: str):
        self.name = name
        self.is_start = name == 'start'
        self.is_end = name == 'end'
        self.is_big = name.isupper()
        self.friends = []  # type: List[Cave]

    def __repr__(self):
        return self.name

    def add_link(self, link):
        if link not in self.friends:
            self.friends.append(link)


def get_cave_by_name(caves, name):
    for cave in caves:
        if cave.name == name:
            return cave


def find_paths(lines):
    pairs = [line.split('-') for line in lines]
    unique_names = list(dict.fromkeys(chain(*pairs)))  # ordered list of unique values, py3.7
    caves = [Cave(name) for name in unique_names]

    # assign connections
    for pair in pairs:
        for cave in caves:
            if pair[0] == cave.name:
                cave.add_link(get_cave_by_name(caves, pair[1]))
            if pair[1] == cave.name:
                cave.add_link(get_cave_by_name(caves, pair[0]))


    # temporary!
    caves_mults = []
    for c in caves:
        mult = len(c.friends)-1 if c.is_big else 1
        for i in range(mult):
            caves_mults.append(c)

    paths = deque()

    for i in range(1, len(caves_mults)):
        permmuts = permutations(caves_mults, i)
        permmuts = [p for p in permmuts if p[0].is_start and p[-1].is_end]
        new = deque()
        for path in permmuts:
            are_lined = True
            for j in range(1, len(path)):
                if path[j - 1] not in path[j].friends:
                    are_lined = False

            if are_lined and path not in new:
                new.append(path)

        paths.extend(new)

    # pprint(paths)
    print(len(paths))


def test_data():
    print('Test Data:')
    data = """  start-A
                start-b
                A-c
                A-b
                b-d
                A-end
                b-end  """

    data = """  dc-end
                HN-start
                start-kj
                dc-start
                dc-HN
                LN-dc
                HN-end
                kj-sa
                kj-HN
                kj-dc """

    # this crashes, memory error
    data = """ fs-end
                he-DX
                fs-he
                start-DX
                pj-DX
                end-zg
                zg-sl
                zg-pj
                pj-he
                RW-he
                fs-DX
                pj-RW
                zg-RW
                start-pj
                he-WI
                zg-he
                pj-fs
                start-RW """

    data = [x.strip() for x in data.split('\n')]

    find_paths(data)


if __name__ == '__main__':
    test_data()