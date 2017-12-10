import unittest


def bank_to_redistribute(banks):
    max_i = 0

    for i in range(len(banks)):
        bank = banks[i]
        if bank > banks[max_i]:
            max_i = i

    return max_i


def run(banks):
    num_banks = len(banks)

    path = []
    seen = set()

    while True:
        r = bank_to_redistribute(banks)
        num = banks[r]
        banks[r] = 0

        for i in range(num):
            banks[(r + i + 1) % num_banks] += 1

        bank_string = ','.join([str(n) for n in banks])

        if bank_string in seen:
            break

        seen.add(bank_string)
        path.append(bank_string)

    return (len(seen) + 1, len(seen) - path.index(bank_string))


class Test(unittest.TestCase):
    def test_star_1(self):
        banks = [0, 2, 7, 0]
        self.assertEqual(5, run(banks)[0])

    def test_star_2(self):
        banks = [0, 2, 7, 0]
        self.assertEqual(4, run(banks)[1])


if __name__ == '__main__':
    banks = [int(n) for n in open('input.txt').read().split("\t")]
    output = run(banks)
    print("star 1: {}".format(output[0]))
    print("star 2: {}".format(output[1]))

    unittest.main()
