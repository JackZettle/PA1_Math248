
def single_half_adder(A, B):
    sum = A ^ B
    carry = A & B

    return carry, sum


print(single_half_adder(0,0))
print(single_half_adder(0,1))
print(single_half_adder(1,0))
print(single_half_adder(1,1))