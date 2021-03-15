addend = [0 for a in range(40)]
carry = [0 for b in range(40)]
accumulator = [0 for c in range(40)]


# This is the machinery of the machine
def increment_adder(add, acc, c):
    # This reduces the addend by 1
    add = add - 1
    # This increments accumulator by one
    acc = (acc + 1) % 10
    # If the accumulator is 0 increment the carry
    if acc == 0:
        c = c + 1
    return add, acc, c


def subtracter(add, acc, c):
    add -= 1
    if acc <= 0:
        c += 1
    acc = (acc - 1) % 10

    return add, acc, c


def subtract_digits(add, acc):
    c = 0
    while add > 0:
        [add, acc, c] = subtracter(add, acc, c)
    return acc, c


def add_digits(add, acc):
    c = 0
    while add > 0:
        [add, acc, c] = increment_adder(add, acc, c)
    return acc, c


ac = input('enter intergar less than 41 digits long (accumulator): ')
ae = input('enter intergar less than 41 digits long(addend): ')
inp = input('adding or subtracting? +/-: ')

for index, digit in enumerate(reversed(ac)):
    accumulator[-1 - index] = int(digit)
for index, digit in enumerate(reversed(ae)):
    addend[-1 - index] = int(digit)

print('accumulators: ', accumulator, 'addend: ', addend, sep="\n")

if inp == '+':
    for i, d in reversed(list(enumerate(addend))):
        stack = carry.pop()
        total, remainder = add_digits(d+stack, accumulator[i])
        accumulator[i] = total
        carry.append(remainder)
if inp == '-':
    for i, d in reversed(list(enumerate(addend))):
        stack = carry.pop()
        total, remainder = subtract_digits(d, accumulator[i]-stack)
        accumulator[i] = total % 10
        carry.append(remainder)

print('answer:\n', accumulator)
