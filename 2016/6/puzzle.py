import unittest
from collections import Counter


def parse_input(filename='input.txt'):
    with open(filename) as f:
        return f.read().strip().split("\n")


def star1(input_lines):
    line_length = len(input_lines[0])
    counters = [Counter() for i in range(line_length)]

    for line in input_lines:
        for i in range(line_length):
            counters[i].update([line[i]])

    return "".join([counter.most_common(1)[0][0] for counter in counters])


def star2(input_lines):
    line_length = len(input_lines[0])
    counters = [Counter() for i in range(line_length)]

    for line in input_lines:
        for i in range(line_length):
            counters[i].update([line[i]])

    return "".join([sorted(counter.items(), key=lambda x: x[1])[0][0] for counter in counters])


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual("easter", star1(parse_input('example.txt')))

    def test_star_2(self):
        self.assertEqual("advent", star2(parse_input('example.txt')))


if __name__ == '__main__':
    print("star 1: {}".format(star1(parse_input())))
    print("star 2: {}".format(star2(parse_input())))

    unittest.main()
