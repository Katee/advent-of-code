import unittest


def captcha(digits, offset=1):
    sum = 0

    for i in range(len(digits)):
        compliment_digit = digits[(i + offset) % len(digits)]
        if digits[i] == compliment_digit:
            sum += int(digits[i])

    return sum


def halfway_round_captcha(digits):
    return captcha(digits, offset=len(digits) // 2)


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(3, captcha("1122"))
        self.assertEqual(4, captcha("1111"))
        self.assertEqual(0, captcha("1234"))
        self.assertEqual(9, captcha("91212129"))

    def test_star_2(self):
        self.assertEqual(6, halfway_round_captcha("1212"))
        self.assertEqual(0, halfway_round_captcha("1221"))
        self.assertEqual(4, halfway_round_captcha("123425"))
        self.assertEqual(12, halfway_round_captcha("123123"))
        self.assertEqual(4, halfway_round_captcha("12131415"))


if __name__ == '__main__':
    digits = open('input.txt', 'r').read().strip()
    print("star 1: {}".format(captcha(digits)))
    print("star 2: {}".format(halfway_round_captcha(digits)))

    unittest.main()
