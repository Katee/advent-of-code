import unittest


def follow_path(steps):
    # x is west/east
    # y is north/south
    # north, east, south, west
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_i = 0

    location = [0, 0]

    for step in steps:
        if step[0] == "L":
            direction_i = (direction_i + 1) % len(directions)
            direction = directions[direction_i]
        elif step[0] == "R":
            direction_i = (direction_i - 1) % len(directions)
            direction = directions[direction_i]

        count = int(step[1:])
        for i in range(count):
            location = tuple(l + d for l, d in zip(location, direction))
            yield location


def taxicab_distance(location):
    return sum([abs(n) for n in location])


def star1(steps):
    path = list(follow_path(steps))
    return taxicab_distance(path[-1])


def star2(steps):
    path = set()

    for location in follow_path(steps):
        if location in path:
            return taxicab_distance(location)
        path.add(location)


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(5, star1(["R2", "L3"]))
        self.assertEqual(2, star1(["R2", "R2", "R2"]))
        self.assertEqual(12, star1(["R5", "L5", "R5", "R3"]))

    def test_star_2(self):
        self.assertEqual(4, star2(["R8", "R4", "R4", "R8"]))


if __name__ == '__main__':
    steps = open('input.txt').read().strip().split(", ")

    print("star 1: {}".format(star1(steps)))
    print("star 2: {}".format(star2(steps)))

    unittest.main()
