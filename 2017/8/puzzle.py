from collections import defaultdict


class Instruction:
    def __init__(self, txt):
        self.register = txt[0]
        self.operation = txt[1]
        self.value = int(txt[2])
        self.predicate = Predicate(txt[4:])

    def __repr__(self):
        return "{} {} {} {}".format(self.register, self.operation, self.value, self.predicate)


class Predicate:
    def __init__(self, txt):
        self.comparison_register = txt[0]
        self.comparison_operation = txt[1]
        self.comparison_value = int(txt[2])

    def __repr__(self):
        return "if {} {} {}".format(self.comparison_register, self.comparison_operation, self.comparison_value)


class Runtime:
    def __init__(self, txt):
        # default all registers to 0
        self.registers = defaultdict(int)
        self.parse_program(txt)

    def parse_program(self, txt):
        self.instructions = []

        for line in txt.split("\n"):
            inst = Instruction(line.split(" "))
            self.instructions.append(inst)

    def evaluate_predicate(self, predicate):
        register_value = self.registers[predicate.comparison_register]

        if predicate.comparison_operation == ">":
            return register_value > predicate.comparison_value
        elif predicate.comparison_operation == "<":
            return register_value < predicate.comparison_value
        elif predicate.comparison_operation == "<=":
            return register_value <= predicate.comparison_value
        elif predicate.comparison_operation == ">=":
            return register_value >= predicate.comparison_value
        elif predicate.comparison_operation == "!=":
            return register_value != predicate.comparison_value
        elif predicate.comparison_operation == "==":
            return register_value == predicate.comparison_value

    def run(self):
        max_held = 0

        for instruction in self.instructions:
            max_held = max([max_held] + self.registers.values())

            if self.evaluate_predicate(instruction.predicate):
                if instruction.operation == "inc":
                    self.registers[instruction.register] += instruction.value
                elif instruction.operation == "dec":
                    self.registers[instruction.register] -= instruction.value

        print("star 1: {}".format(max(self.registers.values())))
        print("star 2: {}".format(max_held))


program = Runtime(open('input.txt').read().strip())
program.run()
