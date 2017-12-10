import unittest
from functools import reduce


def knot_hash_round(lengths, n=None, cur_pos=0, skip_size=0):
    if n is None:
        n = list(range(256))

    for length in lengths:
        # Reverse the order of that length of elements in the list, starting with the element at the current position.
        idxs = [i % len(n) for i in range(cur_pos, cur_pos + length)]
        copy_n = n[:]

        for i, j in zip(idxs, reversed(idxs)):
            n[i] = copy_n[j]

        # Move the current position forward by that length plus the skip size.
        cur_pos += (length + skip_size) % len(n)
        # Increase the skip size by one.
        skip_size += 1

    return (n, cur_pos, skip_size)


def star1(lengths, n=None):
    knot_hash, _, _ = knot_hash_round(lengths, n)
    return knot_hash[0] * knot_hash[1]


def star2(lengths_raw, n=None, num_rounds=64):
    if n is None:
        n = list(range(256))

    lengths = [ord(c) for c in lengths_raw] + [17, 31, 73, 47, 23]

    cur_pos, skip_size = 0, 0

    for i in range(num_rounds):
        n, cur_pos, skip_size = knot_hash_round(lengths, n, cur_pos, skip_size)

    return dense_hash(n)


def sparse_hash(l):
    return [reduce(lambda x, y: x ^ y, l[i * 16:i * 16 + 16], 0) for i in range(16)]


def dense_hash(l):
    return "".join(["%0.2x" % d for d in sparse_hash(l)])


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(12, star1([3, 4, 1, 5], list(range(5))))

    def test_star_2(self):
        self.assertEqual("a2582a3a0e66e6e86e3812dcb672a272", star2(""))
        self.assertEqual("33efeb34ea91902bb2f59c9920caa6cd", star2("AoC 2017"))
        self.assertEqual("3efbe78a8d82f29979031a4aa0b16a9d", star2("1,2,3"))
        self.assertEqual("63960835bcdc130f0b66d7ff4f6a5a8e", star2("1,2,4"))


if __name__ == '__main__':
    lengths = [int(i) for i in open('input.txt').read().strip().split(',')]
    print("star 1: {}".format(star1(lengths)))

    lengths = open('input.txt').read().strip()
    print("star 2: {}".format(star2(lengths)))

    unittest.main()
