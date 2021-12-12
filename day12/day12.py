from itertools import chain, permutations
from pprint import pprint
from typing import List


class Cave:
    def __init__(self, name):
        self.name = name
        self.is_start = name == 'start'
        self.is_end = name == 'end'
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


    # for i in range(1, len(caves)):
    #     permmuts = permutations(caves, i)
    #     permmuts = [p for p in permmuts if p[0].is_start and p[-1].is_end]
    #     # pprint(list(permmuts))
    #     # print()
    #
    #     paths += list(chain(permmuts))

    # new = []
    # for path in paths:
    #     # print(path)
    #     are_lined = True
    #     for i in range(1, len(path)):
    #         if path[i-1] not in path[i].friends:
    #             are_lined = False
    #
    #     if are_lined:
    #         new.append(path)
    #         print(path)

    # pprint(new)


def test_data():
    print('Test Data:')
    data = """  start-A
                start-b
                A-c
                A-b
                b-d
                A-end
                b-end  """

    data = [x.strip() for x in data.split('\n')]

    find_paths(data)


if __name__ == '__main__':
    test_data()