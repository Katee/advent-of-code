import unittest
from itertools import permutations


def is_triangle(sides):
    sides = [int(side) for side in sides]

    return all(sum(perm[0:2]) > perm[2] for perm in permutations(sides))


def star(triangles):
    return [is_triangle(sides) for sides in triangles].count(True)


def read_triangle_columns(file):
    while True:
        lines = [file.readline().split() for i in range(3)]

        if lines == [[], [], []]:
            break

        for i in range(3):
            yield [int(n) for n in [lines[0][i], lines[1][i], lines[2][i]]]


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(False, is_triangle([5, 10, 25]))
        self.assertEqual(True, is_triangle([3, 4, 5]))
        self.assertEqual(True, is_triangle([2, 2, 2]))

    def test_star_2(self):
        pass


if __name__ == '__main__':
    triangles = [sides.split() for sides in open('input.txt').read().strip().split("\n")]
    triangles2 = read_triangle_columns(open('input.txt'))

    print("star 1: {}".format(star(triangles)))
    print("star 2: {}".format(star(triangles2)))

    unittest.main()
