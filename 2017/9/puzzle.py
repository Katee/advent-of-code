chars = "<{!>}>"
chars = "<!!>"
chars = "<!!!>>"
chars = "<{o\"i!a,<{i<a>"
chars = "<random characters>"
chars = "<<<<>"
chars = "<>"
chars = open('input.txt').read().strip()

do_cancel = False
in_garbage = False
group_stack = []

num_groups = 0
num_garbage = 0

for char in chars:
    print(char)

    if do_cancel:
        print('cancel')
        do_cancel = False
        continue

    if char == "!":
        do_cancel = True
        continue

    if in_garbage:
        if char == ">":
            in_garbage = False
        else:
            num_garbage += 1
        continue

    if char == "<":
        in_garbage = True
    elif char == "{":
        group_stack.append(char)
    elif char == "}":
        num_groups += len(group_stack)
        group_stack.pop()
        print("group closed")

print(num_groups)
print(num_garbage)
