import unittest


def spin(programs, number):
    new_programs = list(programs)

    for i in range(len(programs)):
        j = (i + number) % len(programs)
        new_programs[j] = programs[i]

    return new_programs


def exchange(programs, a, b):
    new_programs = list(programs)
    new_programs[a] = programs[b]
    new_programs[b] = programs[a]
    return new_programs


def partner(programs, a, b):
    return exchange(programs, programs.index(a), programs.index(b))


def initialize_programs(n=16):
    return [chr(i) for i in range(97, 97 + n)]


def star1(steps, programs):
    for step in steps:
        if step[0] == "s":
            programs = spin(programs, int(step[1:]))
        elif step[0] == "x":
            a, b = step[1:].split("/")
            programs = exchange(programs, int(a), int(b))
        elif step[0] == "p":
            a, b = step[1:].split("/")
            programs = partner(programs, a, b)

    return "".join(programs)


def star2(steps, programs, iterations=1000000000):
    """
    Execute program steps until a loop is found, then skip over that loop as
    many times as possible.
    """
    seen_states = [programs]

    i = iterations
    while i > 0:
        programs = tuple(star1(steps, programs))
        i -= 1

        if programs in seen_states:
            loop_len = len(seen_states) - seen_states.index(programs)
            i -= (i // loop_len) * loop_len
        else:
            seen_states.append(programs)

    return "".join(programs)


def parse_input(filename='input.txt'):
    with open(filename) as f:
        return f.read().split(",")


class Test(unittest.TestCase):
    def setUp(self):
        self.exampleSteps = ["s1", "x3/4", "pe/b"]

    def testProgramModification(self):
        self.assertEqual("cdeab", "".join(spin(initialize_programs(5), 3)))
        self.assertEqual("ebcda", "".join(exchange(initialize_programs(5), 0, 4)))
        self.assertEqual("ebcda", "".join(partner(initialize_programs(5), 'a', 'e')))

    def testStar1(self):
        self.assertEqual("baedc", star1(self.exampleSteps, initialize_programs(5)))

    def testStar2(self):
        self.assertEqual("baedc", star2(self.exampleSteps, programs=initialize_programs(5), iterations=1))
        self.assertEqual("ceadb", star2(self.exampleSteps, programs=initialize_programs(5), iterations=2))


if __name__ == '__main__':
    steps = parse_input()
    print("star 1: {}".format(star1(steps, initialize_programs(16))))
    print("star 2: {}".format(star2(steps, initialize_programs(16))))

    unittest.main()
