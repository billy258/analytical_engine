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
length_ac = len(ac)
length_ae = len(ae)

for index, digit in enumerate(ac):
    accumulator[index] = int(digit)
for index, digit in enumerate(ae):
    addend[index] = int(digit)

for number in range(len(accumulator)):

print(accumulator, addend, sep=' ')
print(add_digits(addend, accumulator))
