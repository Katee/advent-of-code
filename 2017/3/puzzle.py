import unittest
from collections import defaultdict
import itertools
import math


def star1(n):
    # o is the dimension of the completed square
    o = int(math.floor(math.sqrt(n)))
    if o % 2 == 0:
        o -= 1

    # a is the length of in the last (likely incomplete) spiral
    a = n - o ** 2

    while True:
        if a < o + 1:
            break
        a -= o + 1

    p = abs(((o + 1) / 2) - a)
    return ((o + 1) / 2) + p


def star2(n):
    map = defaultdict(int)

    for position in spiral_positions():
        s = sum([map[p] for p in neighbour_positions(position)])
        if s == 0:
            s = 1
        map[position] = s

        if s > n:
            break

    return s


def spiral_positions():
    directions = itertools.cycle(["left", "down", "right", "up"])

    initial_positions = [(0, 0), (1, 0), (1, 1)]
    for pos in initial_positions:
        last_pos = pos
        yield last_pos
    offset = [0, 0]

    o = 2

    while True:
        for direction in directions:
            offset = [0, 0]

            if direction == "right":
                offset[0] = 1
            elif direction == "left":
                offset[0] = -1
            elif direction == "up":
                offset[1] = 1
            elif direction == "down":
                offset[1] = -1

            run = o
            if direction == "right":
                run += 1
            if direction == "up":
                run -= 1

            for j in range(run):
                new_pos = (last_pos[0] + offset[0], last_pos[1] + offset[1])
                yield new_pos
                last_pos = new_pos

            if direction == "right":
                o += 2


def neighbour_positions(position):
    neighbours = []
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

    for offset in offsets:
        neighbours.append((position[0] + offset[0], position[1] + offset[1]))

    return neighbours


class Test(unittest.TestCase):
    def test_star_1(self):
        # self.assertEqual(0, star1(1))
        self.assertEqual(3, star1(12))
        self.assertEqual(2, star1(23))
        self.assertEqual(31, star1(1024))

    def test_star_2(self):
        pass


if __name__ == '__main__':
    n = 325489
    print("input: {}".format(n))

    print("star 1: {}".format(star1(n)))
    print("star 2: {}".format(star2(n)))

    unittest.main()
