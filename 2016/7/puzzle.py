import unittest
import itertools
import re


def parse_input(filename='input.txt'):
    with open(filename) as f:
        return f.read().strip().split("\n")


def sliding_window_substrings(s, length):
    return (s[i: i + length] for i in range(len(s) - (length - 1)))


def is_abba(s):
    return s[0] != s[1] and s[0] == s[3] and s[1] == s[2]


def contains_abba(s):
    return any(is_abba(s2) for s2 in sliding_window_substrings(s, 4))


def is_aba(s):
    return s[0] != s[1] and s[0] == s[2]


def transform_aba_to_bab(aba):
    return aba[1] + aba[0] + aba[1]


def extract_abas(strings):
    for s in strings:
        for substring in sliding_window_substrings(s, 3):
            if is_aba(substring):
                yield substring


def extract_hyper_and_supernets(ip):
    split_ip = re.split("[\]\[]", ip)
    hypernets = []
    supernets = []

    for i in range(len(split_ip)):
        if i % 2 == 0:
            supernets.append(split_ip[i])
        else:
            hypernets.append(split_ip[i])

    return (hypernets, supernets)


def supports_tls(ip):
    hypernets, supernets = extract_hyper_and_supernets(ip)
    return all(not contains_abba(s) for s in hypernets) and any(contains_abba(s) for s in supernets)


def supports_ssl(ip):
    hypernets, supernets = extract_hyper_and_supernets(ip)
    abas = set(extract_abas(supernets))
    babs = set(extract_abas(hypernets))
    return len(set.intersection(set([transform_aba_to_bab(s) for s in abas]), set(babs))) > 0


def star1(input_lines):
    return [supports_tls(l) for l in input_lines].count(True)


def star2(input_lines):
    return [supports_ssl(l) for l in input_lines].count(True)


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(True, supports_tls("abba[mnop]qrst"))
        self.assertEqual(False, supports_tls("abcd[bddb]xyyx"))
        self.assertEqual(False, supports_tls("aaaa[qwer]tyui"))
        self.assertEqual(True, supports_tls("ioxxoj[asdfgh]zxcvbn"))

    def test_star_2(self):
        self.assertEqual(True, supports_ssl("aba[bab]xyz"))
        self.assertEqual(False, supports_ssl("xyx[xyx]xyx"))
        self.assertEqual(True, supports_ssl("aaa[kek]eke"))
        self.assertEqual(True, supports_ssl("zazbz[bzb]cdb"))


if __name__ == '__main__':
    print("star 1: {}".format(star1(parse_input())))
    print("star 2: {}".format(star2(parse_input())))

    unittest.main()
