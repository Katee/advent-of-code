import unittest


def run(offsets):
    instruction_count = 0
    instruction_pointer = 0

    while True:
        if instruction_pointer > len(offsets) - 1:
            break

        jmp_value = offsets[instruction_pointer]

        offsets[instruction_pointer] += 1

        instruction_count += 1

        instruction_pointer += jmp_value

    return instruction_count


def run2(offsets):
    instruction_count = 0
    instruction_pointer = 0

    while True:
        if instruction_pointer > len(offsets) - 1:
            break

        jmp_value = offsets[instruction_pointer]

        if offsets[instruction_pointer] >= 3:
            offsets[instruction_pointer] -= 1
        else:
            offsets[instruction_pointer] += 1

        instruction_count += 1

        instruction_pointer += jmp_value

    return instruction_count


class Test(unittest.TestCase):
    def test_star_1(self):
        initial_offsets = [0, 3, 0, 1, -3]
        self.assertEqual(5, run(initial_offsets))

    def test_star_2(self):
        initial_offsets = [0, 3, 0, 1, -3]
        self.assertEqual(10, run2(initial_offsets))


if __name__ == '__main__':
    initial_offsets = [int(i) for i in open("input.txt").read().strip().split("\n")]
    print("star 1: {}".format(run(initial_offsets)))

    initial_offsets = [int(i) for i in open("input.txt").read().strip().split("\n")]
    print("star 1: {}".format(run2(initial_offsets)))

    unittest.main()
