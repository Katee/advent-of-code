import unittest
from collections import deque
import sys


DIRECTION_OFFSETS = {
    "n": (0, 1),
    "s": (0, -1),
    "nw": (-1, 0.5),
    "ne": (1, 0.5),
    "sw": (-1, -0.5),
    "se": (1, -0.5),
}


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def follow_steps(steps, start_pos=(0, 0)):
    cur_pos = start_pos

    for step in steps:
        yield cur_pos
        offset = DIRECTION_OFFSETS[step]
        cur_pos = (cur_pos[0] + offset[0], cur_pos[1] + offset[1])

    yield cur_pos


# This won't be fast without a closed form solution to find the distance between two positions.
# Switching to a better grid encoding solution would make that easier.
@Memoize
def find_path(start_pos, end_pos=(0, 0)):
    if start_pos == end_pos:
        return 0

    next_pos = start_pos
    for direction, offset in DIRECTION_OFFSETS.items():
        new_pos = tuple([a + b for a, b in zip(start_pos, offset)])
        if measure_distance(new_pos, end_pos) < measure_distance(next_pos, end_pos):
            next_pos = new_pos

    return 1 + find_path(next_pos)


@Memoize
def measure_distance(start_pos, end_pos=(0, 0)):
    return sum([abs(a - b) for a, b in zip(start_pos, end_pos)])


def star1(steps):
    end_pos = deque(follow_steps(steps), maxlen=1).pop()
    return find_path(end_pos)


def star2(steps):
    max_distance = 0

    for position in follow_steps(steps):
        max_distance = max(max_distance, find_path(position))

    return max_distance


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(3, star1(["ne", "ne", "ne"]))
        self.assertEqual(0, star1(["ne", "ne", "sw", "sw"]))
        self.assertEqual(2, star1(["ne", "ne", "s", "s"]))
        self.assertEqual(3, star1(["se", "sw", "se", "sw", "sw"]))

    def test_star_2(self):
        pass


if __name__ == '__main__':
    steps = open('input.txt').read().strip().split(",")
    sys.setrecursionlimit(len(steps))
    print("star 1: {}".format(star1(steps)))
    print("star 2: {}".format(star2(steps)))

    unittest.main()
