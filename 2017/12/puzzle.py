import unittest
from collections import defaultdict


def parse_program_connections(filename):
    with open(filename) as f:
        for line in f.readlines():
            parsed_line = line.strip().split(" ")
            pid = parsed_line[0]
            pipes = [p.replace(",", "") for p in parsed_line[2:]]
            yield (pid, pipes)


def program_connections(parsed_program_connections):
    connections = defaultdict(list)

    for pid, pipes in parsed_program_connections:
        [connections[pid].append(pipe) for pipe in pipes]

    return connections


def find_connected(connections, starting_pid):
    to_visit = set([starting_pid])
    visited = set()

    while len(to_visit) > 0:
        visiting = to_visit.pop()
        visited.add(visiting)
        for p in connections[visiting]:
            if p not in visited:
                to_visit.add(p)

    return visited


def star1(filename='input.txt'):
    connections = program_connections(parse_program_connections(filename))
    return len(find_connected(connections, '0'))


def star2(filename='input.txt'):
    connections = program_connections(parse_program_connections(filename))

    groups = 0
    to_visit = set(connections.keys())

    while len(to_visit) > 0:
        connected = find_connected(connections, to_visit.pop())
        to_visit = to_visit.difference(connected)
        groups += 1

    return groups


class Test(unittest.TestCase):
    def test_star_1(self):
        self.assertEqual(6, star1('example.txt'))

    def test_star_2(self):
        self.assertEqual(2, star2('example.txt'))


if __name__ == '__main__':
    print("star 1: {}".format(star1()))
    print("star 2: {}".format(star2()))

    unittest.main()
