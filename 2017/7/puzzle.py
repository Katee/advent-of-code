from collections import Counter
import random


class ProgramStack:
    def __init__(self):
        self.programs = {}

    def add(self, program):
        self.programs[program.name] = program

    def find_by_name(self, name):
        return self.programs[name]

    def all(self):
        return self.programs.values()

    def bottom_program(self):
        current_program = self.programs[random.sample(self.programs.keys(), 1)[0]]
        while True:
            parent = current_program.parent_program
            if parent is not None:
                current_program = parent
            else:
                return current_program


class Program(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.calculated_weight = self.weight
        self.parent_program = None
        self.children = []

    def add_child(self, program):
        self.children.append(program)

    def update_weight(self, weight):
        self.calculated_weight += weight

    def __repr__(self):
        return "Program: '{}' (weight: {} (calc: {}))".format(self.name, self.weight, self.calculated_weight)

    def __hash__(self):
        return hash(str(self) + ''.join([str(c) for c in self.children]))


programs_file = [p.split(" ") for p in open('input.txt').read().strip().split("\n")]
program_stack = ProgramStack()

# allocate all programs
for program_description in programs_file:
    program = Program(program_description[0], program_description[1][1:-1])
    program_stack.add(program)

# set parents
for program_description in programs_file:
    if len(program_description) > 3:
        parent_program = program_stack.find_by_name(program_description[0])

        for program_name in program_description[3:]:
            program_name = program_name.replace(",", "")
            child_program = program_stack.find_by_name(program_name)
            child_program.parent_program = parent_program
            parent_program.add_child(child_program)


# set the weights correctly
for program in program_stack.all():
    weight = program.weight
    while program.parent_program is not None:
        parent = program.parent_program
        parent.update_weight(weight)
        program = parent


def program_weights(programs):
    return Counter([p.calculated_weight for p in programs])


def find_unbalanced_child(programs):
    weights = program_weights(programs)
    least_common_weight = [x for x, c in weights.items() if c == 1]

    if len(least_common_weight) == 0:
        return None

    least_common_weight = least_common_weight[0]

    for program in programs:
        if program.calculated_weight == least_common_weight:
            return program

    return None


def find_unbalanced(bottom_program):
    siblings = []

    while True:
        unbalanced_child = find_unbalanced_child(bottom_program.children)

        if unbalanced_child is None:
            break

        siblings = bottom_program.children
        bottom_program = unbalanced_child

    target_weight = program_weights(siblings).most_common(1)[0][0]
    return bottom_program.weight - abs(bottom_program.calculated_weight - target_weight)

bottom_program = program_stack.bottom_program()

print("star 1: {}".format(bottom_program.name))
print("star 2: {}".format(find_unbalanced(bottom_program)))
