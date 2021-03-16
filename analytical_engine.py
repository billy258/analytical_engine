def increment_adder(add, acc, c):
    add = add - 1
    acc = (acc + 1) % 10
    if acc == 0:
        c = c + 1
    return add, acc, c


def decrement_numbers(add, acc, c):
    add -= 1
    if acc <= 0:
        c += 1
    acc = (acc - 1) % 10

    return add, acc, c


def subtract_digits(add, acc):
    c = 0
    while add > 0:
        [add, acc, c] = decrement_numbers(add, acc, c)
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
        carry[i-1] = remainder


def subtraction_mill(add):
    for i, d in reversed(list(enumerate(add))):
        total, remainder = subtract_digits(d, accumulator[i])
        accumulator[i] = total
        carry[i-1] = remainder


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
    print('carry: ', carry)
    for index, c in enumerate(carry):
        accumulator[index] += c
if inp == '-':
    subtraction_mill(addend)
    print('carry: ', carry)
    for index, c in enumerate(carry):
        accumulator[index] -= c


print('answer:\n', accumulator)
