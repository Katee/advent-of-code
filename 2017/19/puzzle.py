import unittest


def findStart(map):
    return (0, map[0].index("|"))


def followMapLines(map, pos, direction=(1, 0)):
    yield pos

    while True:
        pos = addPositions(pos, direction)

        if not inBounds(map, pos):
            break

        if map[pos[0]][pos[1]] == "+":
            directionOptions = connectedDirections(map, pos)
            direction = nextDirection(map, direction, directionOptions, pos)

        yield pos


def nextDirection(map, direction, options, pos):
    for d in connectedDirections(map, pos):
        if d != flipDirection(direction):
            return d


def flipDirection(direction):
    return (-direction[0], -direction[1])


def inBounds(map, pos):
    return pos[0] > 0 and pos[1] > 0 and \
           pos[0] < len(map) and pos[1] < len(map[0])


def addPositions(pos1, pos2):
    return tuple(sum([a, b]) for a, b in zip(pos1, pos2))


def connectedDirections(map, pos):
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    for direction in directions:
        new_pos = addPositions(pos, direction)
        if inBounds(map, new_pos):
            map_char = map[new_pos[0]][new_pos[1]]
            if map_char != " ":
                yield direction


def findLettersInMapPath(map, path):
    for pos in path:
        cur_char = map[pos[0]][pos[1]]

        if cur_char != " " and cur_char != "|" and \
           cur_char != "-" and cur_char != "+":
            yield cur_char


def star1(map):
    path = followMapLines(map, findStart(map))
    return "".join(findLettersInMapPath(map, path))


def star2(map):
    path = followMapLines(map, findStart(map))
    return sum(1 for _ in path)


def parse_map(filename='input.txt'):
    with open(filename) as f:
        return [list(l) for l in f.read().split("\n")][:-1]


class Test(unittest.TestCase):
    def setUp(self):
        self.exampleMap = parse_map('example.txt')

    def testConnectedDirections(self):
        self.assertEqual([(0, 1), (-1, 0)], list(connectedDirections(self.exampleMap, [5, 5])))
        self.assertEqual([(1, 0), (0, -1)], list(connectedDirections(self.exampleMap, [1, 11])))

    def testStar1(self):
        self.assertEqual("ABCDEF", star1(self.exampleMap))

    def testStar2(self):
        self.assertEqual(38, star2(self.exampleMap))


if __name__ == '__main__':
    print("star 1: {}".format(star1(parse_map())))
    print("star 2: {}".format(star2(parse_map())))

    unittest.main()
