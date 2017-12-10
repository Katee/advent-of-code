import unittest


def valid_passphrase(passphrase):
    words = passphrase.split(" ")
    return len(words) == len(set(words))


def valid_passphrase2(passphrase):
    words = ["".join(sorted(word)) for word in passphrase.split(" ")]
    return len(words) == len(set(words))


def count_valid_passphrases(passphrases, valid_func):
    return [valid_func(passphrase) for passphrase in passphrases].count(True)


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(True, valid_passphrase("aa bb cc dd ee"))
        self.assertEqual(False, valid_passphrase("aa bb cc dd aa"))
        self.assertEqual(True, valid_passphrase("aa bb cc dd aaa"))

    def test_star_2(self):
        self.assertEqual(True, valid_passphrase2("abcde fghij"))
        self.assertEqual(False, valid_passphrase2("abcde xyz ecdab"))
        self.assertEqual(True, valid_passphrase2("a ab abc abd abf abj"))
        self.assertEqual(True, valid_passphrase2("iiii oiii ooii oooi oooo"))
        self.assertEqual(False, valid_passphrase2("oiii ioii iioi iiio"))


if __name__ == '__main__':
    passphrases = open("input.txt").read().strip().split("\n")

    print("star 1: {}".format(count_valid_passphrases(passphrases, valid_passphrase)))
    print("star 2: {}".format(count_valid_passphrases(passphrases, valid_passphrase2)))

    unittest.main()
