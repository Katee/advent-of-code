import unittest


KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
KEYPAD2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]


def keypad_position_for_line(keypad_line, position, keypad):
    directions = {"U": [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}

    for c in keypad_line:
        try:
            new_position = [p + o for p, o in zip(position, directions[c])]
            # check position
            if key_at_position(new_position, keypad) is not None:
                position = new_position
        except IndexError:
            pass  # don't update to the new position

    return position


def keypad_positions(lines, starting_position, keypad=KEYPAD):
    position = starting_position
    for line in lines:
        position = keypad_position_for_line(line, position, keypad)
        yield key_at_position(position, keypad)


def key_at_position(position, keypad):
    # clamp position
    if position[0] < 0 or position[1] < 0 or \
       position[1] > len(keypad) or position[1] > len(keypad[0]):
        return None
    return keypad[position[1]][position[0]]


def star1(lines):
    return "".join(str(k) for k in keypad_positions(lines, [1, 1]))


def star2(lines):
    return "".join(str(k) for k in keypad_positions(lines, [0, 2], keypad=KEYPAD2))


class Test(unittest.TestCase):
    def test_star_1(self):
        pass
        self.assertEqual("1985", star1("ULL\nRRDDD\nLURDL\nUUUUD".split("\n")))

    def test_star_2(self):
        self.assertEqual("5DB3", star2("ULL\nRRDDD\nLURDL\nUUUUD".split("\n")))


if __name__ == '__main__':
    steps = open('input.txt').read().strip().split("\n")

    print("star 1: {}".format(star1(steps)))
    print("star 2: {}".format(star2(steps)))

    unittest.main()
