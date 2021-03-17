def increment_adder(add, acc, c):
    add = add - 1
    acc = (acc + 1) % 10
    if acc == 0:
        c = c + 1
    return add, acc, c
# The carry here means the number being carried to the next most significant digit


def decrement_numbers(acc, add, c):
    acc = (acc - 1) % 10
    add -= 1
    if acc == 9:
        c -= 1
    return acc, add, c
# The carry here means if c = 0, there is a number carried forward, c = 1 means there isn't


def subtract_digits(acc, add):
    c = 1
    while add > 0:
        [acc, add, c] = decrement_numbers(acc, add, c)
    return acc, c


def add_digits(add, acc):
    c = 0
    while add > 0:
        [add, acc, c] = increment_adder(add, acc, c)
    return acc, c


def addition_mill(add):
    for i, d in reversed(list(enumerate(add))):
        total, remainder = add_digits(d, accumulator[i])
        accumulator[i] = total
        carry[i] = remainder


def subtraction_mill(add):
    for i, d in reversed(list(enumerate(add))):
        total, remainder = subtract_digits(accumulator[i], d)
        accumulator[i] = total
        carry[i] = remainder


def axes_maker(string, axes):
    for wheel, digit in enumerate(reversed(string)):
        axes[-1 - wheel] = int(digit)


addend = [0 for a in range(40)]
carry = [0 for b in range(40)]
accumulator = [0 for c in range(40)]

ac = input('enter integer less than 41 digits long (accumulator): ')
ae = input('enter integer less than 41 digits long(addend): ')
inp = input('adding or subtracting? +/-: ')

axes_maker(ac, accumulator)
axes_maker(ae, addend)

print('accumulator: ', accumulator, 'addend: ', addend, sep="\n")

if inp == '+':
    addition_mill(addend)
    for index in reversed(range(40)):
        if carry[index] > 0:
            accumulator[index-1] = (accumulator[index-1] + 1) % 10
            if accumulator[index-1] == 0:
                carry[index-1] += 1
    print('carry:\n', carry)
    print('answer:\n', accumulator)
if inp == '-':
    subtraction_mill(addend)
    for index in reversed(range(40)):
        if carry[index] == 0:
            accumulator[index-1] = (accumulator[index-1] - 1) % 10
            if accumulator[index-1] == 9:
                carry[index-1] = 0
    print('carry:\n', carry)
    print('answer:\n', accumulator.join())
