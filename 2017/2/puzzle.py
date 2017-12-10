import unittest
import math


def all_factors(n):
    factors = []

    if n != 0 and n != 1:
        factors = [1]

    i = 2
    while(i <= math.sqrt(n)):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)
        i += 1

    return factors


def checksum(line):
    return max(line) - min(line)


def checksum2(line):
    for n in line:
        for factor in all_factors(n):
            if factor in line:
                return (n / factor)


def spreadsheet_checksum(spreadsheet, checksum_func):
    return sum([checksum_func(line) for line in spreadsheet])


class Test(unittest.TestCase):
    def test_star_1(self):
        spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
        self.assertEqual(18, spreadsheet_checksum(spreadsheet, checksum))

    def test_star_2(self):
        spreadsheet = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 3]]
        self.assertEqual(9, spreadsheet_checksum(spreadsheet, checksum2))


if __name__ == '__main__':
    spreadsheet = [[int(n) for n in l.split("\t")] for l in open('input.txt').read().strip().split("\n")]

    print("star 1: {}".format(spreadsheet_checksum(spreadsheet, checksum)))
    print("star 2: {}".format(spreadsheet_checksum(spreadsheet, checksum2)))

    unittest.main()
