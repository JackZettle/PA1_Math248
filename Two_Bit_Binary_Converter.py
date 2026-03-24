##################################################
#Part 2 program
#Take input of base 10 numbers, convert them to binary, be able to add the numbers
##################################################

integer1 = int(input("Enter the Larger Integer:"))
integer2 = int(input("Enter the Smaller Integer:"))

def binary_converter(integer_1,integer_2):
    result_1 = []
    if integer_1 == 0:
        result_1.append(0)

    while integer_1 > 0:
        if integer_1 % 2 == 1:
            result_1.append(1)
        else:
            result_1.append(0)
        integer_1 = integer_1 // 2
    result_1.reverse()
    result_1 = ("".join(map(str,result_1)))


    result_2 = []
    if integer_2 == 0:
        result_2.append(0)

    while integer_2 > 0:
        if integer_2 % 2 == 1:
            result_2.append(1)
        else:
            result_2.append(0)
        integer_2 = integer_2 // 2
    result_2.reverse()
    result_2 = ("".join(map(str,result_2)))
    return result_1, result_2

#-----------------------------------------------------------------------------
num1_bits, num2_bits = binary_converter(integer1, integer2)
#-----------------------------------------------------------------------------
# Two's Complement

def half_adder(bit_a, bit_b):
    """Returns (sum, carry) for two bits."""
    sum_val = bit_a ^ bit_b
    carry_val = bit_a & bit_b
    return (sum_val, carry_val)

def full_adder(bit_a, bit_b, carry_in):
    """Returns (sum, carry_out) for three bits."""
    sum1, carry1 = half_adder(bit_a, bit_b)
    sum2, carry2 = half_adder(sum1, carry_in)
    carry_out = carry1 | carry2
    return (sum2, carry_out)


def two_bit_adder_logic(a_bits, b_bits):
    """
    Adds two 2-bit numbers (strings like '10', '01')
    Returns (carry, s1, s0)
    """

    # Convert to list of ints
    a = [int(bit) for bit in a_bits]
    b = [int(bit) for bit in b_bits]

    # Reverse so index 0 = LSB
    a.reverse()
    b.reverse()

    # LSB addition
    s0, c0 = half_adder(a[0], b[0])

    # MSB addition (with carry)
    s1, c1 = full_adder(a[1], b[1], c0)

    return (c1, s1, s0)

carry_out, sum1, sum0 = two_bit_adder_logic(num1_bits, num2_bits)

print(f"The sum of {num1_bits} and {num2_bits} in binary is: {carry_out}{sum1}{sum0}") 


