

def half_adder(A, B):
    sum_bit = A ^ B
    carry = A & B

    return sum_bit, carry

def full_adder(A, B, Cin):
    s1, c1 = half_adder(A, B)

    s2, c2 = half_adder(s1, Cin)

    cout = c1 | c2

    return s2, cout


print(full_adder(0,0,0))
print(full_adder(0,0,1))
print(full_adder(0,1,0))
print(full_adder(0,1,1))
print(full_adder(1,0,0))
print(full_adder(1,0,1))
print(full_adder(1,1,0))
print(full_adder(1,1,1))