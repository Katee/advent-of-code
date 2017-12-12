import unittest
import math


def all_factors(n):
    if n != 0 and n != 1:
        yield 1

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            yield n // i


def parsed_spreadsheet(filename):
    with open(filename) as f:
        for l in f.readlines():
            yield [int(n) for n in l.strip().split("\t")]


def checksum(line):
    return max(line) - min(line)


def checksum2(line):
    for n in line:
        for factor in all_factors(n):
            if factor in line:
                return n // factor


def spreadsheet_checksum(spreadsheet, checksum_func):
    return sum([checksum_func(line) for line in spreadsheet])


class Test(unittest.TestCase):
    def test_star_1(self):
        spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(18, spreadsheet_checksum(spreadsheet, checksum))

    def test_star_2(self):
        spreadsheet = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 3]]
        self.assertEqual(9, spreadsheet_checksum(spreadsheet, checksum2))

    def test_all_factors(self):
        self.assertEqual(set([1, 2, 3]), set(all_factors(6)))
        self.assertEqual(3, len(list(all_factors(6))))


if __name__ == '__main__':
    print("star 1: {}".format(spreadsheet_checksum(parsed_spreadsheet('input.txt'), checksum)))
    print("star 2: {}".format(spreadsheet_checksum(parsed_spreadsheet('input.txt'), checksum2)))

    unittest.main()
