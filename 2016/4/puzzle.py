import unittest
import re
from collections import Counter


def checksum(room_name):
    counter = Counter(room_name.replace("-", ""))
    chars = list(set(room_name))

    b = sorted(sorted(chars), key=lambda x: counter[x], reverse=True)
    return "".join(b[:5])


def decrypted_name(room):
    all_chars = "abcdefghijklmnopqrstuvwxyz"
    return "".join(all_chars[(all_chars.index(char) + room[1]) % len(all_chars)] if char in all_chars else " " for char in room[0])


def parse_room(room_line):
    r = re.compile('([\w-]+)-(\d+)\[([a-z]+)\]')
    groups = r.match(room_line).groups()
    return (groups[0], int(groups[1]), groups[2])


def star(rooms):
    for room_line in rooms:
        room = parse_room(room_line)
        if checksum(room[0]) == room[2]:
            yield room[1]
        else:
            yield 0


def star2(room):
    for room_line in rooms:
        room = parse_room(room_line)
        name = decrypted_name(room)
        if name == "northpole object storage":
            return room[1]


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual("abxyz", checksum("aaaaa-bbb-z-y-x"))
        self.assertEqual("abcde", checksum("a-b-c-d-e-f-g-h"))
        self.assertEqual("oarel", checksum("not-a-real-room"))

    def test_star_2(self):
        self.assertEqual("very encrypted name", decrypted_name(("qzmt-zixmtkozy-ivhz", 343)))


if __name__ == '__main__':
    rooms = open('input.txt').read().strip().split("\n")

    print("star 1: {}".format(sum(star(rooms))))
    print("star 2: {}".format(star2(rooms)))

    unittest.main()
