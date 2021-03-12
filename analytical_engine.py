addend = [0 for i in range(40)]
carry = [0 for i in range(40)]
accumulator = [0 for i in range(40)]

#This is the machinery of the machine
def increment_adder(addend, accumulator, carry):
#This reduces the addend by 1   
    addend = addend - 1
 #This increments accumulator by one   
    accumulator = (accumulator + 1) % 10
#If the accumulator is 0 increment the carry
    if accumulator == 0:
        carry = carry + 1
    return addend, accumulator, carry

def add_digits(addend, accumulator):
    carry = 0

    while addend > 0:
        [addend, accumulator, carry] = increment_adder(addend, accumulator, carry)

    return accumulator, carry

acc = input('enter integar less than 41 digits long: ')
addend = input('enter integar less than 41 digits long: ')

for index, digit in enumerate(acc):
    accumulator[len(acc) - digit] = digit
for index, digit in enumerate(addend):
    addend[len(addend) - index] = digit


print(acc, addend, sep = ' ')
print(add_digits(addend, acc))

