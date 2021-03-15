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


def add_digits(add, acc):
    c = 0
    while add > 0:
        [add, acc, c] = increment_adder(add, acc, c)
    return acc, c


ac = input('enter intergar less than 41 digits long: ')
ae = input('enter intergar less than 41 digits long: ')

for index, digit in enumerate(reversed(ac)):
    accumulator[-1 - index] = int(digit)
for index, digit in enumerate(reversed(ae)):
    addend[-1 - index] = int(digit)

print('accumulators: ', accumulator,'addend: ', addend, sep="\n")

for i, d in reversed(list(enumerate(addend))):
    stack = carry.pop()
    total, remainder = add_digits(d, accumulator[i])
    accumulator[i] = total + stack
    carry.append(remainder)

print('answer: ',accumulator)
